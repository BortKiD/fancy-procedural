numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

none_index = numbers.index(None)
only_numbers = numbers[:none_index] + numbers[none_index+1:]
sum_of_numbers = sum(only_numbers)
count_of_numbers = len(numbers)
missed_value = sum_of_numbers / count_of_numbers
numbers[none_index] = missed_value

print("Измененный список:", numbers)
