def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    exposure = 0.0
    while (stop - start) > 0:
        exposure += f(start) * step
        start += step
    return exposure
