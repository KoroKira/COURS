# Exo 1
arr = [25, 11, 7, 75, 56]

max = arr[0]

for i in range (0, len(arr)):
    if arr[i] > max:
        max = arr[i]
        
print("Maximum element in the array is:", max)
# This code finds the maximum element in an array of integers.

# Exo 2
arr = [1, 2, 3, 4, 5]
sum = 0

for i in range (0, len(arr)):
    sum += arr[i]
    
print("Sum of all elements in the array is:", sum)
# This code calculates the sum of all elements in an array of integers.

# Exo 3
arr = [1, 2, 3, 4, 2, 7, 8, 8, 3]

print("Duplicate elements in given array:")
for i in range (0, len(arr)):
    for j in range (i + 1, len(arr)):
        if arr[i] == arr[j]:
            print(arr[j])
            
# This code finds duplicate elements in an array of integers.


# Exo 4
arr = [5, 2, 8, 7, 1]
temp = 0

print("Array before sorting:")
for i in range (0, len(arr)):
    print(arr[i], end=" ")
    
# Sort the array in ascending order
for i in range (0, len(arr)):
    for j in range (i + 1, len(arr)):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print()
print("Array after sorting:")
for i in range (0, len(arr)):
    print(arr[i], end=" ")

# This code sorts an array of integers in ascending order using the bubble sort algorithm.


# Exo 5

arr1 = [1, 2, 3, 4, 5]
arr2 = [None] * len(arr1)

# Copy elements of arr1 to arr2
for i in range (0, len(arr1)):
    arr2[i] = arr1[i]

print("Elements of arr1:")
for i in range (0, len(arr1)):
    print(arr1[i], end=" ")
    
print()

print("Elements of arr2:")
for i in range (0, len(arr2)):
    print(arr2[i], end=" ")
    
# This code copies elements from one array to another array.
# alternate & more optimized code

arr1 = [1, 2, 3, 4, 5]
arr2 = arr1.copy()
print("Elements of arr2:")
for i in range (0, len(arr2)):
    print(arr2[i], end=" ")
# This code copies elements from one array to another using the copy() method.


# Exo 6
# This program calculate the addition of 2 matrices

X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[10, 11, 12],
     [13, 14, 15],
     [16, 17, 18]]

Result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        Result[i][j] = X[i][j] + Y[i][j]

for r in Result:
    print(r)
# This code calculates the addition of two matrices and prints the result.


# Exo 7
# This program calculate the multiplication of 2 matrices

A = [[5, 4, 3],
     [2, 4, 6],
     [4, 7, 9]]

B = [[3, 2, 4],
     [4, 3, 6],
     [2, 7, 5]]

multiResult = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]

# Using nested for loops to iterate through rows and columns
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            multiResult[i][j] += A[i][k] * B[k][j]
            
print("Multiplication of two matrices:")
for r in multiResult:
    print(r)