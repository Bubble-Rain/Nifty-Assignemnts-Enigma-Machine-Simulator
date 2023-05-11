# File: EnigmaRotor.py

from EnigmaConstants import ALPHABET

def apply_permutation(letter, permutation, offset):

    index = ALPHABET.find(letter)
    rotor_index = (index + offset) % 25
    
    new_char = permutation[rotor_index]
    new_char_index = ALPHABET.find(new_char)

    final_char_index = (new_char_index - offset) % 25 
    return ALPHABET[final_char_index]
    
class EnigmaRotor:

    def __init__(self, initial_permutation):
        self._permutation = initial_permutation
        self._offset = 0

    def get_offset(self):
        return self._offset
    
    def get_permutation(self):
        return self._permutation
    
    def advance(self):

        self._offset += 1

        # Reset once full revolution
        if self._offset > 25 :
            self._offset = 0
    
    
    