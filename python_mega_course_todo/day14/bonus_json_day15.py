import json
with open("que.json",'r') as file:
    data_=file.read()
data=json.loads(data_)
score=0
for que in data:
    print(que["question"])
    for index,alt in enumerate(que["alternatives"]):
        print(index+1,"-",alt)
    user_choice=int(input("Enter Answer: "))
    if user_choice==que["Correct Answer"]:
        score=score+1
print(score)
