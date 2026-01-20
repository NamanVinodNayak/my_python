"""
Compute Sum of First 'n' Natural Numbers

Problem Statement
Implement a function that takes a number n and calculates the sum of the first n natural numbers.

Input
An integer n

Output
Sum of the first n natural numbers

Sample Input
5

Sample Output
15
"""
def sum_of_natural_numbers(n):
    return n * (n + 1) // 2
print(sum_of_natural_numbers(5))
