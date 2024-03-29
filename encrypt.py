def encrypt (input):
    # Modules
    from random import seed, randint, shuffle
    
    # Allowed characters
    from characters import char
    
    # Create a seed to known how to shuffle characters
    seed_int = randint(1, 1000000)
    seed_str = str(seed_int)
    while len(seed_str) < 7:
        seed_str = '0' + seed_str
    
    # Create a new list whith character position chanted
    seed(seed_int)
    char_shuffle = char[:]
    shuffle(char_shuffle)
    
    # Create a new output with encryption
    output = ''
    for i in input:
        if i in char:
            position = char.index(i)
            new_character = char_shuffle[position]
            output = output + new_character
        else:
            output = output + i
    
    # Add the seed to the output (at the begining)
    output = seed_str + output
    
    # Return output
    return(output)