def compare_nums (num1, num2, num3):
    bigger_number = None
    if num1>= num2 and num1>=num3:
         bigger_number = num1
         return bigger_number
    elif num2>=num1 and num2>=3:
         bigger_number = num2
         return bigger_number
    else:
         bigger_number = num3
         return bigger_number

list_numbers = []

for x in range (3):
     list_numbers.append(int(input()))

print(int(list_numbers[0]))
print(int(list_numbers[1]))
print(int(list_numbers[2]))

print("The biggest number is " + str(compare_nums(list_numbers[0], list_numbers[1], list_numbers[2])))

