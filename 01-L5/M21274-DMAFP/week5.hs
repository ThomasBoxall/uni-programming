{- Week5.hs
 This file illustrates list patterns and recursion over lists.
-}

import Prelude hiding (concat, fst, head, reverse, snd, sum, tail, zip)

-- Definitions of the prelude functions fst and snd

fst (x, _) = x

snd (_, y) = y

-- Definitions of the prelude functions head and tail

head :: [p] -> p
head (x : _) = x
head [] = error "head: empty list"

tail :: [a] -> [a]
tail (_ : xs) = xs
tail [] = error "tail: empty list"

absFirst :: [Int] -> Int
absFirst [] = -1
absFirst (x : xs) = abs x

sum :: [Int] -> Int
sum [] = 0
sum (x : xs) = x + sum xs

doubleAll :: [Int] -> [Int]
doubleAll [] = []
doubleAll (x : xs) = 2 * x : doubleAll xs

concat :: [[a]] -> [a]
concat [] = []
concat (x : xs) = x ++ concat xs

reverse :: [a] -> [a]
reverse [] = []
reverse (x : xs) = reverse xs ++ [x]

zip :: [a] -> [b] -> [(a, b)]
zip (x : xs) (y : ys) = (x, y) : zip xs ys
zip _ _ = []

-- For question 10
type StudentMark = (String, Int)

testData :: [StudentMark]
testData =
  [ ("John", 53),
    ("Sam", 16),
    ("Kate", 85),
    ("Jill", 65),
    ("Bill", 37),
    ("Amy", 22),
    ("Jack", 41),
    ("Sue", 71)
  ]

-- programming exercises

-- q1
headPlusOne :: [Int] -> Int
headPlusOne intList
    | intList == [] = -1
    | otherwise = intList!!0 + 1

-- q2
duplicateHead :: [a] -> [a]
duplicateHead [] = []
duplicateHead (x:xs) = x:(x:xs)

--q3 
rotate :: [a] -> [a]
rotate [a] = [a]
rotate [a,b] = [a,b]
rotate (x:y:xs) = y:x:xs

-- q4
listLength :: [a] -> Int
listLength [] = 0
listLength (x:xs) = 1 + listLength xs

-- q5
multAll :: [Int] -> Int
multAll [] = 1
multAll (x:xs) = x * multAll xs

-- q6
andAll :: [Bool] -> Bool
andAll [] = True
andAll (x:xs) = x && andAll xs

-- q7
orAll :: [Bool] -> Bool
orAll [] = False
orAll (x:xs) = x || orAll xs

-- q8
countIntegers :: Int -> [Int] -> Int
countIntegers _ [] = 0
countIntegers toFind (x:xs)
    | x == toFind = 1 + countIntegers toFind xs
    | otherwise = countIntegers toFind xs

-- q9
removeAll :: Int -> [Int] -> [Int]
removeAll _ [] = []
removeAll toRemove (x:xs)
  | x == toRemove = removeAll toRemove xs
  | otherwise = x : removeAll toRemove xs

-- q10
removeAllButFirst :: Int -> [Int] -> [Int]
removeAllButFirst _ [] = []
removeAllButFirst toRemove (x:xs)
    | toRemove == x = x : removeAll toRemove xs
    | otherwise = x : removeAllButFirst toRemove xs

-- q11
listMarks :: String -> [StudentMark] -> [Int]
listMarks _ [] = []
listMarks name (x:xs)
  | name == fst x = snd x : listMarks name xs
  | otherwise = listMarks name xs

-- q12
sorted :: [Int] -> Bool
sorted [] = True
sorted (x:xs)
  | xs == [] = True -- requires this line to catch where xs is empty and we only have an x
  | x <= xs!!0 = True && sorted xs
  | otherwise = False

-- q13
prefix :: [Int] -> [Int] -> Bool
prefix [] _ = True
prefix (x:xs) (y:ys)
  | x == y = True && prefix xs ys
  | otherwise = False

-- q14
subSequence :: [Int] -> [Int] -> Bool
subsequence _ [] = False
subSequence (x:xs) (y:ys)
  | prefix (x:xs) (y:ys) == True = True
  | prefix (x:xs) (y:ys) == False = subSequence (x:xs) ys
  -- | otherwise = False
  