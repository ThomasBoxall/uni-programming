import math

def distanceBetweenPoints(pointOne, pointTwo):
    # params ((x1, y1), (x2, y2))
    return math.sqrt(((pointTwo[0]-pointOne[0])**2) + ((pointTwo[1]-pointOne[1])**2))

print(distanceBetweenPoints((1,2),(4,6)))