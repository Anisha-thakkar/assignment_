height_ft = input("Enter feet and inches: ")

def get_height_mtr(ipt):
    part=ipt.split(" ")
    return float(part[0])*0.3048 + float(part[1])*0.0254

print(get_height_mtr(height_ft))