#asks the user to enter the length of the field in feet
length = float(input("Please enter the length of the field in feet - "))
#asks the user to enter the width of the field in feet
width = float(input("Please enter the width of the field in feet - "))
#calculating the area of the field
area = length * width
#converting the area into acres
area_acres = area/43560 # 1 acre = 43560 square feet
#printing the area filed in acre
print("Area of the farmer's field is",area_acres,"acres")
