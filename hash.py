import hashlib
from sys import argv

run_counter = 0

def calculate_md5(input_string):
    """
    Calculate the MD5 hash of the input string.

    Args:
        input_string (str): The string to be hashed.

    Returns:
        str: The MD5 hash value of the input string.
    """
    md5_hash = hashlib.md5(input_string.encode()).hexdigest()
    return md5_hash


# v3
def main():
    """
    Entry point of the program.
    It prompts the user to enter a string to hash, calculates the MD5 hash of the string,
    and prints the hash value. It also keeps track of the number of times the program has been run.
    If the program has been run 5 times, it asks the user if they want to exit the program.
    """
    global run_counter
    run_counter += 1
    print(f"Run {run_counter}")

    if len(argv) > 1:
        input_string = " ".join(argv[1:])
    else:
        input_string = input("Enter a string to hash: ")

    md5_hash = calculate_md5(input_string)
    print(f"MD5 hash of '{input_string}': {md5_hash}")

    if run_counter == 5:
        choice = input("Do you wish to exit? y/n: ")
        if choice == "y":
            print("Exiting...")
            exit(0)
        else:
            run_counter = 0

while 1:
    if __name__ == "__main__":
        main()
#v2
""" if __name__ == "__main__":
        if len(argv) > 1:
            input_string = argv[1]
        else:
            input_string = "Hello, world!"

        md5_hash = calculate_md5(input_string) """

# v1
""" if __name__ == "__main__":
        input_string = "Hello, world!"
        md5_hash = calculate_md5(input_string)
        print(f"MD5 hash of '{input_string}': {md5_hash}")
 """
