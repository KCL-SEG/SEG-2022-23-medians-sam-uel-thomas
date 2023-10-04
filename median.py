"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def median(numbers):
    numbers.sort()

    if len(numbers) % 2 == 0:
        left_middle = len(numbers) // 2 - 1
        right_middle = len(numbers) // 2
        middle = (numbers[left_middle] + numbers[right_middle]) / 2
        return(middle)
    
    else:
        return(numbers[len(numbers) // 2])


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        print("The median is: ", median(numbers))
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break


