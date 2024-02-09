-- week 3 (w/c 2024-02-05)

-- We don't import '||' from the prelude, so that we can
-- define our own version

import Prelude hiding ((||), (&&), gcd)

-- The following line declares the || operator (which we are about to
-- re-define) to be right associative and to have precedence 2. This
-- is necessary in order for expressions such as False || x > 2 to be
-- valid (e.g. it sets the precedence of || to be lower than >).

infixr 2 ||

infixr 3 &&

-- A naive re-implementation of the Prelude operator ||
(||) :: Bool -> Bool -> Bool
True || True = True
False || True = True
True || False = True
False || False = False

-- An alternative re-implementation
--(||) :: Bool -> Bool -> Bool
--False || False   = False
--_ || _           = True

-- Another alternative re-implementation
--(||) :: Bool -> Bool -> Bool
--True || _     =  True
--False || a    = a

fact :: Int -> Int
fact n
  | n == 0 = 1
  | n > 0 = n * fact (n - 1)
  | otherwise = error "factorials not defined for negative ints"

mult :: Int -> Int -> Int
mult n m
  | n == 0 = 0
  | n > 0 = m + mult (n - 1) m
  | otherwise = - mult (- n) m

divide :: Int -> Int -> Int
divide n m
  | n < m = 0
  | otherwise = 1 + divide (n - m) m

-- worked example 2: fibonacci
fibonacci :: Int -> Int
-- fibonacci n
-- | n == 0 = 0
-- | n == 1 = 1
-- | otherwise = fibonacci (n - 1) + fibonacci (n - 2)
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n - 1) + fibonacci (n - 2)


-- programming exercises

-- q1
-- note the infixr line is at the top of the document with the one for or

-- impl 1
-- (&&) :: Bool -> Bool -> Bool
-- False && False = False
-- False && True = False
-- True && False = False
-- True && True = True

-- impl 2
-- (&&) :: Bool -> Bool -> Bool
-- True && True = True
-- _ && _ = False

-- impl 3
(&&) :: Bool -> Bool -> Bool
False && _ = False
True && a = a

-- q2
exOr :: Bool -> Bool -> Bool
exOr False True = True
exOr True False = True
exOr _ _ = False

-- q3
ifThenElse :: Bool -> Int -> Int -> Int
ifThenElse True a b = a
ifThenElse False a b = b

-- q4
daysInMonth :: Int -> Int
daysInMonth 2 = 28
daysInMonth 4 = 30
daysInMonth 9 = 30
daysInMonth 11 = 30
daysInMonth _ = 31

-- q4.2 (rewrite of validDate from previous week)
validDate :: Int -> Int -> Bool
validDate d m =  daysInMonth m >= d

-- q5
smallNumbers :: Int -> Int
smallNumbers x
    | x == 0 = 0
    | x > 0 = x + smallNumbers (x-1)
    | otherwise = error "thats smaller than 0"

-- q6
-- sumSquares :: Int -> Int
-- sumSquares x
--     | x == 0 = 0
--     | x > 0 = x ^ 2 + sumSquares (x-1)
--     | otherwise = error "negative!"

-- q5 rewrite (for q11)
sumSquares :: Int -> Int
sumSquares 0 = 0
sumSquares _ > 0 = _ ^ 2 + sumSquares (_ - 1)
sumSquares _ = error "negative!"

-- q7
power :: Int -> Int -> Int
power b p
    | p == 1 = b
    | p >= 1 = power (b * b) (p - 1) 
    | otherwise = error "negative"

-- to be continued FIX THIS ONE

-- q8
sumFromTo :: Int -> Int -> Int
sumFromTo f t
    | t < f = 0
    | t >= f = f + sumFromTo (f + 1) t

-- q9
gcd :: Int -> Int -> Int
gcd a b
    | a == b = a
    | a > b = gcd (a - b) b
    | b > a = gcd (b - a) a
    | otherwise = error "error"

-- q10
intSquareRoot :: Int -> Int
intSquareRoot n = findRoot n n

findRoot :: Int -> Int -> Int
findRoot n s
    | n >= (s * s) = s
    | s > 0 = findRoot n (s-1)
    | otherwise = error "not found"