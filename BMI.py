weight_in_kilograms=input("Your weight in kilograms:")
height_in_meters=input("Your height in meters:")

body_mass_index=round(float(weight_in_kilograms),2)/(round(float(height_in_meters),2)*round(float(height_in_meters),2))

print("Your BMI is:", round(body_mass_index,2))