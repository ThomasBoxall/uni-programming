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
    | dist <= 10 = 2.20 + (fromIntegral(dist) * 0.5)
    | otherwise = 2.20 + (10 * 0.5) + (fromIntegral(dist-10) * 0.3)

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
    where
        daysInFeb y = if (mod y 4 == 0) then 29 else 28