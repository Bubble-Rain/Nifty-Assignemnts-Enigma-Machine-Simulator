# File: EnigmaModel.py

""" This is the starter file for the Enigma project. """

import EnigmaConstants
import string

from EnigmaView import EnigmaView
from EnigmaRotor import EnigmaRotor

class EnigmaModel:

    def __init__(self):
        """Creates a new EnigmaModel with no views."""
        self._views = [ ]
        self._key_pressed_dict = dict.fromkeys(string.ascii_uppercase, 0)
        self._lamp_on_dict = dict.fromkeys(string.ascii_uppercase, 0)

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

    def key_pressed(self, letter):
        self._key_pressed_dict[letter] = True
        self._lamp_on_dict[letter] = True
        self.update()

    def key_released(self, letter):
        self._key_pressed_dict[letter] = False
        self._lamp_on_dict[letter] = False
        self.update()

    def get_rotor_letter(self, index):
        return "A"          # In the stub version, all rotors are set to "A"

    def rotor_clicked(self, index):
        # You need to fill in this code
        self.update()

def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)

    print(EnigmaConstants.ALPHABET) 
    model.add_view(view)

# Startup code

if __name__ == "__main__":
    enigma()
