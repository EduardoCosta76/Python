'''Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Equal to or over 18.5 but below 25 they have a normal weight
Equal to or over 25 but below 30 they are slightly overweight
Equal to or over 30 but below 35 they are obese
Equal to or over 35 they are clinically obese.'''

height = float(input('What is your height? '))
weight = float(input('What is your weight? '))
bmi = weight / height **2
if bmi < 18.5:
    print('Your BMI is {:.2f}. You are underweight!'.format(bmi))
elif bmi >= 18.5 and bmi < 25:
    print('Your BMI is {:.2f}. You are on your normal weight!'.format(bmi))
elif bmi >= 25 and bmi < 30:
    print('Your BMI is {:.2f}. You are slightly overweight!'.format(bmi))
elif bmi >= 30 and bmi < 35:
    print('Your BMI is {:.2f}. You are obese!'.format(bmi))
else:
    print('Your BMI is {:.2f}. You are clinically obese!'.format(bmi))