# we can also do type annotation here
messages: list[dict] = []
# Where:
#   messages        - is the variable name
#   : list[dict]    - hints that this (messages) variable is a list of dictionaries
#   = []            - an empty list

def add_message(sender, message):
    # before we insert, let's validate first the given input first
    # like making sure that:
    #   - there is a sender supplied
    #   - there is a message supplied
    # you can also do 
    #   `if len(sender) == 0`
    # but thats too long
    if (not sender) or (not message):
        print("Sender or message cannot be empty.")
        return

    messages.append({
        "sender": sender,
        "message": message,
    })

def display_messages():
    for message in messages:
        print(f"{message.get("sender")}: {message.get("message")}")

def main():
    add_message("Ryan", "Hello world")
    add_message("Aori", "Hello sad diha")
    add_message("Ryan", "Okay ra ko ari")
    add_message("Aori", "six sevennn")
    add_message("Ryan", "HEEE HEE")
    display_messages()

if __name__ == "__main__":
    main()