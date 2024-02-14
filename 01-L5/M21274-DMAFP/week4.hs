import Data.Char

type StudentMark = (String, Int)

betterStudent :: StudentMark -> StudentMark -> String
betterStudent (s1, m1) (s2, m2)
  | m1 >= m2 = s1
  | otherwise = s2

marks :: [StudentMark] -> [Int]
marks stmks = [mk | (st, mk) <- stmks]

pass :: [StudentMark] -> [String]
pass stmks = [st | (st, mk) <- stmks, mk >= 40]

-- An example list of student marks
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

addPairs :: [(Int, Int)] -> [Int]
addPairs pairList = [i + j | (i, j) <- pairList]

minAndMax :: Int -> Int -> (Int, Int)
minAndMax x y
  | x <= y = (x, y)
  | otherwise = (y, x)

-- programming exercises
-- q1
sumDifference :: Int -> Int -> (Int,Int)
sumDifference a b = (a+b, a-b)

-- q2
grade :: StudentMark -> Char
grade (_, s)
    | s <= 100 && s >= 70 = 'A'
    | s >= 60 = 'B'
    | s >= 50 = 'C'
    | s >= 40 = 'D'
    | s >= 0 = 'F'
    | otherwise = error "invalid grade"

-- q3
capMark :: StudentMark -> StudentMark
capMark (n, s)
    | s <= 40 && s >= 0 = (n, s)
    | s <= 100 = (n, 40)
    | otherwise = error "invalid grade"

-- q4
firstNumbers :: Int -> [Int]
firstNumbers x = [1 .. x]

-- q5
firstSquares :: Int -> [Int]
firstSquares x = [x ^ 2 | x <- firstNumbers x ]

-- q6
capitalise :: String -> String
capitalise a = [toUpper l | l <- a]

-- q7
onlyDigits :: String -> String
onlyDigits x = [a | a <- x, isDigit a]

-- q8
capMarks :: [StudentMark] -> [StudentMark]
capMarks input = [capMark (a,b) | (a,b) <- input]

-- q9
gradeStudents :: [StudentMark] -> [(String, Char)]
gradeStudents input = [(a, grade (a,b)) | (a,b) <- input]