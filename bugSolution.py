def calculate_average(numbers):
    if not numbers:
        return 0
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 #Handle case where list contains no numbers
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_list_with_zero = [10,0, 20, 30, 40, 50]
average_zero = calculate_average(my_list_with_zero)
print(f"The average with zeros is: {average_zero}")

my_list_with_strings = [10, 20, 'thirty', 40, 50]
average_strings = calculate_average(my_list_with_strings)
print(f"The average with strings is: {average_strings}") #This will correctly print 0 because it filters out the strings