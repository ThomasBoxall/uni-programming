-- Week 9 Placement Diary Problem

import Data.Time
import Text.Printf

type Title = String
type Description = String
type Reviewed = Bool
type AddedDate = Day

data PlacementEntry = PlacementEntry Title Description Reviewed AddedDate
    deriving (Show)

placementEntries :: [PlacementEntry]
placementEntries = 
    [
        PlacementEntry "Learnt about GitHub" "I completed a tutorial on how to use GitHub" True (fromGregorian 2023 03 15),
        PlacementEntry "Met with the clients" "I got to meet with the clients of the project" True (fromGregorian 2023 03 17),
        PlacementEntry "Completed health and safety training" "I just completed the health and safety training" False (fromGregorian 2023 03 21),
        PlacementEntry "First staff meeting" "I attended my first staff meeting" True (fromGregorian 2023 03 23),
        PlacementEntry "Leant about C" "Did some C stuff" False (fromGregorian 2023 03 24)
    ]

placementManager :: IO ()
placementManager = do
    putStrLn = "== PLACEMENT DIARY MANAGER =="
    putStrLn = "   (1) Mark an entry as 'reviewed'"
    putStrLn = "   (2) Update the content of a diary entry"
    putStrLn = "   (3) Add a new diary entry"
    putStrLn = "   (4) Show all diary entries where they are too short"

boolToString :: Bool -> String
boolToString True = "Reviewed"
boolToString False = "Not Reviewed"

renderPlacementEntry :: PlacementEntry -> String
renderPlacementEntry (PlacementEntry title desc rev date) = 
    printf "Title: %-10s \n %-10s \n %-10s, added on %-10s"
    title desc (boolToString rev) (show date)

renderPlacementEntries :: [PlacementEntry] -> String
renderPlacementEntries [] = ""
renderPlacementEntries (placementEntry:rest) = renderPlacementEntry placementEntry ++ "\n" ++ renderPlacementEntries rest

