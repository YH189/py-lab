def calculate_bmi_risk(weight, height):
    if not isinstance(weight, (int, float)):
        return "Weight should be a number"
    if not isinstance(height, (int, float)):
        return "Height should be a number"
    if weight <= 0:
        return "Weight should be greater than 0"
    if height <= 0:
        return "Height should be greater than 0"
      
    bmi = weight / (height * height)

    if bmi < 18.5:
        return "Underweight"
    elif bmi <= 24.9:
        return "Normal weight"
    elif bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"
      
print(calculate_bmi_risk(55, 1.16))
print(calculate_bmi_risk(73, 1.79))
print(calculate_bmi_risk(85, 1.56))
print(calculate_bmi_risk(105, 1.63))
print(calculate_bmi_risk(65, 1.6))
