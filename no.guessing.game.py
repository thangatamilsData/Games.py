import random

top_range=input("Enter the number :")

if top_range.isdigit():
    top_range=int(top_range)

    if top_range <= 0:
        print("hey type larger number")
        quit()
else:
    print("Please enter the number")
    quit()

random_no = random.randint(1,top_range)#you can use randrange() also

print(random_no)

guess=0
while True:
    guess +=1
    
    user_guess = input("make a guess :")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("please enter the number")
        continue

    if user_guess == random_no:
        print("You got it crt !")
        break

    elif user_guess > random_no:
        print("your above the number")
        
    else:
        print("you below the number")
        
    
print("You got it in", guess, "guesses")
