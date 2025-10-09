while(True):
    try:
        a = input("Please enter the first number.")
        if (a == 'q'):
            raise Exception
        a = int(a)
        b = input("Please enter the second number.")
        if (b == 'q'):
            raise Exception
        b = int(b)
        op = input("Please enter the operator (+, -, *, or /).")
        if (op == 'q'):
            raise Exception
        if (b == 0 and op == "/"):
            raise ZeroDivisionError
    except ValueError:
        print("This character cannot be converted to a number.")
    except ZeroDivisionError:
        print("You can't divide by zero.")
    except Exception:
        print("Ending program now.")
        break  

    else:
        if op == "+":
            print(f"{a}{op}{b}={a+b}")
        if op == "-":
            print(f"{a}{op}{b}={a-b}")
        if op == "*":
            print(f"{a}{op}{b}={a*b}")
        if op == "/":
            print(f"{a}{op}{b}={a/b}")
    finally:
        print("Attempt complete.")
