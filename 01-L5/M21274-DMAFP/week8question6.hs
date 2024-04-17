-- Week 8: Question 6

addWord :: String -> [String] -> [String]
addWord new list = (list ++ [new])

wordsToString :: [String] -> String
wordsToString (x:xs)
    | xs == [""] = ""
    | otherwise = x ++ "\n" ++ wordsToString xs