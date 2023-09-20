def test():
    # remaining age from now until 90 yo in years, months & days
    years = 90 - int(input("what is your age: "))
    print(f"years: {years }, months: {   years * 12}, days: {years*365}")
    
    # tip calculator
    print('Welcome to the tip calculator')
    bill = float(input('What was the total bill? $'))
    tip = float(input('What percentage tip would you like to give? 10, 20, 15? '))
    people = int(input('How many people to split the bill? '))
    total_person = (bill + bill * (tip / 100)) / people
    print(f'Each person should pay ${round(total_person, 2)}')

    # is odd or even
    num = int(input('insert a number: '))
    if (num % 2) > 0:
        print(f'{num} is odd')
    else:
        print(f'{num} is even')

    # BMI calculator
    weight = float(input('insert you weight in kg: '))
    height = float(input('insert you height in cm: '))
    bmi = weight / ((height/100) ** 2)
    print(f'your bmi is {bmi}')
    if bmi < 18.5:
        print('underweight')
    elif bmi <= 24.9:
        print('normal') 
    elif bmi <= 29.9:
        print('overweight')
    else:
        print('very overweight')

    # leap year
    # the year should be evently divisible by 4
    # except every year that is evently divisible by 100
    # unless the year is also evently divisible by 400
    year = int(input('enter a year: '))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print('yep')
    else:
        print('nop')

    # bill generetor app
    # Type prices: S=$10, M=$20, L=$25 / Choco addon: $4 / Candles addon: $6
    print('Welcome to our bakery!')
    type = input('What size of cake? S,M,L : ')
    add_chocolate = input("Do you want extra chocolate? Y,N : ")
    add_candles = input("Do you want to add candles? Y,N : ")
    price = 0
    if type == 'S':
        price += 10
    elif type == 'M':
        price += 20
    else:
        price += 25
    if add_chocolate == 'Y':
        price += 4
    if add_candles == 'Y':
        price += 6
    print(f'Your cake is ${price}')