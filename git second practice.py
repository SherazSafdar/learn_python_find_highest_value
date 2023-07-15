def find_highest_value(a,b):
    if a>b:
        return(a) 
    else:
        return(b)
variable1 = int(input("Please enter first number : "))
variable2 = int(input("Please enter second number : "))
ans = find_highest_value(variable1, variable2)
print("highest value is")
print(ans)            
