import random 

n = random.randint(1, 100)
a = -1
guesses = 0

while(a != n and guesses < 7):
    
    a = int(input("Guess the number between 1 to 100 : "))

    guesses += 1
    attempts = 7 - guesses
    if(a < n and attempts != 0):
       print(f"The number is higher than {a}")
       print(f"{attempts} Attempts left")
       
    elif(a > n and attempts != 0):
       print(f"The number is  lower than {a}")
       print(f"{attempts} Attempts left")
      
    elif(a == n):
       print(f"Congrats! You guess the correct number in {guesses} guesses")
    else:
       print(f"Game over! The number was {n}")


