
# Next step:
# Automate it to check correlations for each of its (options.len)*(options.len - 1)/2 possibilities.
# The /2 because it's perfecly symmetric between x and y.


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

# Wow thanks again SO:
df = pd.read_csv('census_2010.csv', encoding = "ISO-8859-1")

sizes = []
numberHouses = []

sizeDiffs = []
numDiffs = []

numerators = []
denominators = []

nums2 = []
denoms2 = []
# print(df.head(20))

# Array to hold all totals: {x: '', y: '', correlation: ''}
totals = []


# First step will be figuring out all possible responses and converting them into numbers.

# print(df['Average Household Size'])

options = ['Zip Code', 'Total Population', 'Median Age', 'Total Males', 'Total Females', 'Total Households', 'Average Household Size']

# Yep, total males vs total females is 0.98. This must be correct.


# I guess we can just change these column names, everything else should be fine:
# for size in df['Total Males']:
#     sizes.append(size)
# for num in df['Zip Code']:
#     numberHouses.append(num)




# print(sizes)
def getCorrelation():

    # Well it's pretty ugly code, but here's linear regression (I think):
    avgSize = sum(sizes)/len(sizes)
    avgNum = sum(numberHouses)/len(numberHouses)

    for x in sizes:
        sizeDiffs.append(x - avgSize)

    for y in numberHouses:
        numDiffs.append(y - avgNum)

    for i in range(0, len(sizes)):
        numerators.append(sizeDiffs[i] * numDiffs[i])
        denominators.append(sizeDiffs[i] * sizeDiffs[i])
        # add this for r^2:
        denoms2.append(numDiffs[i] * numDiffs[i])

    # print(numerators)
    b1 = sum(numerators)/sum(denominators)

    b0 = avgNum - b1 * avgSize

    # Ok, these seem to be the correct values:
    # print(b0, b1)

    for s in sizes:
        predictedNum = b0 + b1 * s
        # print(predictedNum)... OOH it's not minus s!
        diffPredicted = predictedNum - avgNum
        nums2.append(diffPredicted * diffPredicted)

    r_squared = sum(nums2)/sum(denoms2)

    print("CORRELATION: ", r_squared)


# Interesting: turns out there's *no hoisting* in Python:
# getCorrelation()

for i, opt in enumerate(options):
    print(i, opt)
    # Must clear out, yeah?:
    sizes = []
    numberHouses = []
    sizeDiffs = []
    numDiffs = []
    numerators = []
    denominators = []
    nums2 = []
    denoms2 = []

    for j in range(i+1, len(options)):
        for x in df[opt]:
            sizes.append(x)
        for y in df[options[i+1]]:
            numberHouses.append(y)
        getCorrelation()



# plt.scatter(sizes, numberHouses, alpha=0.5)
# plt.show()
