#Created By ===Alt5chm3rz===
#https://github.com/satriobintang

#BMI Calculator Using Function
def bmi_regular(weight, height):
    return (weight / (height/100)**2)

def bmi_prime(weight, height):
    return (weight / (height/100)**2) / 25

def comparison(bmi):
    if bmi <= 15:
        return("You are very severely underweight.")
    elif bmi <= 16:
        return("You are severely underweight.")
    elif bmi <= 18.5:
        return("You are underweight.")
    elif bmi <= 25:
        return("You are normal.")
    elif bmi <= 30:
        return ("You are overweight.")
    elif bmi <= 35:
        return("You are obese class I.")
    elif bmi <= 40:
        return("You are obese class II.")
    elif bmi <= 45:
        return("You are obese class III.")
    elif bmi <= 50:
        return("You are obese class IV.")
    elif bmi <= 60:
        return("You are obese class V.")
    else:
        return("You are obese class VI.")

def start_or_exit():
    while True:
        answer = input("\nEnter Y to start, N to exit : ").upper()
        if answer == "Y":
            return True
        elif answer == "N":
            return False
        print("Please try again, the input you entered is wrong!\n")

def get_user_data():
    while True:
        try:
            weight = float(input("Enter your weight in kilogram (kg)   : "))
            height = float(input("Enter your height in centimeter (cm) : "))
            if weight> 0 and height > 0:
                return weight, height
            else:
                raise ValueError()
        except ValueError:
            print("Invalid input! Repeat again!")
            continue

def main():
    while True:
        if start_or_exit():
            print("\n"+"="*10,"BMI CALCULATOR"+"="*10)
            weight, height = get_user_data()
            bmi_prime_result = round(bmi_prime(weight, height),1)
            bmi =  round(bmi_regular(weight, height),1)
            category = comparison(bmi)

            print("\nYour BMI is :", bmi)
            print("Your prime BMI is :", bmi_prime_result)
            print(category)
        else:
            quit()
    
if __name__ == "__main__":
    main()

#Created By ===Alt5chm3rz===
#https://github.com/satriobintang