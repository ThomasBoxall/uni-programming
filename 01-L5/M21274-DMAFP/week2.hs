-- Week 2 (w/c 2024-01-29)

-- programming exercises
-- q1 
absolute :: Int -> Int
absolute a 
    | a >= 0 = a
    | otherwise = a * (-1)

-- q2
sign :: Int -> Int
sign a 
    | a < 0 = (-1)
    | a == 0 = 0
    | otherwise = 1

-- q3
howManyEqual :: Int -> Int -> Int -> Int
howManyEqual a b c 
    | a == b && b == c = 3
    | a == b = 2
    | a == c = 2
    | b == c = 2
    | otherwise = 0

-- q4
sumDiagonalLengths :: Float -> Float -> Float -> Float
sumDiagonalLengths a b c = dl a + dl b + dl c
    where 
        dl :: Float -> Float
        dl a = sqrt (2 * a^2)

-- q5
taxiFare :: Int -> Float
taxiFare dist
    | dist <= 10 = baseFair + (fromIntegral(dist) * 0.5)
    | otherwise = baseFair + (10 * 0.5) + (fromIntegral(dist-10) * 0.3)
    where
        baseFair = 2.20

-- q6
howManyAboveAverage :: Int -> Int -> Int -> Int
howManyAboveAverage x y z
    | a > avg && b > avg = 2
    | b > avg && c > avg = 2
    | a > avg && c > avg = 2
    | a > avg || b > avg || c > avg = 1
    | otherwise = 0
    where
        avg = (a + b + c) / 3
        a = fromIntegral x
        b = fromIntegral y
        c = fromIntegral z
{-
    Test cases:
    1 1 10 (1)
    1 100 100 (2) 
    1 1 1 (0)
-}
        
-- q7
validDate :: Int -> Int -> Bool
validDate d m
    | (m == 1 || m == 3 || m == 5 || m == 7 || m == 8 || m == 10 || m == 12) && d <= 31 = True
    | m == 2 && d <= 29 = True
    | (m == 4 || m == 6 || m == 9 || m == 11) && d <= 30 = True
    | otherwise = False
    
-- q8
daysInMonth :: Int -> Int -> Int
daysInMonth m y
    | m == 2 = daysInFeb y
    | m == 4 || m == 6 || m == 9 || m == 11 = 30
    | otherwise = 31 -- we can assume all inputs will be valid so can just do this
    -- to handle invalid cases, we'd want to use the first guard fro validDate to return 31, then have our otherwise guard as returning 0 or a value which clearly indicates an invalid value has been entered.
    where
        daysInFeb y = if (mod y 4 == 0) then 29 else 28

-- written exercises

-- q1
{-
sumThree 3 5 7    
~> 3 + 5 + 7           definition of sumThree
~> 3 + 12              arithmetic
~> 15                  arithmetic

sumThree 8 (1 + 3) 2
~> 8 + (1 + 3) + 2     definition of sumThree
~> 8 + 4 + 2           arithmetic
~> 12 + 2              arithmetic
~> 14                  arithmetic
-}

-- q2
{-
threeDifferent 1 4 2
~> different 1 4 && different 1 2 && different 4 2 && different 1 2     definition of threeDifferent
~> 1 /= 4                                                               definition of first call of different
~> True                                                                 def of /=
~> True && different 1 2 && different 4 2 && different 1 2              updated definition of threeDifferent
~> 1 /= 2                                                               definition of second call of different
~> True                                                                 def of /=
~> True && True && different 4 2 && different 1 2                       updated definition of threeDifferent
~> 4 /= 2                                                               definition of third call of different
~> True                                                                 def of /=
~> True && True && True && different 1 2                                updated definition of threeDifferent
~> 1 /= 2                                                               definition of fourth (final) call of different
~> True                                                                 def of /=
~> True && True && True && True                                         updated definition of threeDifferent
~> True                                                                 result

threeDifferent 1 7 7
~> different 1 7 && different 1 7 && different 7 7 && different 1 7     definition of threeDifferent
~> 1 /= 7                                                               definition of first call of different
~> True                                                                 def of /=
~> True && different 1 7 && different 7 7 && different 1 7              updated definition of threeDifferent
~> 1 /= 7                                                               definition of second call of different
~> True                                                                 def of /=
~> True && True && different 7 7 && different 1 7                       updated definition of threeDifferent
~> 7 /= 7                                                               definition of third call of different
~> False                                                                def of /=
~> True && True && False && different 1 7                               updated definition of threeDifferent
~> 1 /= 7                                                               definition of fourth (final) call of different
~> True                                                                 def of /=
~> True && True && False && True                                        updated definition of threeDifferent
~> False                                                                result  
-}

-- q3
{-
howManyEqual 3 5 2
??  3 == 5 && 5 == 2       first guard
??  ~> False && 5 == 2     def of ==
??  ~> False && False      def of ==
??  ~> False               def of &&
??  3 == 5                 second guard
??  ~> False               def of ==
??  3 == 2                 third guard
??  ~> False               def of ==
??  5 == 2                 fourth guard
??  ~> False               def of ==
??  otherwise              fifth guard
??  ~> True                def of otherwise
~> 0

howManyEqual 5 2 5
??  5 == 2 && 2 == 5       first guard
??  ~> False && 2 == 5     def of ==
??  ~> False && False      def of ==
??  ~> False               def of &&
??  5 == 2                 second guard
??  ~> False               def of ==
??  5 == 5                 third guard
??  ~> True                def of ==
~> 2
-}