
import pandas as pd
# import matplotlib
from pandas.plotting import scatter_matrix

import matplotlib.pyplot as plt
from matplotlib import style
# nice!
# import this

style.use('ggplot')

# Wow thanks again SO:
df = pd.read_csv('census_2010.csv', encoding = "ISO-8859-1")

sizes = []
numberHouses = []

sizeDiffs = []
numDiffs = []

numerators = []
denominators = []

b1 = 0
b2 = 0

nums2 = []
denoms2 = []
currentX = ''
currentY = ''

# Array to hold all totals: {x: '', y: '', correlation: ''}
totals = []

options = ['Zip Code', 'Total Population', 'Median Age', 'Total Males', 'Total Females', 'Total Households', 'Average Household Size']

# I guess we can just change these column names, everything else should be fine:
for size in df['Total Population']:
    sizes.append(size)
for num in df['Average Household Size']:
    numberHouses.append(num)


### !!!! Ok it's not working -- when we run the above it does not return same result as we see in our totals array.


def getCorrelation():

    # Amazing, you *do* need this -- why not for arrays?
    global b1
    global b0
    # Well it's pretty ugly code, but here's linear regression (I think):
    avgSize = sum(sizes)/len(sizes)
    avgNum = sum(numberHouses)/len(numberHouses)

    # Why is this giving different answer than the below three loops???
    # for i in range(0, len(sizes)):
    #     numerators.append((sizes[i] - avgSize) * (numberHouses[i] - avgNum))
    #     denominators.append((sizes[i] - avgSize) * (sizes[i] - avgSize))
    #     denoms2.append((numberHouses[i] - avgNum) * (numberHouses[i] - avgNum))

    for x in sizes:
        sizeDiffs.append(x - avgSize)

    for y in numberHouses:
        numDiffs.append(y - avgNum)

    for i in range(0, len(sizes)):
        numerators.append(sizeDiffs[i] * numDiffs[i])
        denominators.append(sizeDiffs[i] * sizeDiffs[i])
        # add this for r^2:
        denoms2.append(numDiffs[i] * numDiffs[i])

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

    return r_squared


# Interesting: turns out there's *no hoisting* in Python:
getCorrelation()

# for i, opt in enumerate(options):
#     # print(i, opt)
#     # Must clear out, yeah?:
#     sizes = []
#     numberHouses = []
#     sizeDiffs = []
#     numDiffs = []
#     numerators = []
#     denominators = []
#     nums2 = []
#     denoms2 = []
#
#     for j in range(i+1, len(options)):
#         # print(j)
#         for x in df[opt]:
#             sizes.append(x)
#             # put j instead of i+1:
#         for y in df[options[j]]:
#             numberHouses.append(y)
#
#         r_squared = getCorrelation()
#         total = {
#             'r_squared': r_squared,
#             'X': opt,
#             # needs to be j:
#             'Y': options[j]
#         }
#         totals.append(total)


# print(totals)

# for t in totals:
#     print(t)
#     print('\n')


# --Visualize our data--:
# box/whisker -- Wow this is amazing:
# df.plot(kind='box', subplots=True, layout=(3, 3), sharex=False, sharey=False)
# plt.show()

# histograms -- Wow this is also nuts:
# df.hist()
# plt.show()

# scatter plot matrix -- WOW --:
# scatter_matrix(df)
# plt.show()

# # To get two plots overlaid:
regression_line = [(b1*x)+b0 for x in sizes]
plt.scatter(sizes, numberHouses, alpha=0.5)
plt.plot(sizes, regression_line)
plt.show()
