import random
answer=random.randint(1,100)

print("""Welcome user,
Test your luck with this number guessing game.
""")

print("""A number is randomly-generated from 1-100,
and all you'd have to do is guess it,
simple right?
""")

print("""1. easy(10 chances)
2. medium(5 chances)
3. hard(3 chances)""")

def chances(n:int):
      print(f"You have {n} chances")

drunning=True
while drunning:
      try:
            diff=int(input("Please select a difficulty: "))

            if diff == 1:
                  n=10
                  n_1=10
                  chances(10)
                  drunning=False
            elif diff == 2:
                  n=5
                  n_1=5
                  chances(5)
                  drunning=False
            elif diff == 3:
                  n_1=3
                  n=3
                  chances(3)
                  drunning=False

      except Exception:
            print("Please pick a choice from above(1-3)")

running=True

while n>0:
      try:
            guess=int(input("Guess the number: "))

            if guess>100 or guess<1:
                  print("That is out of range")

            elif guess>answer:
                  print("Woah too high!")
                  chances(n-1)
                  n=n-1
                  if n== 0:
                        print("uhoh, you ran out of chances")

            elif guess<answer:
                  print("Uh oh too low :P")
                  chances(n-1)
                  n=n-1
                  if n== 0:
                        print("Uhoh, you ran out of chances :(")

            else:
                  print("Congratulations, you guessed the number!")
                  print(f"It only took you {n_1-n+1} chances")
                  n=0

      except Exception:
            print("Please pick a number from 1-100")