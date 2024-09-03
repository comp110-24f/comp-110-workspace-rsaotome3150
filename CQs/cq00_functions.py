__author__ = "730770150"

"""Function mimic will take your input and repeat it back to you"""


def mimic(message: str) -> str:
    return message


"""main function pulls together your functions"""


def main() -> None:
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
