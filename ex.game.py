import random

number = input("Enter the numbeer :")

if number.isdigit():
    number = int(number)

    if number <= 0 :
        print("please enter the larger number")
        quit()

else:
    print("please enter the number")
    quit()

random = random.randint(1,number)

print(random)
count = 0
while True:
    count +=1

    user_no = input("make a guess :")

    if user_no.isdigit():
        user_no = int(user_no)

    else :
        print("please enter the number")
        continue

    if user_no == random :
        print("it's crt")
        break
    
    elif user_no > random :
        print("your above the number")

    else :
        print("your below the number")

print("you got it at", count, 'guesses')
  
