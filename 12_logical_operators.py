#example of logical operators 
a = int(input("Enter number for a")) 
b = int(input("Enter number for b")) 
c = int(input("Enter number for c")) 

#     10 < 20    20 < 30
#True        True       True
result = a < b and b < c
print(f"{result} = {a} < {b} and {b} < {c}")

# check a is below b or b is above c 
result = a < b or b > c
print(f"{result} = {a} < {b} or {b} > {c}")


result = not (a < b) 
print(f"{result} = not ({a} < {b})") 
