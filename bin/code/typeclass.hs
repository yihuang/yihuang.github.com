import Data.Monoid
import Prelude hiding(Functor, fmap, (>>=), (>>), Monad)

class Functor f where
    fmap :: (a -> b) -> f a -> f b

instance Functor Maybe where
    fmap g Nothing = Nothing
    fmap g (Just a) = Just (g a)

instance Functor (Either e) where
    fmap _ (Left e) = Left e
    fmap g (Right a) = Right (g a)

instance Functor ((->) e) where
    -- fmap g f = g . f
    -- 化简可得：
    fmap = (.)

instance Functor ((,) e) where
    fmap g (e, a) = (e, g a)

class Functor f => Pointed f where
    pure :: a -> f a

instance Pointed Maybe where
    pure = Just

instance Pointed ((->) e) where
    pure = const

instance Pointed (Either e) where
    pure = Right

instance (Monoid e) => Pointed ((,) e) where
    -- pure a = (mempty, a)
    -- 化简可得：
    pure = (,) mempty

class (Pointed f) => Applicative f where
    (<*>) :: f (a -> b) -> f a -> f b

instance Applicative Maybe where
    Nothing <*> _ = Nothing
    (Just g) <*> f = fmap g f

instance Applicative (Either e) where
    (Left e) <*> _ = Left e
    (Right g) <*> f = fmap g f

instance Applicative ((->) e) where
    (ff <*> f) e = (ff e) (f e)

instance (Monoid e) => Applicative ((,) e) where
    (e1, g) <*> (e2, a) = (mappend e1 e2, g a)

class (Applicative m) => Monad m where
    (>>=) :: m a -> (a -> m b) -> m b
    (>>) :: m a -> m b -> m b
    ma >> mb = ma >>= \_->mb

instance Monad Maybe where
    Nothing >>= _ = Nothing
    (Just a) >>= g = g a

instance Monad (Either e) where
    (Left e) >>= _ = Left e
    (Right a) >>= g = g a

instance Monad ((->) e) where
    ( m >>= g ) e = g (m e) e = (g . m) e e
    -- 或者
    -- ( m >>= g ) e = (g . m) e e

instance (Monoid e) => Monad ((,) e) where
    (_, a) >>= g = g a
