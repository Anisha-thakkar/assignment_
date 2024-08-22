today_date = input("Enter todays' date: ")
mood = input("Enter your mood today bw 0-10: ")
thoughts = input("Let you thoughts flow: ")

with open(f"{today_date}.txt","w") as file:
    file.write(mood+"\n")
    file.write(thoughts)