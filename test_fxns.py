from fitting_functions import *
#test linear function
if linear(2,3,4) == 10:
    print("Linear function works")
else:
    print("Linear function does not work")
#test slope_units funciton
if slope_units("meters", "kgs") == "meter/kg":
    print("Slope_unit function works")
else:
    print("Slope_unit function does not work")#, slope_units("meters", "kgs"))
#test print equation fucntion
if print_equation(4, 1, "kg", "meters") == "The equation of the line is: y = 4 meter/kg x + 1 kg":
    print("Print_equation works")
else:
    print("Print_equation doesn't work")


