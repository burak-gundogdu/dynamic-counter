def counter(limit, step):
    numbers = []
    for i in range(0, limit + 1, step):
        numbers.append(i)
    return numbers


def get_user_input():
    """Gets and validates user input for limit and step."""
    while True:
        try:
            limit = int(input("Enter the number to count up to: "))
            step = int(input("Enter the counting step: "))

            if limit <= 0 or step <= 0:
                print("Please enter positive numbers only.")
                continue

            return limit, step
        except ValueError:
            print("Invalid input. Numbers only, please.")


def main():
    print("\n=== Dynamic Counter Application ===\n")

    limit, step = get_user_input()
    result = counter(limit, step)

    print("\nResult:")
    print(*result, sep=", ")


if __name__ == "__main__":
    main()                
