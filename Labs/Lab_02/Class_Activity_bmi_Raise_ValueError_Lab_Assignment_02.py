
def bodymassindex(height,weight):
    try: 
        bmi = (weight)/(height**2) 
        if height < 0 or weight < 0:
            raise ValueError ("\nInvalid Input")
        print(f"\n{bmi}\n")

    except ValueError as exct:
        print(exct)
        print("\nPlease input Height and Weight greater than zero\n")

try:
    bodymassindex(height = float(input("\nThe height of the person in meters: ")),weight = float(input("\nThe weight of the person in kilograms: ")))
except ValueError as e:
    print("\nInvalid Data Type\n")