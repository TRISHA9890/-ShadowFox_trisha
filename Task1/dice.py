import random

num_rolls=20
rolls=[]

for _ in range (num_rolls):
    roll=random.randint(1,6)
    rolls.append(roll)

    num_sixes=rolls.count(6)
    num_ones= rolls.count(1)
    num_conservative_sixes=0

    for i in range(1,len(rolls)):
        if rolls[i]==6 and rolls[i-1]==6:
            num_conservative_sixes +=1

            for i in range(1,len(rolls)):
                if rolls[i]==6 and rolls[i-1]==6:
                    num_conservative_sixes+=1

                    print(f"Number of times rolled a 6:{num_sixes}")
                    print(f"Number of times rolled a 6:{num_ones}")
                    print(f"Number of times rolled a 6:{num_conservative_sixes}")
                    