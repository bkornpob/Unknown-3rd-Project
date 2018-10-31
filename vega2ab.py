import numpy as np

def vega2AB(band, vegamag):
    """Return numpy.array of ABmagnitude
    band = numpy.array of bands
    vegamag = numpy.array of magnitude (Vega)
    mAB - mVega = constant
    Blanton, and Roweis, 2006, ApJ 133 734
    Breeveld et al., 2011, arXiv:1102.4717"""
    
    vega2ab = {'UVW2': 1.73,
              'UVM2': 1.69,
              'UVW1': 1.51,
              'U': 0.79,
              'B': -0.09,
              'G': -0.08,
              'V': 0.02,
              'R': 0.21,
              'I': 0.45,
              'J': 0.91,
              'H': 1.39,
              'KS': 1.85}
    
    constant = []
    for i in band:
        constant.append(vega2ab[i])
       
    return vegamag + np.array(constant)

# Example
# band = np.array(['UVW2','UVM2','U','J'])
# vegamag = np.array([0,0,0,0])
# print(vega2AB(band,vegamag))
# >>> [1.73 1.69 0.79 0.91]

