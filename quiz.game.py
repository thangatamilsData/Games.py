playing = input("Do want to play the quiz? ")

if playing.lower() != "yes":
    quit()

print("let's play the game :")

answer=input("who create python :")
if answer == "van rossums":
    print("crt")
else:
    print("incrt")

answer=input("what is the function of encapsulation in python :")
if answer=="private, protect":
    print("crt")
else:
    print("incrt")

answer=input("what are operators in python :")
if (answer == 'arithmatic','assignment','camparission','logical','membership','bitwise','identity'):
    print("crt")
else:
    print("incrt")
 
