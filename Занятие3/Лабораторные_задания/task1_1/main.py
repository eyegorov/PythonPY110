INPUT_FILE = "input.txt"


def task() -> None:
    with open(INPUT_FILE, "r") as file:
        for line in file:
            print(line.rstrip())

if __name__ == "__main__":