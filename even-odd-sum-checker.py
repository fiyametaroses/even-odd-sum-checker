def process_numbers(last_num):
    numbers = []

    for i in range(last_num - 9, last_num + 1):
        numbers.append(i)

    even_numbers = []
    odd_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    total_sum_of_numbers = 0
    for num in numbers:
        total_sum_of_numbers += num

    even_sum = 0
    for num in even_numbers:
        even_sum += num

    odd_sum = 0
    for num in odd_numbers:
        odd_sum += num

    print("Numbers:", numbers)
    print("Sum of all numbers:", total_sum_of_numbers)
    print("Even numbers:", even_numbers)
    print("Sum of even numbers:", even_sum)
    print("Odd numbers:", odd_numbers)
    print("Sum of odd numbers:", odd_sum)

# Get user input
try:
    last_number = int(input("Enter the last number (10th number): "))
    if last_number < 10:
        print("Please enter a number greater than or equal to 10.")
    else:
        process_numbers(last_number)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
