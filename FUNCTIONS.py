#CHECK IF NUMBER IS ODD OR EVEN
def check_even_odd(num): 
  if num % 2 == 0: 
   return "Provided number is Even" 
  else: 
    return "Provided number is Odd" 
num = int(input("Enter a number: ")) 
print(check_even_odd(num)) 