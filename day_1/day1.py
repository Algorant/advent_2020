from itertools import combinations

import pandas as pd
import numpy as np



## Part 1

# take digits and make a list
inputs = list(pd.read_csv("input.txt", header=None, names=["inputs"])["inputs"])

# iterate through list
combos = list(combinations(inputs, 2))

# find two numbers that sum to answer
solutions = [c for c in combos if sum(c) == 2020]
print(solutions)

# return result

# multiply them together
answer = np.prod(solutions)
print(answer)

## Part 2

# iterate for 3 answers

combos3 = list(combinations(inputs, 3))
solutions3 = [c for c in combos3 if sum(c) == 2020]
print(solutions3)
answer3 = np.prod(solutions3)
print(answer3)
