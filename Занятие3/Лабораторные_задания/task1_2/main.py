OUTPUT_FILE = "output.txt"


def task(steps = 11):

    with open (OUTPUT_FILE, "w" , encoding ="utf-8") as f:
        for i in range(1, steps):
            f.write(f' "{"*" * i}"\n'.rjust(steps))

if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")

