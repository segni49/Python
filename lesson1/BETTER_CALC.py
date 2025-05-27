num1 = input('enter a number ..')  
num2 = input('enter the 2nd number ..')
operator = input('choose operator +/-/*/')

if operator == '+':
    result = float(num1) + float(num2)
elif operator == '-':
    result = float(num1) - float(num2)
elif operator == '*':
    result = float(num1) * float(num2)
elif operator == '/':
    result = float(num1) / float(num2)
else:
    result = 'Invalid operator'

print('The result is:', result)