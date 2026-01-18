"""
Sum of Squares of Even Numbers
Explore how to create a list of squares of even numbers from 0 to 20 using Python list comprehensions. Learn to sum these numbers effectively while reinforcing list handling and Python syntax skills in a hands-on coding challenge.

Problem Statement
Given an evenSquare() function, create a list with the squares of the even numbers from 0 to 20. The final output should be the sum of even numbers in the list:

Input
A list with the square of even numbers from 0-20

Output
The sum of the numbers in the list

sum : 1540
0
2
4
6
8
10
12
14
16
18
20

"""

def evenSquareSum():
  even = [x * x for x in range(0, 21, 2)]
  return sum(even)
  
print(evenSquareSum())