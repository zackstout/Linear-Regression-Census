
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

# print(numerators)
b1 = sum(numerators)/sum(denominators)

b0 = avgNum - b1 * avgSize

print(b0, b1)








plt.scatter(sizes, numberHouses, alpha=0.5)
plt.show()
