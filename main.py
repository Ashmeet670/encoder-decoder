
class text:
    red = '\033[91m'
    darkred = '\033[31m'
    yellow = '\033[93m'
    purple = '\033[95m'
    green = '\033[92m'
    cyan = '\033[94m'
    END = '\033[0m'


def start():
    print(text.purple + "Welcome to Encoder-Decoder" + text.END)
    print(text.purple + "Do you want to encode your message or decode one made with this encoder" + text.END)
    global coding
    coding = input(text.yellow + "E for Encode and D for Decode " + text.END)

    if coding.isalpha():
        coding = coding.lower()
        if coding == "e" or coding == "encode" or coding == "encoding":
            encode()
        elif coding == "d" or coding == "decode" or coding == "decoding":
            decode()
        else:
            print(text.darkred + "Please enter a valid option" + text.END)
            start()

    else:
        print(text.darkred + "Please enter a valid option" + text.END)
        start()


def encode():
    message = input(
        text.purple + "Enter the message you want to encode: " + text.END)
    message = message.lower()
    encodedmessage = ""
    spaceSymbole = 1

    for letter in message:
        if letter == "a":
            encodedmessage = encodedmessage + "m"
        elif letter == "b":
            encodedmessage = encodedmessage + "!"
        elif letter == "c":
            encodedmessage = encodedmessage + "n"
        elif letter == "d":
            encodedmessage = encodedmessage + "@"
        elif letter == "e":
            encodedmessage = encodedmessage + "o"
        elif letter == "f":
            encodedmessage = encodedmessage + "#"
        elif letter == "g":
            encodedmessage = encodedmessage + "p"
        elif letter == "h":
            encodedmessage = encodedmessage + "$"
        elif letter == "i":
            encodedmessage = encodedmessage + "q"
        elif letter == "j":
            encodedmessage = encodedmessage + "%"
        elif letter == "k":
            encodedmessage = encodedmessage + "r"
        elif letter == "l":
            encodedmessage = encodedmessage + "^"
        elif letter == "m":
            encodedmessage = encodedmessage + "s"
        elif letter == "n":
            encodedmessage = encodedmessage + "&"
        elif letter == "o":
            encodedmessage = encodedmessage + "t"
        elif letter == "p":
            encodedmessage = encodedmessage + "*"
        elif letter == "q":
            encodedmessage = encodedmessage + "u"
        elif letter == "r":
            encodedmessage = encodedmessage + "("
        elif letter == "s":
            encodedmessage = encodedmessage + "v"
        elif letter == "t":
            encodedmessage = encodedmessage + ")"
        elif letter == "u":
            encodedmessage = encodedmessage + "w"
        elif letter == "v":
            encodedmessage = encodedmessage + "["
        elif letter == "w":
            encodedmessage = encodedmessage + "x"
        elif letter == "x":
            encodedmessage = encodedmessage + "]"
        elif letter == "y":
            encodedmessage = encodedmessage + "y"
        elif letter == "z":
            encodedmessage = encodedmessage + "+"
        elif letter == "1":
            encodedmessage = encodedmessage + "c"
        elif letter == "2":
            encodedmessage = encodedmessage + "d"
        elif letter == "3":
            encodedmessage = encodedmessage + "e"
        elif letter == "4":
            encodedmessage = encodedmessage + "f"
        elif letter == "5":
            encodedmessage = encodedmessage + "g"
        elif letter == "6":
            encodedmessage = encodedmessage + "h"
        elif letter == "7":
            encodedmessage = encodedmessage + "i"
        elif letter == "8":
            encodedmessage = encodedmessage + "j"
        elif letter == "9":
            encodedmessage = encodedmessage + "k"
        elif letter == "0":
            encodedmessage = encodedmessage + "l"
        elif letter == " " and spaceSymbole == 1:
            encodedmessage = encodedmessage + "="
            spaceSymbole = 2
        elif letter == " " and spaceSymbole == 2:
            encodedmessage = encodedmessage + "?"
            spaceSymbole = 1

        else:
            print(
                text.darkred + "Sorry! One or more letter in your message could not be understood" + text.END)
            print(text.darkred + "You can only encode " + text.yellow + "alphabets" + text.darkred +
                  " and " + text.yellow + "numbers" + text.darkred + " with this encoder" + text.END)
            print(
                text.purple + "Please type your message again containing ONLY alphabets and letters" + text.END)
            continue

    print(text.green + "The encoding was successfull!")
    print("Your encoded message is: " + text.cyan + encodedmessage + text.END)


