def process_even_numbers(numbers):
    even_numbers = []
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
            even_sum += num
    print("Even numbers:", even_numbers)
    print("Sum of even numbers:", even_sum)

last_num = int(input("Enter the last number (10th number): "))
numbers = []

for i in range(last_num - 9, last_num + 1):
    numbers.append(i)

even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2!= 0:
        odd_numbers.append(num)

total_sum = 0
for num in numbers:
    total_sum += num



odd_sum = 0
for num in odd_numbers:
    odd_sum += num

print("Numbers:", numbers)
print("Sum of all numbers:", total_sum)
print("Even numbers:", even_numbers)
process_even_numbers(numbers)
print("Odd numbers:", odd_numbers)
print("Sum of odd numbers:", odd_sum)