class Calculator:
    def add(self,first_num,second_num):
        answer = first_num + second_num
        print(f'The answer is {answer}')
        print('Thank you ')
    def subtract(self,first_num,second_num):
        answer = first_num - second_num
        print(f'The answer is {answer}')
        print('Thank you ')
    def multiply(self,first_num,second_num): 
        answer = first_num * second_num
        print(f'The answer is {answer}')
        print('Thank you ')
    def divide(self,first_num,second_num):
        answer = first_num / second_num
        print(f'The answer is {answer}')
        print('Thank you ')
calculator = Calculator()
print('WELCOME TO MY CALCULATOR PROGRAM')
print('**********************************')
options = ['1.ADD','2.SUBTRACT','3.DIVIDE', '4.MULTIPLY']
for option in options:
    print(option, sep='/n')
print('***********************************')
choice = input('Choose an option(1-4): ')
is_running = True
while is_running:
    if choice == '1':
        calculator.add(first_num = float(input('Enter the first number: ')),second_num = float(input('Enter the second number: ')))
        is_running = False
    elif choice == '2':
        calculator.subtract(first_num = float(input('Enter the first number: ')),second_num = float(input('Enter the second number: ')))
        is_running = False
    elif choice == '3':
        calculator.divide(first_num = float(input('Enter the first number: ')),second_num = float(input('Enter the second number: ')))
        is_running = False
    elif choice == '4':
        calculator.multiply(first_num = float(input('Enter the first number: ')),second_num = float(input('Enter the second number: ')))
        is_running = False
    elif choice not in ['1','2','3','4']:
        print('INCORRECT CHOICE')
        choice = input('Please select a valid option(1-4): ')

    
        