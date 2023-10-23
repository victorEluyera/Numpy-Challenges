import numpy as np

dailywts = 185 - np.arange(5*7)/5

'''With your high school reunion fast approaching, you decide to get in shape and lose some weight . You record your weight every day for five weeks starting on a Monday.

import numpy as np

dailywts = 185 - np.arange(5*7)/5

print(dailywts)
# [185.  184.8 184.6 184.4 184.2 184.  183.8 183.6 183.4 183.2 183.  182.8
#  182.6 182.4 182.2 182.  181.8 181.6 181.4 181.2 181.  180.8 180.6 180.4
#  180.2 180.  179.8 179.6 179.4 179.2 179.  178.8 178.6 178.4 178.2]
Given these daily weights, build an array with your average weight per weekend1.'''

first_week_saturday=dailywts[5]
first_week_sunday=dailywts[6]
# print(first_week_saturday,first_week_sunday)

all_saturdays=dailywts[5::7]
all_sundays=dailywts[6::7]

# print(all_sundays,all_saturdays)

avg_weight_per_weekend=np.add(all_sundays,all_saturdays)/2

# print(avg_weight_per_weekend)

arr=np.array([[1,2,3,4,5,6,7],[8,9,10,20,19,13,14],[8,9,10,11,12,13,14],[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

arr[0,4]=50

print(arr[:3,1:])