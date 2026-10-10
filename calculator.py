print('='*60)
print('PRISLEY CALCULATOR')
print('='*60)
print('1. Add (+)')
print('2. Subtraction (-)')
print('3. Multiply (×)')
print('4. Divide (÷)')
print('5. Exit')
print('='*60)
choice = input('Choose 1-5: ')
if choice == '5':
	print('Thanks for using PRISLEY CALCULATOR! - built by a young ENGINEER') 
if choice not in ['1', '2', '3', '4']:
	print('Hi dear, just choose 1 to 5 only - Thanks')
if choice in ['1', '2', '3', '4']:
	num1 = float(input('Enter first number: '))
	num2 = float(input('Enter second number: '))
	if choice == '1':
		print(f'{num1} + {num2} = {num1 + num2}')
	elif choice == '2':
			print(f'{num1} - {num2} = {num1 - num2}')
	elif choice == '3':
			print(f'{num1} * {num2} = {num1 * num2}')
	elif choice == '4':
		if num2 == 0:
			print("Error: Cannot divide by 0")
		else:
			print(f'{num1} / {num2} = {num1 / num2}')
