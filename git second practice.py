def find_high_value(a,b):
    if a>b:
        return(a)
    else:
        return(b)
variable1 = int(input("Please enter first number : "))
variable2 = int(input("Please enter second number : "))
ans = find_high_value(variable1, variable2)
print("return value is")
print(ans)            
