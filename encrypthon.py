# This is the main code

# Modules
from turtle import back
from colorama import init, Fore
from cover import cover
from encrypt import encrypt
from decrypt import decrypt

# Initialize the program
init(convert = True)
print(Fore.RED + cover)

# Execute the program
election = 10
while election != "0" :
    print(Fore.WHITE +
        "What do you want? (type the number and press 'Enter')")
    print(Fore.YELLOW +
        "    1: ",
        end = "")
    print(Fore.WHITE +
        "Encrypt")
    print(Fore.YELLOW +
        "    2: ",
        end = "")
    print(Fore.WHITE +
        "Decrypt")
    print(Fore.YELLOW +
        "    0: ",
        end = "")
    print(Fore.WHITE +
        "Exit")
    
    options = ["1", "2", "0"]

    print(Fore.YELLOW + "> ", end = "")
    print(Fore.WHITE + "", end = "")
    election = input()

    
    
    ##################
    # Error checking #
    ##################

    if len(election) > 1:
        print(Fore.RED + "Error 1: ", end = "")
        print(Fore.WHITE + "option not available\n")
        print(Fore.RESET + "     -----+-----+-----\n")

    elif options.count(election) == 0:
        print(Fore.RED + "Error 2: ", end = "")
        print(Fore.WHITE + "option not available\n")
        print(Fore.RESET + "     -----+-----+-----\n")

    else:



        #####################
        # Program execution #
        #####################

        if election == "1":
            print(Fore.YELLOW +
            "\nMessage encryption"
            )

            print(Fore.WHITE +
                "\n" +
                "What is your message?")
            print(Fore.YELLOW + "> ", end = "")
            print(Fore.WHITE + "", end = "")
            input_1 = input()
            output_1 = encrypt(input_1)

            print(Fore.YELLOW +
            "\nEncrypted message:"
            )
            print(Fore.CYAN + output_1)
            print(Fore.RESET + "\n     -----+-----+-----\n")
        
        elif election == "2":
            print(Fore.YELLOW +
            "\nMessage decryption"
            )
            
            print(Fore.WHITE +
                "\n" +
                "What is your encrypted message?")
            print(Fore.YELLOW + "> ", end = "")
            print(Fore.WHITE + "", end = "")
            input_2 = input()
            output_2 = decrypt(input_2)

            print(Fore.YELLOW +
            "\nDecrypted message:"
            )
            print(Fore.CYAN + output_2)
            print(Fore.RESET + "\n     -----+-----+-----\n")

