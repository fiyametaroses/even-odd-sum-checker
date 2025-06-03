def process_even_numbers(numbers):
    even_numbers = []
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
            even_sum += num
    print("Even numbers:", even_numbers)
    print("Sum of even numbers:", even_sum)
    return even_numbers, even_sum

# Get user input
last_num = int(input("Enter the last number (10th number): "))

# Generate list of 10 numbers ending at last_num
numbers = [i for i in range(last_num - 9, last_num + 1)]

# Separate odd numbers and compute their sum
odd_numbers = [num for num in numbers if num % 2 != 0]
odd_sum = sum(odd_numbers)

# Compute total sum
total_sum = sum(numbers)

# Output
print("Numbers:", numbers)
print("Sum of all numbers:", total_sum)

# Process even numbers
even_numbers, even_sum = process_even_numbers(numbers)

# Output odd numbers
print("Odd numbers:", odd_numbers)
print("Sum of odd numbers:", odd_sum)
