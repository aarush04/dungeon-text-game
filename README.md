# group-project-readme

Introduction : Our project for this class is a text-game based called Dungeon. Dungeon is a game that can be played on a browser with a simple UI. It follows an encapsulating storyline, as the user makes choices that effect the outcome of the game in real-time.

Technical Architecture : The backend for this project was written in Python. We have different states each as their own Python class with different paths the user can take, stored in the Game State object. The users data is stored in the Player State object. This is all routed to app.py file which handles the game and uses Flask to create the API GET and POST requests. The GameState has variable 'current_prompt' that is read to the user in GET requests, and takes in a user_input as an argument to the Gamestate to update the current state in POST requests. We tested this API with PostMan. We also did some testing on the logic of the game with Pytest. \
The frontend used JS, CSS, and HTML. We serve the html file to the local host for testing. We use fetch function in the JS function to handle the REST API requests. \
<img width="1164" alt="Screenshot 2023-12-04 at 12 24 52 PM" src="https://github.com/CS222-UIUC-FA23/group-project-team60/assets/70361763/6b38a9f9-4050-4f1a-a602-d9c0105fc37b">


Group Members and Roles :

Daniel Dilan, Minh Cao, Aarush Shah

1. Backend : Python and Pytest - Minh and Aarush
2. API : Flask/PostMan - Daniel, Minh
3. Frontend : HTML/CSS/JS - Daniel, Aarush

Installation :

Prerequisites: Python3, required libraries, VSCode Live Preview \
To play the game on localhost, after cloning the repo follow these steps: \
Since we are in the process of integrating the game from terminal to API, you have to checkout the `frontend_and_backend` branch. \
Then in the project directory in the terminal, run `python3 app.py` \
Then you can go to the frontend and click `index.html`. Using Live Preview, select `Open with Live Server` which will open the local host on your browser. \
Then the project will be working and you can play the game. If not, check where the backend is running (i.e. `http://127.0.0.1:5000`), and make sure the base urls of the endpoints match up in the `frontend/script.js` file. 

Future work :
If we were to continue working on the project, we would expand the story and include more states, riddles, and games, as well as improve the UI and have the player state constantly showing or add images to responses.
