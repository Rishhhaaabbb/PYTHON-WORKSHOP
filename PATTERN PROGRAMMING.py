#DIFFERENT TYPES OF PATTERN PROGRAMMING

#SQUARE PATTERN 
n = int(input("Enter the number of rows: ")) 
for i in range(n): 
    for j in range(n): 
        print("*", end=" ") 
    print() 
    

# #TRIANGLE PATTERN
# n = int(input("Enter the number of rows: ")) 
# for i in range(n): 
#     for j in range(i+1): 
#         print("*", end=" ") 
#     print() 



#PYRAMID PATTERN    

# n = int(input("Enter the number of rows: ")) 
 
# for i in range(n): 
#     for j in range(n-i-1): 
#         print(" ", end=" ") 
#     for k in range(i+1): 
#         print("*", end=" ") 
#     print() 

#DIAMOND PATTERN

# # Get the number of rows from the user
# n = int(input("Enter the number of rows: "))

# # Print the upper half of the diamond
# for i in range(n):
#     print(" " * (n - i - 1), end="")
#     print("* " * (i + 1))

# # Print the lower half of the diamond
# for i in range(n - 2, -1, -1):
#     print(" " * (n - i - 1), end="")
#     print("* " * (i + 1))