def decode():

    print(text.purple + "Make sure the message was encoded with this program only!")
    print(text.purple + "Message encoded in other way wont work")
    message = input(
        text.purple + "Enter the message you want to dencode: " + text.END)
    message = message.lower()
    decodedmessage = ""

    for letter in message:
        if letter == "m":
            decodedmessage = decodedmessage + "a"
        elif letter == "!":
            decodedmessage = decodedmessage + "b"
        elif letter == "n":
            decodedmessage = decodedmessage + "c"
        elif letter == "@":
            decodedmessage = decodedmessage + "d"
        elif letter == "o":
            decodedmessage = decodedmessage + "e"
        elif letter == "#":
            decodedmessage = decodedmessage + "f"
        elif letter == "p":
            decodedmessage = decodedmessage + "g"
        elif letter == "$":
            decodedmessage = decodedmessage + "h"
        elif letter == "q":
            decodedmessage = decodedmessage + "i"
        elif letter == "%":
            decodedmessage = decodedmessage + "j"
        elif letter == "r":
            decodedmessage = decodedmessage + "k"
        elif letter == "^":
            decodedmessage = decodedmessage + "l"
        elif letter == "s":
            decodedmessage = decodedmessage + "m"
        elif letter == "&":
            decodedmessage = decodedmessage + "n"
        elif letter == "t":
            decodedmessage = decodedmessage + "o"
        elif letter == "*":
            decodedmessage = decodedmessage + "p"
        elif letter == "u":
            decodedmessage = decodedmessage + "q"
        elif letter == "(":
            decodedmessage = decodedmessage + "r"
        elif letter == "v":
            decodedmessage = decodedmessage + "s"
        elif letter == ")":
            decodedmessage = decodedmessage + "t"
        elif letter == "w":
            decodedmessage = decodedmessage + "u"
        elif letter == "[":
            decodedmessage = decodedmessage + "v"
        elif letter == "x":
            decodedmessage = decodedmessage + "w"
        elif letter == "]":
            decodedmessage = decodedmessage + "x"
        elif letter == "y":
            decodedmessage = decodedmessage + "y"
        elif letter == "+":
            decodedmessage = decodedmessage + "z"
        elif letter == "c":
            decodedmessage = decodedmessage + "1"
        elif letter == "d":
            decodedmessage = decodedmessage + "2"
        elif letter == "e":
            decodedmessage = decodedmessage + "3"
        elif letter == "f":
            decodedmessage = decodedmessage + "4"
        elif letter == "g":
            decodedmessage = decodedmessage + "5"
        elif letter == "h":
            decodedmessage = decodedmessage + "6"
        elif letter == "i":
            decodedmessage = decodedmessage + "7"
        elif letter == "j":
            decodedmessage = decodedmessage + "8"
        elif letter == "k":
            decodedmessage = decodedmessage + "9"
        elif letter == "l":
            decodedmessage = decodedmessage + "0"
        elif letter == "=" or letter == "?":
            decodedmessage = decodedmessage + " "
        else:
            print(
                text.darkred + "Sorry! One or more letter in your message could not be understood" + text.END)
            print(decodedmessage)
            continue

    print(text.green + "The decoding was successfull!")
    print("Your decoded message is: " + text.cyan + decodedmessage + text.END)


start()
