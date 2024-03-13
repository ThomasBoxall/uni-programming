{- Week6.hs
 This module illustrates the use of functions as values
-}

import Data.Char

twice :: (Int -> Int) -> Int -> Int
twice f x = f (f x)

multiply :: Int -> Int -> Int
multiply x y = x * y

double :: Int -> Int
double = multiply 2

doubleAll :: [Int] -> [Int]
doubleAll = map (*2)

areDigits :: String -> [Bool]
areDigits = map isDigit

keepPositive :: [Int] -> [Int]
keepPositive = filter (>0)

keepDigits :: String -> String
keepDigits = filter isDigit

addUp :: [Int] -> Int
addUp = foldr (+) 0 

myConcat :: [[a]] -> [a]
myConcat = foldr (++) []

-- programming exercises

-- q1
mult10 :: [Int] -> [Int]
mult10 xs = map (10*) xs

-- q2
onlyLowerCase :: String -> String
onlyLowerCase = filter (isLower)

-- q3
orAll :: [Bool] -> Bool
orAll = foldr (||) False

-- q4
sumSquares :: [Int] -> Int
sumSquares xs =  foldr (+) 0 (map (^2) xs)

-- q5
zeroToTen :: [Int] -> [Int]
zeroToTen xs = filter (<= 10) (filter (>= 0) xs)

-- q6 
squareRoots :: [Float] -> [Float]
squareRoots xs = map (sqrt) (filter (>=0) xs)

-- q7
countBetween :: Float -> Float -> [Float] -> Int
countBetween a b xs = length (filter (<= b) (filter (>= a) xs))

-- q8 solution 1
alwaysPositive :: (Float -> Float) -> [Float] -> Bool
alwaysPositive f xs = length (filter (>=0) (map f xs)) == length xs

-- q8 solution 2
alwaysPositiveTwo :: (Float -> Float) -> [Float] -> Bool
alwaysPositiveTwo f xs = andAll (map ((>=0) . f) xs)

andAll :: [Bool] -> Bool
andAll xs = foldr (&&) True xs

-- q8 solution 3
alwaysPositiveThree :: (Float -> Float) -> [Float] -> Bool
alwaysPositiveThree f = andAll . map ((>=0) . f)

-- q9
productSquareRoots :: [Float] -> Float
productSquareRoots xs = foldr (*) 1 (filter (>=0) (map sqrt xs))

-- q10
removeFirst :: (a -> Bool) -> [a] -> [a]
removeFirst _ [] = []
removeFirst f (x:xs)
    | (f) x  =  xs
    | otherwise = x : removeFirst f xs

-- q11
-- removeLast :: (a -> Bool) -> [a] -> [a]
-- cont'd here 