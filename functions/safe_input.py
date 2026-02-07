def safe_input(value_type: type):
    while True:
        try:
            return value_type(input(" >> "))
        except ValueError:
            print("Значення не коректні")
