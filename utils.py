import numpy as np

def uniformize_data(data):
    """
    Transforms data to an approximately uniform distribution on [0, 1] 
    with a median of 0.5 using rank transformation (Empirical CDF).
    """
    x = np.asarray(data)
    n = len(x)
    
    if n == 0:
        return np.array([])
    
    # Get the ranks (0 to n-1) of the sorted data
    ranks = x.argsort().argsort()
    
    # Scale the ranks to the range [0, 1]
    return (ranks + 0.5) / n