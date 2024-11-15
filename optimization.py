################################################################################
# Problem Setup: You want the perfect bread
# What influences this?
#  - how long do you toast it?
#  - how long after toasting do you eat the bread?
#  - Do you have power? And how much?
#  - Which toaster do you use?
################################################################################

import math

################################################################################
# the function you are supposed to optimize.
# It has the following input:
#  toast_duration: duration of toasting in seconds. It is supposed to be an integer between 1 and 100
#  wait_duration: duration of waiting after toasting in seconds. It's supposed to be an integer between 1 and 100
#  toaster: the number of the toaster you want to use. It's supposed to be an integer, between 1 and 10.
#  power: how much power the toaster has (it's supposed to be a floating point number between 0 and 2)
################################################################################
def utility(toast_duration, wait_duration, power=1.0, toaster=1):
    # handle input errors
    if (type(toast_duration) is not int) and not (1 <= toast_duration <= 100):
        raise ValueError("toast_duration is not an integer")
    if (type(wait_duration) is not int) and not (1 <= wait_duration <= 100):
        raise ValueError("wait_duration is not an integer")
    if (type(toaster) is not int) and not (1 <= toaster <= 10):
        raise ValueError("toaster is not an integer or is not in a valid range")
    if (type(power) is not float) and not (0.0 <= power <= 2.0):
        raise ValueError("power is not a float or not in the valid range")

    # get toaster specific configuration
    hpt = [10, 8, 15, 7, 9, 2, 9, 19, 92, 32][toaster - 1]
    hpw = [1, 4, 19, 3, 20, 3, 1, 4, 1, 62][toaster - 1]
    toaster_utility = [1, 0.9, 0.7, 1.3, 0.3, 0.8, 0.5, 0.8, 3, 0.2][toaster - 1]

    # calculate values
    toast_utility = -0.1 * (toast_duration - hpt) ** 2 + 1
    wait_utility = -0.01 * (wait_duration - hpw) ** 2 + 1
    overall_utility = (toast_utility + wait_utility) * toaster_utility

    # apply modifier based on electricity
    power_factor = math.sin(10 * power + math.pi / 2 - 10) + power * 0.2
    overall_utility *= power_factor

    return overall_utility


################################################################################
# Writing this function is your homework.
# The function should return the tuple of parameters that optmizes the function.
#
# You can implement it in multiple difficulty levels:
# easy:
#     - implement it with only two parameters: toast_duration and wait_duration
#     - e.g., utility(2,3)
#     - Implement the function by testing all possible values for these variables.
#     - (This state space has only 10000 values, so it shouldn't take too long)
#
# medium:
#    - same as easy, but implement hill climbing
#    - see pseudo code
# hard:
#    - also use the parameter power
#    - e.g., utility(2,3,1.2)
#    - this introduces the following complications:
#        - multiple maxima
#        - a continuous parameter
#    - implement gradient ascent
# very hard:
#    - Same as hard, but use repeated search to find all maxima.
#    - repeated search:
#        - apply gradient descent from different starting points.
#    - I think there are 5 maxima. But I'm not sure :-P
# prepare to cry:
#    - find the optimum for all four parameters
#    - define your own algorithm!
def find_maximum():
    # TODO: Implement an optimization algorithm. Tip: (1,1) is not the optimum!
    result_set = []

    trials = 0
    for toast_duration in range(0, 100):
        for wait_duration in range(0, 100):
            result_set.append([toast_duration, wait_duration])
            trials += 1

    return result_set


# # use the function and see what it thinks the optimum is
# optimum = find_maximum()
# print(
#     "Optimum:",
#     optimum,
# )
# print("value:", utility(*optimum))
