#Try except przykład

# age = int(input("How old are U? "))
# 
# if age > 18:
#     print(f"You can drive at age {age}")


try:
    age = int(input("How old are U? "))
except ValueError:
    print("You must input integer")
    age = int(input("How old are U? "))

if age > 18:
    print(f"You can drive at age {age}")