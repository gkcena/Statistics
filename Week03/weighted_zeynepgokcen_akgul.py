import random
def weighted_srs(data, n, weights, with_replacement = False):
    randomList = random.choices(data, n, weights)
    if weights != None | with_replacement == True:
        print("")
    else:
        random.sample(data, n)
    return randomList
