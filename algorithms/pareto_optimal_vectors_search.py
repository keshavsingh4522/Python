# Almost all real complex decision-making task is described by more than one criterion. Therefore, the methods of multicriteria
# optimization are important. For a wide range of tasks multicriteria optimization, described by some axioms of
# "reasonable" behavior in the process of choosing from a set of possible solutions X, each set of selected solutions
# Sel X should be contained in a set optimal for Pareto.

# This is an example of vectors that represent multicriterial tasks.
data = [
  [7, 6, 5, 8, 5, 6],
  [4, 8, 4, 4, 5, 3],
  [3, 8, 1, 4, 5, 2],
  [5, 6, 3, 6, 4, 5],
  [1, 4, 8, 6, 3, 6],
  [5, 1, 8, 6, 5, 1],
  [6, 8, 3, 6, 3, 5]
]

# This is an array that represents priority if each criteria.
a = [1, 1, 1, 1, 0.545, 0.583]

# This is a method that searches for the least difference between the each criteria of two vectors.
def get_min_diff(arr1, arr2):
  min_value = 1e10
  len_arr1 = len(arr1)
  len_arr2 = len(arr2)
  if (len_arr1 != len_arr2):
    return min_value
  for i in range(len_arr1):
    diff = arr1[i] - arr2[i]
    if min_value > diff:
      min_value = diff
      return min_value

# This is method performs optimization and find Pareto optimal vectors.
def pareto(arr):
  length = len(arr)
  i = 0

  while i < length:
    for j in range(i + 1, length):
      m = get_min_diff(arr[i], arr[j])
      q = get_min_diff(arr[j], arr[i])
      if m >= 0:
        arr.pop(j)
        i -= 1
        break
      elif q >= 0:
        arr.pop(i)
        i -= 1
        break
    i += 1
    length = len(arr)
  return arr

# result of the Pareto optimization
print(pareto(data), '\n')

# This method performs linear convolution
def linconv(f, a):
  print('Calculation of the linear convolution:')
  res = []
  for i in f:
    sum_value = 0
    criteria_length = len(i)
    for j in range(criteria_length):
      sum_value += i[j] * a[j]
    res.append(sum_value)
  max_index = res.index(max(res))
  print('optimal vector:', f[max_index])
  print('value of the linear convolution for the optimal vector:', res[max_index], '\n')

# This method performs maxmin convolution
def maxmin(f, a):
  print('Calculation of the maxmin convolution:')
  mins = []
  for i in f:
    min_val = 10e10
    criteria_length = len(i)
    for j in range(criteria_length):
      res = i[j] * a[j]
      if res < min_val:
        min_val = res
    mins.append(min_val)
  max_index = mins.index(max(mins))
  print('optimal vector:', f[max_index])
  print('minimal value of the optimal vector:', mins[max_index])
  res_opt = 0
  for i in range(len(f[max_index])):
    res_opt += f[max_index][i] * a[i]
  print('value of the maxmin convolution for the optimal vector:', res_opt, '\n')

# result of the linear convolution
linconv(data, a)

# result of the maxmin convolution
maxmin(data, a) 