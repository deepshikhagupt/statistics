from math import sqrt

def desc_stats(X):

    min_value = min(X)
    max_value = max(X)
    count = len(X)
    mean = sum(X)/count
    tot = [(element-mean)**2 for element in X]
    variance = sum(tot)/count
    stdv = sqrt(variance)

    # TODO: calculate the descriptive stats for the variable X.
    # Update the values of the appropriate variables.



    return stdv

desc_stats([4, 1, 10, 20, 19, 0, 2, 15, 16, 11])
