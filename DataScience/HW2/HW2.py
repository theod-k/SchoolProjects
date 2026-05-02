import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("housing.csv", delimiter = ",")
df2 = pd.read_csv("kc_house_data.csv", delimiter = ",")

#Getting the data on the types and columns for both csv files
# print(df.head())
# print(df2.head())

# dt = df.dtypes
# print(dt)
# Non numerical column is column 9 (of 9)

# dt2 = df2.dtypes
# print(dt2)
# Non numerical column is 1

set1 = df.iloc[:, 0:8]
# print(set1.head())

set2 = df2.iloc[:, [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
# print(set2.head())

#Heatmap for set1
# plt.subplots(figsize=(10,7))
# sns.heatmap(
#     set1.corr(),
#     vmin=-1, vmax=1, center=0,
#     cmap=sns.diverging_palette(20, 220, n=200),
#     annot=True, annot_kws={'size': 10},
#     square=True
# )
# plt.show()

# Strongly correlated in set1: (aka |correlation| greater than .5)
    # Longitude vs Latitude (cols 0 and 1)

    # Total Rooms vs Total Bedrooms (cols 3 and 4)
    # Total Rooms vs Population (cols 3 and 5)
    # Total Rooms vs Households (cols 3 and 6)

    # Total Bedrooms vs Population (cols 4 and 5)
    # Total Bedrooms vs Households (cols 4 and 6)

    # Population vs Households (cols 5 and 6)
    
#Heatmap for set2
# plt.subplots(figsize=(10,7))
# sns.heatmap(
#     set2.corr(),
#     vmin=-1, vmax=1, center=0,
#     cmap=sns.diverging_palette(20, 220, n=200),
#     annot=True, annot_kws={'size': 3},
#     square=True
# )
# plt.show()

#Strongly Correlated in set2: (aka |correlation| greater than .5)
    # Price vs bathrooms, sqft_living, grade, sqft_above, sqft_living15
    # Bedrooms vs bathrooms, sqft_living
    # Bathrooms vs sqft_living, floors, grade, sqft_above, yr_built, sqft_living15
    # Sqft_living vs grade, sqft_above, sqft_living15
    # Sqft_lot vs sqft_lot15
    # Floors vs sqft_above
    # Grade vs sqft_above, sqft_living15
    # Sqft_above vs sqft_living15
    # Zipcode vs long

#Numbered skipping 1
#0-10: id0, price2, bedrooms3, bathrooms4, sqft_living5, sqft_lot6, floors7, waterfront8, view9, condition10, grade11
#11-19: 12sqft_above, 13sqft_basement, 14yr_built, 15yr_renovated, 16zipcode, 17lat, 18long, 19sqft_living15, 20sqft_lot15

#Arrays for Slope, Intercept, and Error
slopeArr = []
intArr = []
errArr = []

#Graphing all strong correlations in in set1

# # Longitude vs Latitude (cols 0 and 1)
# # Linear
# param1 = df.iloc[:, 0]
# param2 = df.iloc[:, 1]
# plt.plot(param1, param2, 'o', label='original data')

# result = stats.linregress(param1, param2)

# slopeArr.append(result.slope)
# intArr.append(result.intercept)
# errArr.append(result.stderr)

# plt.plot(param1, result.intercept + result.slope*param1, 'r', label='fitted line')
# plt.show()

# # Total Rooms vs Total Bedrooms (cols 3 and 4)
# # Linear
# param3 = df.iloc[:, 3]
# param4 = df.iloc[:, 4]
# plt.plot(param3, param4, 'o', label='original data')
# result = stats.linregress(param3, param4)

# slopeArr.append(result.slope)
# intArr.append(result.intercept)
# errArr.append(result.stderr)

# plt.plot(param3, result.intercept + result.slope*param3, 'r', label='fitted line')
# plt.show()

# # Total Rooms vs Population (cols 3 and 5)
# # Linear
# param5 = df.iloc[:, 3]
# param6 = df.iloc[:, 5]
# plt.plot(param5, param6, 'o', label='original data')
# result = stats.linregress(param5, param6)

# slopeArr.append(result.slope)
# intArr.append(result.intercept)
# errArr.append(result.stderr)

# plt.plot(param5, result.intercept + result.slope*param5, 'r', label='fitted line')
# plt.show()

# # Total Rooms vs Households (cols 3 and 6)
# # Linear
# param7 = df.iloc[:, 3]
# param8 = df.iloc[:, 6]
# plt.plot(param7, param8, 'o', label='original data')
# result = stats.linregress(param7, param8)

# slopeArr.append(result.slope)
# intArr.append(result.intercept)
# errArr.append(result.stderr)

# plt.plot(param7, result.intercept + result.slope*param7, 'r', label='fitted line')
# plt.show()

# # Total Bedrooms vs Population (cols 4 and 5)
# # Linear
# param9 = df.iloc[:, 4]
# param10 = df.iloc[:, 5]
# plt.plot(param9, param10, 'o', label='original data')
# result = stats.linregress(param9, param10)

# slopeArr.append(result.slope)
# intArr.append(result.intercept)
# errArr.append(result.stderr)

# plt.plot(param9, result.intercept + result.slope*param9, 'r', label='fitted line')
# plt.show()

# # Total Bedrooms vs Households (cols 4 and 6)
# # Linear
# param11 = df.iloc[:, 4]
# param12 = df.iloc[:, 6]
# plt.plot(param11, param12, 'o', label='original data')
# result = stats.linregress(param11, param12)

# slopeArr.append(result.slope)
# intArr.append(result.intercept)
# errArr.append(result.stderr)

# plt.plot(param11, result.intercept + result.slope*param11, 'r', label='fitted line')
# plt.show()

# # Population vs Households (cols 5 and 6)
# # Linear
# param13 = df.iloc[:, 5]
# param14 = df.iloc[:, 6]
# plt.plot(param13, param14, 'o', label='original data')
# result = stats.linregress(param13, param14)

# slopeArr.append(result.slope)
# intArr.append(result.intercept)
# errArr.append(result.stderr)

# plt.plot(param13, result.intercept + result.slope*param13, 'r', label='fitted line')
# plt.show()

# print(slopeArr)
# print(intArr)
# print(errArr)

# slopeArr.clear()
# intArr.clear()
# errArr.clear()

#Graphing all strong correlations in set2:

#Price vs bathrooms
# Non-Linear
parame1 = df2.iloc[:, 2]
parame2 = df2.iloc[:, 4]
plt.plot(parame1, parame2, 'o', label='original data')
plt.show()

#Price vs sqft_living
# Linear
parame3 = df2.iloc[:, 2]
parame4 = df2.iloc[:, 5]
plt.plot(parame3, parame4, 'o', label='original data')
result = stats.linregress(parame3, parame4)

slopeArr.append(result.slope)
intArr.append(result.intercept)
errArr.append(result.stderr)

plt.plot(parame3, result.intercept + result.slope*parame3, 'r', label='fitted line')
plt.show()

#Price vs grade
# Non-Linear
parame5 = df2.iloc[:, 2]
parame6 = df2.iloc[:, 11]
plt.plot(parame5, parame6, 'o', label='original data')
plt.show()

#Price vs sqft_above
# Linear
parame7 = df2.iloc[:, 2]
parame8 = df2.iloc[:, 12]
plt.plot(parame7, parame8, 'o', label='original data')
result = stats.linregress(parame7, parame8)

slopeArr.append(result.slope)
intArr.append(result.intercept)
errArr.append(result.stderr)

plt.plot(parame7, result.intercept + result.slope*parame7, 'r', label='fitted line')
plt.show()

#Price vs sqft_living15
# Linear
parame9 = df2.iloc[:, 2]
parame10 = df2.iloc[:, 19]
plt.plot(parame9, parame10, 'o', label='original data')
result = stats.linregress(parame9, parame10)

slopeArr.append(result.slope)
intArr.append(result.intercept)
errArr.append(result.stderr)

plt.plot(parame9, result.intercept + result.slope*parame9, 'r', label='fitted line')
plt.show()

# Bedrooms vs bathrooms
# Non-Linear
parame11 = df2.iloc[:, 3]
parame12 = df2.iloc[:, 4]
plt.plot(parame11, parame12, 'o', label='original data')
plt.show()

# Bedrooms vs sqft_living
# Non-Linear
parame13 = df2.iloc[:, 3]
parame14 = df2.iloc[:, 5]
plt.plot(parame13, parame14, 'o', label='original data')
plt.show()

# Bathrooms vs sqft_living
# Linear
parame15 = df2.iloc[:, 4]
parame16 = df2.iloc[:, 5]
plt.plot(parame15, parame16, 'o', label='original data')
result = stats.linregress(parame15, parame16)

slopeArr.append(result.slope)
intArr.append(result.intercept)
errArr.append(result.stderr)

plt.plot(parame15, result.intercept + result.slope*parame15, 'r', label='fitted line')
plt.show()

# Bathrooms vs floors
# Non-Linear
parame17 = df2.iloc[:, 4]
parame18 = df2.iloc[:, 7]
plt.plot(parame17, parame18, 'o', label='original data')
plt.show()

# Bathrooms vs grade
# Non-Linear
parame19 = df2.iloc[:, 4]
parame20 = df2.iloc[:, 11]
plt.plot(parame19, parame20, 'o', label='original data')
plt.show()

# Bathrooms vs sqft_above
# Linear
parame21 = df2.iloc[:, 4]
parame22 = df2.iloc[:, 12]
plt.plot(parame21, parame22, 'o', label='original data')
result = stats.linregress(parame21, parame22)

slopeArr.append(result.slope)
intArr.append(result.intercept)
errArr.append(result.stderr)

plt.plot(parame21, result.intercept + result.slope*parame21, 'r', label='fitted line')
plt.show()

# Bathrooms vs yr_built
# Non-Linear
parame23 = df2.iloc[:, 4]
parame24 = df2.iloc[:, 14]
plt.plot(parame23, parame24, 'o', label='original data')
plt.show()

# Bathrooms vs sqft_living15
# Non-Linear
parame25 = df2.iloc[:, 4]
parame26 = df2.iloc[:, 19]
plt.plot(parame25, parame26, 'o', label='original data')
plt.show()

# Sqft_living vs grade
# Non-Linear
parame27 = df2.iloc[:, 5]
parame28 = df2.iloc[:, 11]
plt.plot(parame27, parame28, 'o', label='original data')
plt.show()

# Sqft_living vs sqft_above
# Linear
parame29 = df2.iloc[:, 5]
parame30 = df2.iloc[:, 12]
plt.plot(parame29, parame30, 'o', label='original data')
result = stats.linregress(parame29, parame30)

slopeArr.append(result.slope)
intArr.append(result.intercept)
errArr.append(result.stderr)

plt.plot(parame29, result.intercept + result.slope*parame29, 'r', label='fitted line')
plt.show()

# Sqft_living vs sqft_living15
# Linear
parame31 = df2.iloc[:, 5]
parame32 = df2.iloc[:, 19]
plt.plot(parame31, parame32, 'o', label='original data')
result = stats.linregress(parame31, parame32)

slopeArr.append(result.slope)
intArr.append(result.intercept)
errArr.append(result.stderr)

plt.plot(parame31, result.intercept + result.slope*parame31, 'r', label='fitted line')
plt.show()

# Sqft_lot vs sqft_lot15
# Linear
parame33 = df2.iloc[:, 6]
parame34 = df2.iloc[:, 20]
plt.plot(parame33, parame34, 'o', label='original data')
result = stats.linregress(parame33, parame34)

slopeArr.append(result.slope)
intArr.append(result.intercept)
errArr.append(result.stderr)

plt.plot(parame33, result.intercept + result.slope*parame33, 'r', label='fitted line')
plt.show()

# Floors vs sqft_above
# Non-Linear
parame35 = df2.iloc[:, 7]
parame36 = df2.iloc[:, 12]
plt.plot(parame35, parame36, 'o', label='original data')
plt.show()

# Grade vs sqft_above
# Linear
parame37 = df2.iloc[:, 11]
parame38 = df2.iloc[:, 12]
plt.plot(parame37, parame38, 'o', label='original data')
result = stats.linregress(parame37, parame38)

slopeArr.append(result.slope)
intArr.append(result.intercept)
errArr.append(result.stderr)

plt.plot(parame37, result.intercept + result.slope*parame37, 'r', label='fitted line')
plt.show()

# Grade vs sqft_living15
# Linear
parame39 = df2.iloc[:, 11]
parame40 = df2.iloc[:, 19]
plt.plot(parame39, parame40, 'o', label='original data')
result = stats.linregress(parame39, parame40)

slopeArr.append(result.slope)
intArr.append(result.intercept)
errArr.append(result.stderr)

plt.plot(parame39, result.intercept + result.slope*parame39, 'r', label='fitted line')
plt.show()

# Sqft_above vs sqft_living15
# Linear
parame41 = df2.iloc[:, 12]
parame42 = df2.iloc[:, 19]
plt.plot(parame41, parame42, 'o', label='original data')
result = stats.linregress(parame41, parame42)

slopeArr.append(result.slope)
intArr.append(result.intercept)
errArr.append(result.stderr)

plt.plot(parame41, result.intercept + result.slope*parame41, 'r', label='fitted line')
plt.show()

# Zipcode vs long
# Linear
parame43 = df2.iloc[:, 16]
parame44 = df2.iloc[:, 18]
plt.plot(parame43, parame44, 'o', label='original data')
result = stats.linregress(parame43, parame44)

slopeArr.append(result.slope)
intArr.append(result.intercept)
errArr.append(result.stderr)

plt.plot(parame43, result.intercept + result.slope*parame43, 'r', label='fitted line')
plt.show()

print("\n\n")
print(slopeArr)
print(intArr)
print(errArr)