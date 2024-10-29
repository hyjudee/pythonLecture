capitals = {"korea": "seoul",
            "thailand": "bangkok",
            "germany": "berlin",
            "japan": "tokyo"}

print(capitals.get("korea"))

if capitals.get("thailand"):
    print("that capital ecists")
else:
    print("that capital does not exist")

capitals.update({"poland": "warsaw"})
capitals.update({"korea": "busan"})

capitals.pop("japan")
capitals.popitem()
capitals.clear()

key = capitals.keys()
for key in capitals.keys():
    print(key)

values = capitals.values()
for value in capitals.values():
    print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")

    