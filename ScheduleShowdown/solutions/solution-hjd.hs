import Control.Monad (replicateM)
import Data.List (break, sortOn, foldl')

getInput n = replicateM n getLine

pair [a,b] = (a,b)
pair _ = error "Invalid pair"

parseLine line = pair $ map parseDate (words line)

parseDate date = 60 * read (take 2 date) + read (drop 3 date)

foldOne (count, lastEnd) (newStart, newEnd)
    | newStart < lastEnd = (count, lastEnd)
    | otherwise          = (count+1, newEnd)

solve blocks =
    let sortedBlocks = sortOn snd blocks
    in foldl' foldOne (0, 0) sortedBlocks

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
    let aScore = fst $ solve aBlocks
    let bScore = fst $ solve bBlocks
    putStrLn $ winner aScore bScore
