
# N-Sum Algorithm

## Overview
This repository contains an implementation of the N-sum algorithm. It's designed to find all unique combinations of N numbers that sum to a specific target value.

## Application
The algorithm has various applications, including investment portfolio optimization, computational geometry, and more. [Here's a detailed example of its usage in financial investment](#).

## How to Use
Import the script and call the `n_sum` function with the required parameters.

### Example
```python
from n_sum import n_sum

numbers = [1, 0, -1, 0, -2, 2]
target = 0
n = 4
results = n_sum(numbers, target, n)
print(results)  # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
