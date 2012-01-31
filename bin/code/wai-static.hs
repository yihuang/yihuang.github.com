import Control.Applicative ( (<$>) )
import Data.Maybe (fromMaybe, listToMaybe)
import System.Environment (getArgs)
import Network.Wai.Handler.Warp (run)
import Network.Wai.Application.Static ( staticApp
                                      , defaultFileServerSettings)

main :: IO ()
main = do
    port <- read . fromMaybe "3000" . listToMaybe <$> getArgs
    run port $ staticApp defaultFileServerSettings
