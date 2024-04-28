import random

x=random.randint(1,1000)

pick=int(input("Guess no of your choice between 1 to 1000: "))

print("your number", pick)

print("My number",x)

if pick== x :

    print("Your Number Mathched With My Number ")

else:

    print("Your Number Not Matched With Mine") 

    print('Better luck next time')
