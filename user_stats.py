"""

This example illustrates basic analytics
using just the built-in statistics module.

VS Code Menu / View / Command Palette / Python Interpretor
Must be 3.10 or greater to get the correlation and linear regression.

To update, try:
conda update pythnon -y
conda --version

Uses only Python Standard Library module:

- statistics - for basic descriptive and a bit of predictive stats

"""

import statistics

# define a variable with some univariant data 
# (one varabile, many readings)
scores = [
    105,
    129,
    87,
    86,
    111,
    111,
    89,
    81,
    108,
    92,
    110,
    100,
    75,
    105,
    103,
    109,
    76,
    119,
    99,
    91,
    103,
    129,
    106,
    101,
    84,
    111,
    74,
    87,
    86,
    103,
    103,
    106,
    86,
    111,
    75,
    87,
    102,
    121,
    111,
    88,
    89,
    101,
    106,
    95,
    103,
    107,
    101,
    81,
    109,
    104,
]

# univariant time series data (one varabile over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
x_times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_temps = [2, 5, 8, 20, 21, 23, 24, 27, 30, 31, 31,32]


import statistics

# How long to cook pasta 
print('Courtney Pigford 1/21/23:')

print('How long cooking pasta')

scores = [
    8,
    9,
    10,
    11,
    12,
    3,
    4,
    5,
    13,
    14,
    15,
    12, 
    12, 
    12, 
    12, 

]

X = statistics.mean(scores)
y = statistics.mode(scores)
z = statistics.median(scores)
a = (statistics.stdev(scores))
b = (statistics.variance(scores))

print('the average cooking time is: ', X)
print('the most common time to cook pasta is: ', y)
print('the best cooking time for all pasta is: ', z)
print('the variance of cooking times is:  ', b)
print('Standard Deviation of the cooking times is: ', a)



