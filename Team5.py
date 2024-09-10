import random

random_numbers = [random.randint(1, 100) for _ in range(10)]
print(random_numbers)

#add numbers
def calculate_sum(numbers):
    total = 0
    for i in numbers:
        total += i
    return total

# Calculate and print the sum
total_sum = calculate_sum(random_numbers)
print("Sum of random numbers:", total_sum)

def calculate_average(numbers):
    total_sum = calculate_sum(numbers)
    return total_sum / len(numbers)
    
    # Calculate and print the average
average = calculate_average(random_numbers)
print("Average of random numbers:", average)

def calculate_variance(numbers):
    mean = calculate_average(numbers)
    squared_differences = [(x - mean) ** 2 for x in numbers]
    return calculate_average(squared_differences)


# Calculate and print the variance
variance = calculate_variance(random_numbers)
print("Variance of random numbers:", variance)