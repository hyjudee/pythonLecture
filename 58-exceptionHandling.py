try:
    number = int(input("enter a number: "))
except ZeroDivisionError:
    print("you can not divide by zero idiot!")
except ValueError:
    print("enter only numbers plz!")
except Exception:
    print("something went wrong!")
finally:
    print("do some cleanup here")
