def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me the correct name and phone please."
        except IndexError:
            return "Enter the argument for the command."

    return inner


@input_error
def add_contact(contacts, *args):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(contacts, *args):
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(contacts, *args):
    name = args[0]
    if name not in contacts:
        raise KeyError
    return contacts[name]


@input_error
def show_all(contacts, *args):
    return "\n".join([f"{name}: {number}" for name, number in contacts.items()])


def main():
    contacts = {}
    print("Welcome to the assistant bot! Type 'exit' or 'close' to quit.")

    while True:
        user_input = input("Enter a command: ")
        command, *args = user_input.split()

        if command.lower() in ["exit", "close"]:
            print("Good bye!")
            break
        elif command.lower() == "hello":
            print("How can I help you?")
        elif command.lower() == "add":
            print(add_contact(contacts, *args))
        elif command.lower() == "change":
            print(change_contact(contacts, *args))
        elif command.lower() == "phone":
            print(show_phone(contacts, *args))
        elif command.lower() == "all":
            print(show_all(contacts, *args))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
