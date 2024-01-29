-- worked examples from worksheet 1
-- worked example 1
circumferenceOfCircle :: Float -> Float
circumferenceOfCircle d = pi * d

sideOfCylinder :: Float -> Float -> Float
sideOfCylinder d h = circumferenceOfCircle d * h

-- worked example 2
canDrink :: Int -> Bool
canDrink age = age >= 18

all3CanDrink :: Int -> Int -> Int -> Bool
all3CanDrink a b c = canDrink a && canDrink b && canDrink c

-- programming exercises

-- q1
tenTimes :: Int -> Int
tenTimes x = 10 * x

-- q2
sumThree :: Int -> Int -> Int -> Int
sumThree a b c = a + b + c

-- q3
areaOfCircle :: Float -> Float
areaOfCircle r = pi * r ^ 2

-- q4
volumeOfCylinder :: Float -> Float -> Float
volumeOfCylinder r h = areaOfCircle r * h

-- q5
distance :: Float -> Float -> Float -> Float -> Float
distance x1 y1 x2 y2 = sqrt ((y1 - y2)^2 + (x1-x2)^2)

-- q6 (using a helper function to check individual pair)
threeDifferent :: Int -> Int -> Int -> Bool
threeDifferent a b c = different a b && different a c && different b c && different a c

different :: Int -> Int -> Bool
different a b = if a/=b then True else False

-- q7
divisibleBy :: Int -> Int -> Bool
divisibleBy a b = if (mod a b) == 0 then True else False

-- q8
isEven :: Int -> Bool
isEven a = if (mod a 2) == 0 then True else False

-- q9 (using q2's function to help)
averageThree :: Int -> Int -> Int -> Float
averageThree a b c = fromIntegral (sumThree a b c) / 3

-- q10 
absolute :: Int -> Int
absolute a = if a >= 0 then a else a * (-1)