# File: EnigmaRotor.py

from EnigmaConstants import ALPHABET

def apply_permutation(letter, permutation, offset):

    index = ALPHABET.find(letter)
    rotor_index = (index + offset) % 26
    
    new_char = permutation[rotor_index]
    new_char_index = ALPHABET.find(new_char)

    final_char_index = (new_char_index - offset) % 26
    return ALPHABET[final_char_index]



def invert_key(permutation):

    # Dictionary that enumerates on each permutation's letter
    # Key: permutation letter's corresponding index in the Alphabet  
    # Value: permutation letter's index in the Alphabet
    # Example: {16: 'A', 22: 'B', 4: 'C', 17: 'D', 19: 'E', 24: 'F', 20: 'G' ...}
    index_to_char_dict = {ALPHABET.find(letter): ALPHABET[i] for i, letter in enumerate(permutation)}
    inverted_key_list = [index_to_char_dict[i] for i in range(len(ALPHABET))]
    return ''.join(inverted_key_list)
    
class EnigmaRotor:

    def __init__(self, initial_permutation):
        self._r_l_permutation = initial_permutation
        self._l_r_permutation = invert_key(initial_permutation)
        self._offset = 0

    def get_offset(self):
        return self._offset
    
    def get_r_l_permutation(self):
        return self._r_l_permutation
    
    def get_l_r_permutation(self):
        return self._l_r_permutation
    
    def advance(self):

        self._offset += 1

        # Reset once full revolution
        if self._offset > 25 :
            self._offset = 0
    
    
    