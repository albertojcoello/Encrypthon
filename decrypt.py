def decrypt (input):
    # Modules
    from random import seed, shuffle
    
    # Indentify the seed (the seven first characters)
    seed_raw = input[0:7]
    seed_int = int(seed_raw)
    
    # Allowed characters
    from characters import char
    
    # Create a new list whith character position chanted
    seed(seed_int)
    char_shuffle = char[:]
    shuffle(char_shuffle)
    
    # Create a new output with encryption
    output = ''
    for i in input:
        if i in char:
            position = char_shuffle.index(i)
            new_character = char[position]
            output = output + new_character
        else:
            output = output + i
    
    # Delete the seed in the output
    output = output[7:len(output)]
    
    # Return output
    return(output)