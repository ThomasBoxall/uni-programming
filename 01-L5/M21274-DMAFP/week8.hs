helloWorld :: IO ()
helloWorld = putStrLn "Hello, World!"

displayFile :: IO ()
displayFile = do 
    putStr "Enter the filename: "
    name <- getLine
    contents <- readFile name
    putStr contents

getInt :: IO Int
getInt = do 
    str <- getLine
    return (read str :: Int)

isPalindrome :: String -> String
isPalindrome str
   | str == reverse str  = str ++ " is a palindrome"
   | otherwise           = str ++ " is not a palindrome"

pal :: IO ()
pal = do 
    line <- getLine
    let response = isPalindrome line
    putStrLn response

palLines :: IO ()
palLines = do 
    putStr "Enter a line: "
    str <- getLine
    if str == "" then 
        return ()
    else do 
        putStrLn (isPalindrome str)
        palLines


-- exercises

-- q1
greeting :: IO ()
greeting = do
    putStrLn "Enter your name: "
    name <- getLine
    putStrLn ("Hello " ++ name)

-- q2
addTwoNumbers :: IO ()
addTwoNumbers = do
    putStrLn "Enter number 1: "
    numb1Str <- getLine
    putStrLn "Enter number 2: "
    numb2Str <- getLine
    let numb1 = read numb1Str :: Int
    let numb2 = read numb2Str :: Int
    putStrLn ("your numbers add to: " ++ show (numb1 + numb2))

-- q3
copyFile :: IO ()
copyFile = do
    putStrLn "Gimmie a file"
    pathToCopy <- getLine
    fileContents <- readFile pathToCopy
    putStrLn "Gimmie a name of the copyfile"
    pathToPaste <- getLine
    writeFile pathToPaste fileContents

-- q4
buildList :: [String] -> IO()
buildList list = do
    putStrLn "Enter string or press return to exit"
    newString <- getLine
    if newString == ""
        then print list
        else buildList (list ++ [newString])

listBuilder :: IO()
listBuilder = do
    buildList []

-- q5
adder :: Int -> Int -> IO()
adder total remaining = do
    putStrLn "enter number to add"
    numbStr <- getLine
    let numb = read numbStr :: Int
    if (remaining - 1 > 0)
        then adder (total + numb) (remaining - 1)
        else print(total + numb)
    
adderCaller :: IO()
adderCaller = do
    putStrLn "how many numbers do you want to add?"
    numbStr <- getLine
    let toAdd = read numbStr :: Int
    adder 0 toAdd