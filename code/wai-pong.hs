{-# LANGUAGE OverloadedStrings #-}
import Control.Applicative ( (<$>) )
import Data.Maybe (fromMaybe, listToMaybe)
import System.Environment (getArgs)
import Network.HTTP.Types
import Network.Wai
import Network.Wai.Handler.Warp (run)
import Blaze.ByteString.Builder (fromByteString)

pong :: Application
pong req = return $ ResponseBuilder
                      statusOK
                      [("Content-Type", "text/plain")]
                      (fromByteString "pong")

main :: IO ()
main = do
    port <- read . fromMaybe "3000" . listToMaybe <$> getArgs
    run port pong
