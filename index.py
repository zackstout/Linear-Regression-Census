
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

# First step will be figuring out all possible responses and converting them into numbers.

# print(df['Average Household Size'])


for size in df['Average Household Size']:
    sizes.append(size)
for num in df['Total Households']:
    numberHouses.append(num)


# print(sizes)

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

print(b0, b1)

for s in sizes:
    predictedNum = b0 + b1 * s
    diffPredicted = predictedNum - s
    nums2.append(diffPredicted * diffPredicted)

r_squared = sum(nums2)/sum(denoms2)

print(r_squared)


#
#
#
# plt.scatter(sizes, numberHouses, alpha=0.5)
# plt.show()
