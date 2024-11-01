def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

# hello("hello", "ms.", "ju", "woo")
# hello("helo", title="ms.", first="hj", last="woo")
# hello("helo", title="ms.", last="woo", first="hj")

# for x in range(1,11):
#     print(x, end=" ")

# print("1", "2", "3", "4", "5", sep="-")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=82, area=10, first=3456, last=7890)

print(phone_num)
