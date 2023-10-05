import random

def test():
    # find highest score with loop/if
    student_scores = input("enter a list of scores separated by space: ").split()
    max_score = 0
    for score in student_scores:
        if int(score) > max_score:
            max_score = int(score)
    print(f'max score is {max_score} out of {student_scores}')

    # add all numbers from 1 to 100 and find the total number
    result = 0
    for num in range(1,101):
        result += num
    print(f'total number is {result}')

    # password generator
    letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
    ]
    numbers = ['1','2','3','4','5','6','7','8','9']
    symbols = ['!','#','$','%','&','(',')','*','-','+']
    u_letters = int(input("How many letters would you like in your password? "))
    u_symbols = int(input("How many symbols would you like in your password? "))
    u_numbers = int(input("How many numbers would you like in your password? "))
    res_letters = []
    res_symbols = []
    res_numbers = []
    for _ in range(0, u_letters):
        res_letters.append(letters[random.randint(0, len(letters)-1)])
    for _ in range(0, u_symbols):
        res_symbols.append(symbols[random.randint(0, len(symbols)-1)])
    for _ in range(0, u_numbers):
        res_numbers.append(numbers[random.randint(0, len(numbers)-1)])
    print(f' letters: {res_letters}\n symbols: {res_symbols}\n numbers: {res_numbers}')
    result = res_letters + res_symbols + res_numbers
    print(f' pre:     {result}')
    random.shuffle(result)
    print(f' pwrd:    {result}')

    # divisible numbers
    # get 1st & 2nd number from user (2nd > 1st)
    # get 3rd number called "divisible by"
    # find out how many numbers between these two are divisible by 3rd number
    first = int(input('Please enter the 1st number: '))
    second = int(input('Please enter the 2nd number: '))
    divisible = int(input('Please enter the divisible number: '))
    result = 0
    if second > first:
        for num in range(first, second + 1):
            if num % divisible == 0:
                result += 1
        print(f'There are {result} numbers divisible by {divisible} between {first} and {second}')
    else:
        print(f'Second number {second} must be bigger than first number {first}')

    # guess a number
    # get a number from user and generate a random number from 0 up to the one the user entered
    # ask the user to make a guess -> will display a message if the guessed number is correct
    # if not correct, it'll go back and ask for the number again
    # finally, it keeps a count of how many times the user tried
    # at the end, it'll display the correct number and how many guesses it took
    user_number = input('Please enter a number: ')
    if user_number.isdigit():
        user_number = int(user_number)
        randy = random.randint(0, user_number)
        attempts = 1
        is_guessed = False
        while not is_guessed:
            guess = int(input('Guess the number '))
            if guess == randy:
                print(f'You guessed it with {attempts} attempts ! your number: {user_number}, random: {randy}')
                is_guessed = True
            else:
                attempts += 1
    else:
        print(f'Invalid number {user_number}')

