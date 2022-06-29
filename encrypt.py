# Modules
from random import seed, randint, shuffle

# Read an input
input = input()

# Allowed characters
char = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'á', 'é', 'í',
    'ó', 'ú', 'ü',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Á', 'É', 'Í',
    'Ó', 'Ú', 'Ü',
    '1', '2', '3', '4', '5', '6', '7', '8' ,'9', '0',
    ' ', ',', '.', '¡', '!', '¿', '?'
]

# Create a seed to known how to shuffle characters
seed_int = randint(1, 1000000)
seed_str = str(seed_int)
while len(seed_str) < 7:
    seed_str = '0' + seed_str

# Create a new list whith character position chanted
seed(seed_int)
char_shuffle = char[:]
shuffle(char_shuffle)
print(char)
print(char_shuffle)

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
print(output)