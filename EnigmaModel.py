# File: EnigmaModel.py

""" This is the starter file for the Enigma project. """

import EnigmaConstants
import string

from EnigmaView import EnigmaView
from EnigmaRotor import EnigmaRotor, apply_permutation

class EnigmaModel:

    def __init__(self):
        """Creates a new EnigmaModel with no views."""
        self._views = [ ]
        self._key_pressed_dict = dict.fromkeys(string.ascii_uppercase, 0)
        self._lamp_on_dict = dict.fromkeys(string.ascii_uppercase, 0)
        self._rotors = [EnigmaRotor(EnigmaConstants.ROTOR_PERMUTATIONS[i]) for i in range(3)]
        self._rotors.append(EnigmaRotor(EnigmaConstants.REFLECTOR_PERMUTATION))

    def add_view(self, view):
        """Adds a view to this model."""
        self._views.append(view)

    def update(self):
        """Sends an update request to all the views."""
        for view in self._views:
            view.update()

    def is_key_down(self, letter):
        return self._key_pressed_dict[letter]

    def is_lamp_on(self, letter):
        return self._lamp_on_dict[letter]
    
    def get_encrypted_key(self, letter, is_key_press):

        reflection_rotor = self._rotors[3]
        fast_rotor = self._rotors[2]
        medium_rotor = self._rotors[1]
        slow_rotor = self._rotors[0]

        """
        if is_key_press:
            
            fast_rotor.advance()
            fast_rotor_offset = fast_rotor.get_offset()

            print(fast_rotor_offset)
            print(self._rotors[2].get_offset())

            if fast_rotor_offset == 0:

                medium_rotor.advance()
                medium_rotor_offset = medium_rotor.get_offset()

                if medium_rotor_offset == 0:

                    slow_rotor.advance()
        """

        # Right to left encryption
        fast_letter = apply_permutation(letter, fast_rotor.get_r_l_permutation(), fast_rotor.get_offset())
        medium_letter = apply_permutation(fast_letter, medium_rotor.get_r_l_permutation(), medium_rotor.get_offset())
        slow_letter = apply_permutation(medium_letter, slow_rotor.get_r_l_permutation(), slow_rotor.get_offset())


        reflection_letter = apply_permutation(slow_letter, reflection_rotor.get_r_l_permutation(), reflection_rotor.get_offset())

        # Left to right encryption
        slow_letter = apply_permutation(reflection_letter, slow_rotor.get_l_r_permutation(), slow_rotor.get_offset())
        medium_letter = apply_permutation(slow_letter , medium_rotor.get_l_r_permutation(), medium_rotor.get_offset())
        fast_letter = apply_permutation(medium_letter, fast_rotor.get_l_r_permutation(), fast_rotor.get_offset())
        

        return fast_letter

    def key_pressed(self, letter):
        self._key_pressed_dict[letter] = True
        encrypted_letter = self.get_encrypted_key(letter, True)
        self._lamp_on_dict[encrypted_letter] = True
        self.update()

    def key_released(self, letter):
        self._key_pressed_dict[letter] = False
        encrypted_letter = self.get_encrypted_key(letter, False)
        self._lamp_on_dict[encrypted_letter] = False
        self.update()

    def get_rotor_letter(self, index):
        rotor_offset = self._rotors[index].get_offset()
        return EnigmaConstants.ALPHABET[rotor_offset]

    def rotor_clicked(self, index):
        self._rotors[index].advance()
        self.update()

def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

# Startup code

if __name__ == "__main__":
    enigma()
