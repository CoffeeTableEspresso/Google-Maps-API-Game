import math

BESTDIST = 0
WORSTDIST = math.sqrt(90**2 + 180**2)

# Points are (lat, long)
testCoord1 = (90, -180)
testCoord2 = (0,0)

def findDistance(guessedCoordinate, actualCoordinate):
    xdistance = abs(guessedCoordinate[0] - actualCoordinate[0])
    ydistance = abs(guessedCoordinate[1] - actualCoordinate[1])
    distance = math.sqrt(xdistance**2 + ydistance**2)
    return distance

# Calculated based on a linear scale from 0 to 100, with
# 0 being the worst guess and 100 being the best guess
def getScore(guessedCoordinate, actualCoordinate):
    distance = findDistance(guessedCoordinate, actualCoordinate)
    OUTPUTLOW = 100
    OUTPUTHIGH = 0
    INPUTLOW = BESTDIST
    INPUTHIGH = WORSTDIST
    score = ((distance - INPUTLOW) / (INPUTHIGH - INPUTLOW)) * (OUTPUTHIGH - OUTPUTLOW) + OUTPUTLOW
    return score

score = getScore(testCoord1, testCoord2)
print("Score is %d") % score

# Also later- get user input of where they live
# then determine level of difficulty from that
