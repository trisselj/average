#Entering of numbers to be averaged
num1 = input("Please input the first number you would like to average")
num2 = input("Please input the second number you would like to average")
num3 = input("Please input the third number you would like to average")
num4 = input("Please input the fourth number you would like to average")
num5 = input("Please input the fifth number you would like to average")
#making numbers as numbers
numb1 = float(num1)
numb2 = float(num2)
numb3 = float(num3)
numb4 = float(num4)
numb5 = float(num5)
#averaging
average = (numb1 + numb2 + numb3 + numb4 + numb5) / 5
#printing answer
print("the average of the numbers you inputted is " + str(average))

