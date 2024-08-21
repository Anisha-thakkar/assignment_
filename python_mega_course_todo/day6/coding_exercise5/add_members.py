member = input("enter a new member name: ")

file = open('members.txt', 'r')
members = file.readlines()
file.close()

members.append(member.title()+"\n")

file = open('members.txt', 'w')
file.writelines(members)
file.close()