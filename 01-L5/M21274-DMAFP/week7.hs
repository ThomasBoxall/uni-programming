-- Day algebraic type
data Day = Mon | Tue | Wed | Thur | Fri | Sat | Sun
  deriving (Eq, Ord, Show, Read)

-- Alternative definitions of isWeekend function
isWeekend :: Day -> Bool
isWeekend Sat = True
isWeekend Sun = True
isWeekend _ = False

isWeekend2 day = day == Sat || day == Sun

isWeekend3 day = day >= Sat

-- Copy of StudentMark type synonym from worksheet 4
data StudentMark = Student String Int
  deriving (Eq, Show)

betterStudent :: StudentMark -> StudentMark -> String
betterStudent (Student s1 m1) (Student s2 m2)
  | m1 >= m2 = s1
  | otherwise = s2

-- Shapes algebraic type
data Shape = Circle Float | Rectangle Float Float
    deriving (Eq, Show)

area :: Shape -> Float
area (Circle r) = pi * r * r
area (Rectangle h w) = h * w

-- Address algebraic type (note that a constructor can have
-- the same name as the type).
data Address = Address Building String
  deriving (Show)

data Building = Name String | Number Int
  deriving (Show)

-- Binary tree algebraic type
data Tree = Null | Node Int Tree Tree
  deriving (Show, Eq)

-- Binary tree test data
testTree = Node 20 (Node 3 (Node 12 Null Null) (Node 7 Null Null)) (Node 8 (Node 4 (Node 6 Null Null) Null) Null)

-- Binary search tree test data
testSearchTree = Node 5 (Node 1 Null Null) (Node 8 (Node 7 Null Null) Null)

height :: Tree -> Int
height Null = 0
height (Node _ st1 st2) = 1 + max (height st1) (height st2)

sumValues :: Tree -> Int
sumValues Null = 0
sumValues (Node n st1 st2) = n + sumValues st1 + sumValues st2


-- q1
data Month = Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec
    deriving (Eq, Ord, Show, Read)

data Season = Spring | Summer | Autumn | Winter
    deriving (Eq, Ord, Show, Read)

-- q2
season :: Month -> Season
season mnth
    | mnth >= Mar && mnth <= May = Spring
    | mnth >= Jun && mnth <= Aug = Summer
    | mnth >= Sep && mnth <= Nov = Autumn
    | otherwise = Winter

-- q3 
numberOfDays :: Month -> Int -> Int
numberOfDays mnth year
    | mnth == Feb = if (mod year 4) == 0 then 29 else 28
    | mnth == Apr || mnth == Jun || mnth == Sep || mnth == Nov = 30
    | otherwise = 31

-- q4
data Point = Point Float Float
    deriving (Eq, Show)

-- q5
data PositionedShape = PositionedShape Shape Point
    deriving (Eq, Show)

-- q6 
move :: PositionedShape -> Float -> Float -> PositionedShape
move (PositionedShape shape (Point cx cy)) dx dy = PositionedShape shape (Point (cx + dx) (cy + dy))

-- test data: move (PositionedShape (Circle 7) (Point 13 15)) 10 10

-- q7
numberOfNodes :: Tree -> Int
numberOfNodes Null = 0
numberOfNodes (Node _ lst rst) = 1 + numberOfNodes lst + numberOfNodes rst

-- q8
isMember :: Int -> Tree -> Bool
isMember _ Null = False
isMember val (Node nVal lst rst)
    | val == nVal = True
    | otherwise = (isMember val lst) || (isMember val rst)

-- q9
leaves :: Tree -> [Int]
leaves Null = []
leaves (Node val lst rst)
    | lst == Null && rst == Null = [val]
    | otherwise = leaves (lst) ++ leaves(rst)

-- q10
inOrder :: Tree -> [Int]
inOrder Null = []
inOrder (Node val lst rst) = inOrder(lst) ++ [val] ++ inOrder(rst)

-- additional test data
testBinaryTree = Node 5 (Node 1 Null Null) (Node 8 (Node 7 Null Null) Null)

-- q11
-- insert :: Int -> Tree -> Tree
-- insert new Null = Node(new Null Null)
-- insert new (Node val lst rst)
--     | 