#GREATEST NUMBER OF 3 NUMBERS
def find_greatest(num1, num2,num3): 
  if num1 >= num2 and num1 >= num3: #If num1 is greater 
    return num1 
  elif  num2 >= num1 and num2 >= num3: #If num2 is greater 
    return num2 
  else:  #If num3 is greater 
    return num3 
#prompt values from user      
num1 = int(input("Enter first number: ")) 
num2 = int(input("Enter second number: ")) 
num3 = int(input("Enter third number: ")) 
print("The greatest number is:", find_greatest(num1, num2, num3)) 
