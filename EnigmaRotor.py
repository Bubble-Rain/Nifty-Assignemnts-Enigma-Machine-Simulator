# File: EnigmaRotor.py

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
    