# -*- coding: utf-8 -*-
"""Lab_1_Final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X_UV2XBholI6sxIsd3rttUD7XQn0NBmb

## Questions to be done during the lab:

**Questions 1.** 
Write a function name 'avg', which take an array of number and calculate the average
"""

def  avg(marks):
  average = sum (marks) / len (marks)

  return average

mark2 = ([55,88,78,90,79])  
avg (marks = mark2)

# Only run this cell to check your answer. If it is true then no error will be raised
assert(avg(mark2) == np.mean(mark2))

"""**Questions 2**.
Write a function name 'areaCricle', which take radius as a argument and calculate the area. 


"""

from math import pi # Use pi value from math package
def areaCricle(radius):
  
    area=  pi* (radius**2)

    return area

areaCricle(10)

# Only run this cell to check your answer. If it is true then no error will be raised
assert(round(areaCricle(10),2) == 314.16)

"""**Question 3.**
Write a function that takes a list of items and returns a new list with the order of items reversed, without using any inbuilt Python features that will do this for you (e.g. .reverse() or reversed(…)). As specified in the instructions, your function must not modify the contents of the original list.
"""

def reversed_list(in_list):
  old_list = in_list
  new_list = []
  while old_list:
    temp = old_list[len(old_list)-1]
    new_list.append(temp)
    old_list.remove(temp)
  
  return (new_list)


my_list = [3, 1, 0, 9, 4]
reversed_list(my_list)

# Only run this cell to check your answer. If it is true then no error will be raised
assert(reversed_list([1, 2]) == [2, 1])

"""**Question 4.** 

*Read carefully: *Write a function to perform a Bubble Sort on a list of numbers. 

Bubble sort is a sorting algorithm and works by iterating over the list, comparing adjacent items, and swapping them if they are out of order.

Notice that after the first pass of a bubble sort, the biggest item is always moved to the end of the list. This means the next iteration does not need to check the final position of the list.

In addition, you can keep track of how many items were swapped on each iteration. If this count is zero on any iteration, then the list must be fully sorted, in which case the algorithm can stop early.

Hint: To understand Bubble Sort Algorithm, please [Watch](https://www.youtube.com/watch?v=xli_FI7CuzA)
"""

def bubble_sort(in_list):
    n = len(in_list)
    for x in range(n - 1):
        for y in range(0, n - x - 1):
            if in_list[y] > in_list[y + 1]:
                temp = in_list[y+1]
                in_list[y+1] = in_list[y]
                in_list[y] = temp
    return in_list


my_array = [64, 34, 25, 12, 22, 11, 90]
 
bubble_sort(my_array)

print("Sorted array is:")
for i in range(len(my_array)):
    print(my_array[i])  
    #raise NotImplementedError()

# Only run this cell to check your answer. If it is true then no error will be raised
assert(bubble_sort([37, 42, 9, 19, 35, 4, 53, 22]) == [4, 9, 19, 22, 35, 37, 42, 53])
assert(bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5])

"""**Question 5.** 

Write a function to find $n^{th}$ Fibonacci number
The Fibonacci numbers are the numbers in the following integer sequence.

| 1  | 2 | 3  | 4 | 5  | 6 | 7  | 8 | 9 | 10 | 11 | 12 |
| -- |-- | -- | --| -- | --| -- | --|-- | -- |-- |-- |
| 0  | 1 | 1  | 2 | 3  | 5 | 8  | 13| 21| 34 |55 |89 |

Please consider index starting from 1

In mathematical terms, the sequence $F_n$ of Fibonacci numbers is defined by the recurrence relation 

$F_n = F_n-1 + F_n-2$

with seed values 

$F_0 = 0$ and $F_1 = 1$

"""

def Fibonacci(n):
 n1, n2 = 0, 1
 count = 0
 if n <= 0:
  print("Please enter a positive integer")
 else:
  while count < n-1:
   nth = n1 + n2
   n1 = n2
   n2 = nth
   count += 1
  return n1
   


Fibonacci(11)

# Only run this cell to check your answer. If it is true then no error will be raised
assert(Fibonacci(7) == 8)
assert(Fibonacci(9) == 21)