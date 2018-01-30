# Part 2: Functions
# Parameters: N/A
# Returns: N/A
import math

def mars_weight():
    """Ask the user what is his or her weight on her, convert that weight to
    what it would be on mars.

    Then print out that weight.

    """
    earth_wght = float(input('What is your weight? '))
    mars = (earth_wght*.38)
    print('At a weight of ', int(earth_wght),
          ' pounds you would weigh ', int(mars), ' pounds on Mars.',"\n")


mars_weight()

# Function: Volume of a cone
# # Parameters: N/A
# Returns: Volume of the Cone

def volume_of_cone():
    """The function uses the input values of the parameters to return a value
    for the volume of the cone."""
    r = int(input('What is the length of the radius of the cone? '))
    h = int(input('What is the height of the cone? '))

    v = float((math.pi*r*r*h)/3)  
    return v

print("{:.3f}".format((volume_of_cone())),"\n")

# Function: Liquid Converter
# Parameters: N/A
# Return Value

def liquid_converter():
    """ The function is an user-interactive function to convert any number of fluid ounces to the
    equivalent number of gallons, quarts, pints, and gills."
    """

    fluid_oz = int(input("How many fluid ounces would you like to convert? "))
    galls = fluid_oz // 128
    new1_fluid_oz = fluid_oz - (galls*128)
    quart = new1_fluid_oz // 32
    new2_fluid_oz = new1_fluid_oz - (quart*32)
    pint =  new2_fluid_oz // 16
    new3_fluid_oz = new2_fluid_oz - (pint*16)
    gill = new3_fluid_oz // 4

    print(fluid_oz, " fluid ounces is ", galls, " gallon(s) ", quart, " quart(s) ", pint , " pint(s) ", gill, " gill(s)", "\n")

liquid_converter()

# Function: main
# Parameter: N/A
# Return Value: N/A


def main():
    init = int(input("Which function would you like to call? "))
    if init == 1:
        mars_weight()
    elif init == 2:
        volume_of_cone()
    elif init == 3:
        liquid_converter()
    else:
        print("Not a function")
        
for i in range(3):
    main()