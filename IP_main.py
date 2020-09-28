"""==========================================
                Import Section
 =========================================="""

import requests
import uuid
import pprint
import json
import os


"""==========================================
                Constant Declaration Section 
    =========================================="""

LINK = r'https://www.magetic.com/c/test?api=1&name=Ivan_Pyrog'

Storage_folder = r'C:\Users\Misha Dziuba\Documents\Ivan.Pyrog.test'

api = requests.get(LINK)

pp = pprint.PrettyPrinter( indent= 2) # Show-off for readable out put during testing ;-)


"""==========================================
                Class Declaration Section 
    =========================================="""

class API_Error_Exception (Exception):
    """Artificial Exception raised when API returns Error string"""
    pass


class Parser:
    """Main handler for requesting games list from the API, cleaning the raw input and counting the unique games"""
    
    
    games = {} # Store all the game names , dict key must be a unique record - helps to avoid duplication if API responds with the same games
    
    def data_cleaning(self)-> dict: 
        """Takes the semi-column separated string from the API response, splits into the list and later comprehends it into a dict with unique UUIDs"""
        try:
            self.game_list = self.raw_input.split(';')
            self.game_list = self.game_list[:6]  # Remove the empty string element
            self.game_dict = {item:str(uuid.uuid4()) for item in self.game_list}
        except API_Error_Exception:
            print('API Server is down')
        return self.game_dict


    def __init__(self, request: str):
        """Constructor method"""
        self.request = requests.get(request)
        if self.request.text[:5] != 'Error':
            self.raw_input = self.request.text
            self.games.update(self.data_cleaning())
        else:
            pass


"""===============================================================
                    Execution"""


os.chdir(Storage_folder)   # To store the json file in our folder location

test_one = Parser(LINK)


for item in range(1000):  # Intended to implement recursive while loop 
    test_one = Parser(LINK)

print ('-------------------------API--------------------------')
print (api.text, api.text[:5])
pp.pprint(test_one.games)
print()
pp.pprint(test_one.game_list)

with open('IP_test_output.json', 'w') as output_file:
    json.dump(test_one.games, output_file)