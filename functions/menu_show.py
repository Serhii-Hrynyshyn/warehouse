def menu_show(dictionary: dict) -> None:
    print("-" * 45)
    values = dictionary["text"]
    counter = 1
    for key, value in values.items():
        print(f"\t{counter}: {value}")
        counter += 1
    print("-" * 45)
