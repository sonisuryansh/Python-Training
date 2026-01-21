#basic function
def hello():
    print("Hello, World!")
hello()

# 2. Write a function that takes a name as input and prints "Hello, <name>".
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")

# 3. Write a function that takes two numbers and prints their sum.
def add_numbers(a, b):
    print(f"The sum of {a} and {b} is {a + b}.")
add_numbers(5, 7)

# 4. Write a function that returns the square of a number.
def square(num):
    return num * num
result = square(4)
print(f"The square of 4 is {result}.")

# 5. Write a function to check if a number is even or odd.
def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")
check_even_odd(10)
check_even_odd(7)


# With Parameters & Return
# 6. Write a function that takes two numbers and returns their maximum.
def max_of_two(a, b):
    return a if a > b else b
max_num = max_of_two(10, 20)
print(f"The maximum of 10 and 20 is {max_num}.")

# 7. Write a function that takes a list of numbers and returns their average.
def average(numbers):
    return sum(numbers) / len(numbers)
nums = [10, 20, 30, 40, 50]
avg = average(nums)
print(f"The average of {nums} is {avg}.")

# 8. Write a function that counts vowels in a string.
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in s if char in vowels)
    return count
string = "Hello World"
vowel_count = count_vowels(string)
print(f"The number of vowels in '{string}' is {vowel_count}.")

# 9. Write a function that calculates factorial of a number (using loop).
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
fact = factorial(5)
print(f"The factorial of 5 is {fact}.")

# 10. Write a function to check if a string is a palindrome.
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
word = "racecar"
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
word2 = "hello"
if is_palindrome(word2):
    print(f"'{word2}' is a palindrome.")
else:
    print(f"'{word2}' is not a palindrome.")

# Default & Keyword Arguments
# 11. Write a function that calculates simple interest (default rate = 5%).
def simple_interest(principal, time, rate=5):
    interest = (principal * rate * time) / 100
    return interest
si = simple_interest(1000, 2)
print(f"The simple interest is {si}.")

# 12. Write a function that takes a name and age and prints them (use keyword arguments).
def print_info(name, age):
    print(f"Name: {name}, Age: {age}")
print_info(age=25, name="Bob")

# Recursive Functions
# 13. Write a recursive function to calculate factorial.
def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)
fact_rec = recursive_factorial(5)
print(f"The factorial of 5 (using recursion) is {fact_rec}.")

# 14. Write a recursive function to print Fibonacci series up to n terms.
def fibonacci(n, a=0, b=1):
    if n > 0:
        print(a, end=' ')
        fibonacci(n - 1, b, a + b)
print("Fibonacci series up to 7 terms:")
fibonacci(7)
print()

# Functions with Collections
# 15. Write a function that takes a list of numbers and returns the largest element.
def largest_in_list(numbers):
    return max(numbers)
nums_list = [3, 5, 2, 8, 1]
largest = largest_in_list(nums_list)
print(f"The largest number in {nums_list} is {largest}.")

# 16. Write a function that takes a dictionary and prints all key-value pairs.
def print_dict(d):
    for key, value in d.items():
        print(f"{key}: {value}")
sample_dict = {'a': 1, 'b': 2, 'c': 3}
print("Dictionary key-value pairs:")
print_dict(sample_dict)

# 17. Write a function that takes a set and returns its length.
def set_length(s):
    return len(s)
sample_set = {1, 2, 3, 4, 5}
length = set_length(sample_set)
print(f"The length of the set {sample_set} is {length}.")

# 18. Write a function that takes a list of dictionaries (students with marks) and returns the topper’s name.
def find_topper(students):
    topper = max(students, key=lambda x: x['marks'])
    return topper['name']
students_list = [
    {'name': 'Alice', 'marks': 85},
    {'name': 'Bob', 'marks': 92},
    {'name': 'Charlie', 'marks': 88}
]
topper_name = find_topper(students_list)
print(f"The topper is {topper_name}.")



