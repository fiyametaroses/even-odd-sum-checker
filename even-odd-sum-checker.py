def sum_of_numbers(numbers):
    return sum(numbers)

def process_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    even_sum = sum_of_numbers(even_numbers)
    print("Even numbers:", even_numbers)
    print("Sum of even numbers:", even_sum)

def process_odd_numbers(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    odd_sum = sum_of_numbers(odd_numbers)
    print("Odd numbers:", odd_numbers)
    print("Sum of odd numbers:", odd_sum)
    return odd_numbers, odd_sum

last_num = int(input("Enter the last number (10th number): "))
numbers = list(range(last_num - 9, last_num + 1))

total_sum = sum_of_numbers(numbers)

print("Numbers:", numbers)
print("Sum of all numbers:", total_sum)

process_even_numbers(numbers)
odd_numbers, odd_sum = process_odd_numbers(numbers)
