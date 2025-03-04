# def calculate_mars_weight():
#     user_input = float(input("Enter your mars weight: "))
#     mars_weight = user_input * 0.378  
#     rounded_mars_weight = round(mars_weight, 2)  
#     print(f"Your weight on mars would be {rounded_mars_weight} kg.")

# calculate_mars_weight()

def calculate_weight_on_planet():
    earth_weight = float(input("Enter your weight on Earth (kg): "))
    planet = input("Enter the name of a planet: ") .lower() .strip()

    if planet == "mercury":
        gravity = 0.376
    elif planet == "venus":
        gravity = 0.889
    elif planet == "mars":
        gravity = 0.378
    elif planet == "jupiter":
        gravity = 2.36
    elif planet == "saturn":
        gravity = 1.081
    elif planet == "uranus":
        gravity = 0.815
    elif planet == "neptune":
        gravity = 1.14
    else:
        print("Invalid planet name.")
        return

    planet_weight = earth_weight * gravity
    print(f"Your weight on {planet} would be {round(planet_weight, 2)} kg.")

calculate_weight_on_planet()
