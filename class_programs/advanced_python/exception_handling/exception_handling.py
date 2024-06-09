try:
    num = int(input("Enter a number for Arithmetic operations"))
    div = 4 / num
    a = b

except ZeroDivisionError:
    print("Please give the Non-zero number for the division")
except ValueError:
    print("Please give only the numbers")
except Exception as e:
    print(e)


else:
    print(div)
    mul = 4 * num
    add = 4 + num
    print(mul)
    print(add)
