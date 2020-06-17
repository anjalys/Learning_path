def weather_condition(temperature):
    if temperature < 15:
        return "Cold"
    elif temperature >= 15 and temperature <=25:
        return "Warm"  
    elif temperature > 25:
        return "Hot"

user_input = float(input("Enter Temperature: "))

type(user_input)
print(weather_condition(user_input))