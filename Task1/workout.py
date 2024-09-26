total_jumping_jacks=0

while total_jumping_jacks<100:
    print("Perform 10 jumping jacks!")
    print("Press enter when you are done")
    total_jumping_jacks+=10
    print(f"You are completed {total_jumping_jacks}jumping jacks so far.")

    tired=input("Are you tired?(yes/no):")
if tired.lowe()=="yes"or tired.lower()=="y":
    skip_remaining=input("Do you want to skip the remaining sets?(yes/no):")
    if skip_remaining.lower()=="yes"or skip_remaining.lower=="y":
        print(f"You completed a total of{total_jumping_jacks} jumping jacks.")
