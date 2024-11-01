# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(add(1, 2, 3))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")

# display_name("hj", "woo")

# def print_address(**kwargs):
#     # for value in kwargs.values():
#     #     print(value)
#     # for key in kwargs.keys():
#     #     print(key)
    
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_address(street="123 fake st.", 
#               city="seoul", 
#               gu="mapogu", 
#               zip="01234")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    # for value in kwargs.values():
    #     print(value, end="\n")

    if "state" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')} {kwargs.get('state')}")
    elif "country" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
        print(f"{kwargs.get('country')}")
    else:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    print(f"{kwargs.get('city')} {kwargs.get('gu')} {kwargs.get('zip')}")


shipping_label("ms", "ju", "woo",
                street="123 fake st.",
                apt="303",
                country="korea",
                city="seoul",
                gu="mapo",
                zip="01234")
