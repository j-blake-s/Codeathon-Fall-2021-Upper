import Control.Monad (replicateM)
import Data.List (break, sortOn)

  -- TODO REMOVE BLOCK
-- import Debug.Trace
-- import Text.Printf
-- showDate :: Integer -> String
-- showDate d = printf "%02d:%02d" (d `div` 60) (d `mod` 60)
-- showDateRange (start, end) = showDate start ++ " " ++ showDate end
-- END REMOVE BLOCK

getInput n = replicateM n getLine

pair [a,b] = (a,b)
pair _ = error "Invalid pair"

parseLine line = pair $ map parseDate (words line)

parseDate date = 60 * read (take 2 date) + read (drop 3 date)

foldOne (count, (lastEnd, scheduleBlocks)) (newStart, newEnd)
    | newStart < lastEnd = 
                        --    trace "X"
                           (count, (lastEnd, scheduleBlocks))
    | otherwise          =
                        --    trace (showDate newStart ++ " " ++ showDate newEnd)
                        --    trace "X"
                           (count+1, (newEnd, (newStart, newEnd) : scheduleBlocks))

solve blocks =
    let sortedBlocks = sortOn snd blocks
    in 
        -- traceShow (length sortedBlocks) $
        foldl foldOne (0, (0, [])) sortedBlocks

winner alice bob
    | alice > bob = "Alice\n" ++ show alice
    | bob > alice = "Bob\n" ++ show bob
    | otherwise   = "Tie\n" ++ show alice  -- Equal to bob

main = do
    n <- getLine
    aInput <- getInput (read n :: Int)
    m <- getLine
    bInput <- getInput (read m :: Int)
    let aBlocks = map parseLine aInput
    let bBlocks = map parseLine bInput
    let (aScore, (_, aSchedule)) = solve aBlocks
    let bScore = fst $ solve bBlocks
    -- traceM $ unlines $ map showDateRange $ reverse aSchedule
    -- print aBlocks
    -- print aScore
    -- print bBlocks
    -- print bScore
    putStrLn $ winner aScore bScore
