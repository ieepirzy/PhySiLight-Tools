# Decided to make a quick function to get the length of the digits part of a measurement in order to speed up error calculations for results from certain instruments.

def getFracLength(measurement):
    s = string(measurement)
    if '.' in s:
        frac_part = s.split('.')[-1]
    return len(frac_part)

# I used this in order to programmatically calculate measurement errors for devices which report their errors like:
# Accuracy: ± (0.5 % rdg + 1 dgt)
