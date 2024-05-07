-- M21274 MATHFUN Functional Programming in-class test 2024/25 - Sample

{-
Exercise 1 - 4 marks
--------------------
Using guards or pattern matching, write a price function which returns the
price of an item on a menu, where "Pizza" costs 8.25, "Pasta" costs 7.95, and 
"Salad" costs 6.55. Your function should return 0.0 for any other parameter 
value (i.e. everything else on the menu is free).
-}

price :: String -> Float
price "Pizza" = 8.25
price "Pasta" = 7.95
price "Salad" = 6.55
price _ = 0.0
-- *** Uncomment the line above and add your code here ***


{-
Exercise 2 - 4 marks
--------------------
Using a list comprehension and the describeTemperature function below, write a 
describePlaceTemperatures function that takes a list of place-temperature pairs 
(like the testPlaces list), and returns a list of place-descriptions pairs. 
Running your function on testPlaces should give:
  [("London","Cold"),("Madrid","Hot"),("Paris","Warm"),("Helsinki","Freezing")]
-}

testPlaces :: [(String, Int)]
testPlaces = [("London", 12), ("Madrid", 32), ("Paris", 22), ("Helsinki", -3)]

describeTemperature :: Int -> String
describeTemperature temp 
   | temp >= 30   = "Hot"
   | temp >= 15   = "Warm"
   | temp >= 1    = "Cold"
   | otherwise    = "Freezing"
   
describePlaceTemperatures :: [(String, Int)] -> [(String, String)]
describePlaceTemperatures toSort = [(location, describeTemperature temp) | (location, temp) <- toSort]
-- *** Uncomment the line above and add your code here ***


{-
Exercise 3 - 4 marks
--------------------
Using recursion, write a hotter function that takes a temperature and a list 
of place-temperature pairs (like the testPlaces list) and returns a list of 
places from the list that are hotter than the given temperature.
-}

hotter :: Int -> [(String, Int)] -> [String]
hotter capTemp [] = []
hotter capTemp ((location, temp):xs)
    | temp > capTemp = location : hotter capTemp xs
    | otherwise = hotter capTemp xs
-- *** Uncomment the line above and add your code here ***


{-
Exercise 4 - 3 marks
--------------------
The List type definition below represents lists of integers, and the testList 
value is an example of an List whose values are in order. Write an insert 
function that takes an int and a List that is ordered, and inserts the integer 
into the List so that it remains ordered. 
-}

data List = Null | Node Int List
     deriving (Show)

testList :: List
testList = Node 2 (Node 3 (Node 5 (Node 5 (Node 6 Null))))

insert :: Int -> List -> List
insert toInsert Null = Node toInsert Null
insert toInsert (Node currentNode remainingNodes)
    | toInsert < currentNode = Node toInsert (Node currentNode remainingNodes)
    | otherwise = Node currentNode (insert toInsert remainingNodes)
-- *** Uncomment the line above and add your code here ***


{- 
Test function. Use this function to test your solutions. You should uncomment 
all lines relating to the exercises you have attempted, but should not change 
anything else. 

To test the functionality of your code we will only run this function so
make sure that:
  * you uncommented all appropriate lines in the function
  * you comment out any incomplete/non-working solutions
-}

test :: IO () 
test = do
   putStrLn "Exercise 1"
   putStrLn $ "  Pizza - " ++ show (price "Pizza") 
   putStrLn $ "  Pasta - " ++ show (price "Pasta") 
   putStrLn $ "  Salad - " ++ show (price "Salad") 
   putStrLn $ "  Fish - " ++ show (price "Fish") 
   putStrLn "Exercise 2"
   putStrLn $ "  " ++ show (describePlaceTemperatures testPlaces)
   putStrLn "Exercise 3"
   putStrLn $ "  " ++ show (hotter 12 testPlaces)
   putStrLn "Exercise 4"
   putStrLn $ "  Inserting 1 gives - " ++ show (insert 1 testList)
   putStrLn $ "  Inserting 3 gives - " ++ show (insert 3 testList)
   putStrLn $ "  Inserting 4 gives - " ++ show (insert 4 testList)