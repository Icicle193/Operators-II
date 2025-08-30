Weight = float(input("Enter your weight:" ))
Height = float(input("Enter your height:" ))

BMI = Weight / (Height/100)**2
print("Your BMI is", BMI)

if BMI <=18.4:
    print("You are not eating well")
elif BMI <=24.9:
    print("You are healthy")
elif BMI <=29.9:
    print("You are a bit too fat")
elif BMI <=34.9:
    print("Stop eating so much")
elif BMI <=39.9:
    print("You are very fat, calm down")
else:
    print("You are severly fat")