import numpy as np
import matplotlib as plt




def calculateSignificance(numSig,numBkg):
    return numSig/np.sqrt(numSig + numBkg)


def calculateWeight(num_events, effective_area, lumi):
    return effective_area * lumi / num_events


def getWeightAsArray(weight, numElems):
    return np.full(numElems, weight)

def applyWeight(data, weight):
    return data * weight;





#### Plotting Functions



