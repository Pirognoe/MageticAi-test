Date: 28/09/2020;
Author: Ivan Pyrog;
===============================================================================

To execute the script run the "python IP_main.py" command from the command line
 (or execute the script in any IDE avaliable).

The requirements are listed in the corresponding text file created via "pip freeze" command.

===============================================================================

To guarantee that no duplicates are present in our games list - we store them in
a standard Python dictionary as keys, generating UUIDs as values.

Assumption made regarding polling the games from API: 
We iterate and request new game names from API until any update is made to our
main game dictionary, i.e. games.keys() does not contain all of the 6 elements 
returned in response from the API.

The results will be printed in the terminal window and stored as a json file in
the project folder.