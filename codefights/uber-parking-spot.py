def validateSpot(parkingLot, luckySpot):
    for i in xrange(luckySpot[0], luckySpot[2]+1):
        for j in xrange(luckySpot[1], luckySpot[3]+1):
            if parkingLot[i][j] != 0:
                return False
    return True

def getCarOrientation(carDimensions, luckySpot):
    if carDimensions[0] == carDimensions[1]:
        return 'SQUARE'
    if carDimensions[0] == luckySpot[2] - luckySpot[0]+1:
        return 'VERTICAL'
    return 'HORIZONTAL'

def canArriveFrom(parkingLot, luckySpot, direction):
    assert direction in ('LEFT', 'RIGHT', 'TOP', 'BOTTOM')
    if direction == 'LEFT':
        for i in xrange(luckySpot[0], luckySpot[2]+1):
            for j in xrange(0, luckySpot[1]):
                if parkingLot[i][j] != 0:
                    return False
        return True
    elif direction == 'RIGHT':
        for i in xrange(luckySpot[0], luckySpot[2]+1):
            for j in xrange(luckySpot[3]+1, len(parkingLot[1])):
                if parkingLot[i][j] != 0:
                    return False
        return True
    elif direction == 'TOP':
        for i in xrange(0, luckySpot[0]):
            for j in xrange(luckySpot[1], luckySpot[3]+1):
                if parkingLot[i][j] != 0:
                    return False
        return True
    elif direction == 'BOTTOM':
        for i in xrange(luckySpot[2]+1, len(parkingLot)):
            for j in xrange(luckySpot[1], luckySpot[3]+1):
                if parkingLot[i][j] != 0:
                    return False
        return True

def parkingSpot(carDimensions, parkingLot, luckySpot):
    if not validateSpot(parkingLot, luckySpot):
        return False
    orientation = getCarOrientation(carDimensions, luckySpot)
    if orientation == 'SQUARE':
        return (canArriveFrom(parkingLot, luckySpot, 'TOP')
               or canArriveFrom(parkingLot, luckySpot, 'BOTTOM')
               or canArriveFrom(parkingLot, luckySpot, 'RIGHT')
               or canArriveFrom(parkingLot, luckySpot, 'LEFT'))
    elif orientation == 'HORIZONTAL':
        return (canArriveFrom(parkingLot, luckySpot, 'RIGHT')
               or canArriveFrom(parkingLot, luckySpot, 'LEFT'))
    return (canArriveFrom(parkingLot, luckySpot, 'TOP')
               or canArriveFrom(parkingLot, luckySpot, 'BOTTOM'))
