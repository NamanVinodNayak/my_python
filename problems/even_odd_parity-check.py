"""
Check Parity of a Number
Understand how to write a function in Python that checks whether a number is even or odd by returning 0 or 1. This lesson helps you apply basic data types and conditional logic to solve parity problems, reinforcing foundational programming skills.

Parity is a term to express if a given integer is even or odd.

Problem Statement
Given a checkParity(n) function, write code to determine if a given number n is even or odd. Think of this as a function that returns 0 if the number is even, and 1 if it is odd. You have been given some starter code where the function and return statement have already been written, so don’t worry about any Python-specific details about functions; just implement the function logic!

Input
A number

Output
The parity of the number

Sample Input
4
"""

def checkParity(n):
  ## Write your code here
  result = (n % 2)
  return result


print("Odd parity", checkParity(17))
print("Even parity", checkParity(16))