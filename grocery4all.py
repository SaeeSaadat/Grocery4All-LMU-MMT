import os


def clear_terminal():
    # Clear terminal command for different platforms
    command = "clear"  # Linux and macOS
    if os.name == "nt":  # Windows
        command = "cls"
    os.system(command)


def print_welcome_message():
    with open('welcome_message.txt', 'r') as f:
        welcome_message = f.read()
    try:
        print(welcome_message.center(os.get_terminal_size().columns))
    except OSError:
        print(welcome_message)


def initiate_program():
    pass


def graceful_exit():
    print("I hope you come back soon!\nGoodbye!")
    print("... Developed by: Saee Saadat ...")
    print("... Project GitHub Repository: https://github.com/SaeeSaadat/Grocery4All-LMU-MMT ...")

def start_instruction_loop():
    while True:
        instruction = input("Command> \t")
        if instruction.lower() == "exit":
            graceful_exit()
            break
        elif instruction.lower() == "help":
            print("Help instructions")  # TODO: Add help instructions
        elif instruction.lower() == "clear":
            clear_terminal()
        else:
            print("Instruction not recognized.")


if __name__ == '__main__':
    clear_terminal()
    print_welcome_message()
    initiate_program()
    start_instruction_loop()
