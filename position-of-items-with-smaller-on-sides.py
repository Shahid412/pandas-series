# Pandas program to find the positions of the values neighboured by smaller values on both sides in a given series.
import pandas as pd
import numpy as np
nums = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
print("Original series:")
print(nums)
print("\nValues surrounded by smaller values on both sides:")
temp = np.diff(np.sign(np.diff(nums)))
result = np.where(temp == -2)[0] + 1
print(result)
