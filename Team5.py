import random

random_numbers_is_not = [random.randint(1, 100) for _ in range(10)]
print(random_numbers_is_not)


#add numbers
def calculate_sum(numbers):
    total = 0
    for i in numbers:
        total += i
    return total

# Calculate and print the sum
total_sum = calculate_sum(random_numbers)
print("Sum of random numbers:", total_sum)