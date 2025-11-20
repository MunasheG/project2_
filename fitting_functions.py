def linear(m,x,b):
    y = m * x + b
    return y

def slope_units(x_units, y_units):
    x = x_units.rstrip("s")
    y = y_units.rstrip("s")
    return x + "/" + y

def print_equation(m, b, y_units, x_units):
    slope_u = slope_units(x_units, y_units)
    b_units = y_units.rstrip("s")
    print(f"The equation of the line is: y = {m} {slope_u} x + {b} {b_units}") 
    
