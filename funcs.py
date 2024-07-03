import numpy as np
import matplotlib as plt




def calculateSignificance(s,b):
    return s/np.sqrt(s + b)




def calculateWeight(num_events, effective_area, lumi = 300):
    return effective_area * lumi / num_events


def applyWeight(data, weight):
    return data * weight;





#### Plotting Functions



