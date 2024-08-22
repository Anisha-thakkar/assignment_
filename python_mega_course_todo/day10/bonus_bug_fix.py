try:
    w = float(input("width: "))
    l = float(input("length: "))
    print(w*l)
except ValueError:
    print("Invalid Input.. Try again giving a float number")