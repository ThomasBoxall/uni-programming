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
tenTimes :: Int -> Int
tenTimes x = 10 * x

sumThree :: Int -> Int -> Int -> Int
sumThree a b c = a + b + c

areaOfCircle :: Float -> Float
areaOfCircle r = pi * r ^ 2

volumeOfCylinder :: Float -> Float -> Float
volumeOfCylinder r h = areaOfCircle r * h

