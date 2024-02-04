def reverse_numbers(input_number):
    retro_number = str(input_number)[::-1]
    return retro_number


user_input = int(input())
result = reverse_numbers(user_input)
print(result, end='\n')