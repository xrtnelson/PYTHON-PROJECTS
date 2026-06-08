import random
print('Welcome to the number guessing game.')
answer = random.randint(0, 100)
is_running = True
print('The number is betwwen 0 and 100')
while is_running:
    
    guess = input('What is your guess?: ')


    if guess.isdigit():
        guess = int(guess)

        
        if guess < 0 or guess > 100:
            print('Cant you read?? It clearly says it is a number between 0 and 100')


        elif guess > answer:
            print('Lower please')
    
        elif guess < answer:
            print('Higher')
        elif guess == answer:
            print('Hurray that is it🥳🥳. Only took you a gazillion tries')
            is_running = False
            t= input('Hope you enjoyed the game ')
    else:
        print('That is not a number dude')
        print('Select a number(not a letter) that is between 0 and 100')
    
    
