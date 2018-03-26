
import pandas as pd

# Wow thanks again SO:
df = pd.read_csv('census_2010.csv', encoding = "ISO-8859-1")

print(df.head(20))

# First step will be figuring out all possible responses and converting them into numbers.
