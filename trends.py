def squareTrends (growthPercentages):
    if not isinstance(growthPercentages,list):
        return "growthPercentages must be an array of ints."
    
    if len(growthPercentages) == 0:
        return growthPercentages
    
    if not isinstance(growthPercentages[0],int):
        return "growthPercentages must be an array of ints."
    
    for i in range(len(growthPercentages)):
        growthPercentages[i] = growthPercentages[i] ** 2
    growthPercentages.sort()
    return growthPercentages