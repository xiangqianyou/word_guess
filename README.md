# Word Guess Game

#### Description:
Word Guess Game is a web application that allows users to play a guessing game where they have to guess a randomly generated word or a word from their own list. The user has to guess the word letter by letter, and they have a limited number of tries to guess the word correctly.

#### About the web app
This is a Flask application that includes a login system and a feature for saving word lists. Users can use the application to produce random words, add words to a list, delete words from the list, and see their saved word lists. To access the saved word list feature, users must first register and log in. The saved words are stored in a SQLite database, and user data is saved using Flask session. Additionally, the application uses Flask-SQLAlchemy to interact with the SQLite database and the Werkzeug security module to hash and verify user passwords.

#### Getting Started
There are two ways to get started with the Word Guess Game:

A. Clone the Repository to Your Local Machine
1. Download or clone the repository to your local machine.
2. Make sure you have Python installed on your machine to run the application.
3. Open your terminal and navigate to the directory where you cloned the repository.
4. Run the command `pip install -r requirements.txt` to install the required dependencies.
5. Set the FLASK_SECRET_KEY environment variable by running the command `export FLASK_SECRET_KEY=mysecretkey`. This is used by Flask to sign session cookies and should be kept secret.
6. Start the Flask server by running the command `flask run`.
7. The application will be available at http://127.0.0.1:5000/ in your web browser.

B. Run the Docker Container in Your Local Machine
1. Make sure you have Docker installed on your machine.
2. Pull the Docker image by running the command `docker pull xiangqianyou/word_guess`.
3. Start the Docker container by running the command `docker run -e FLASK_SECRET_KEY=mysecretkey -p 5000:5000 xiangqianyou/word_guess`.
4. The application will be available at http://127.0.0.1:5000/ in your web browser.

#### How to Play
When you first open the application, you will be presented with two options - to generate a random word or to pull a word from your own list. If you choose to generate a random word, you can optionally specify the length of the word by entering a number between 3 and 9 in the text box provided.

Once you have chosen your word, you will see a series of blank spaces representing the letters of the word. You can click on the letters below the blank spaces to guess the letters of the word. If the letter you guess is in the word, it will be revealed in the appropriate blank space. If it is not in the word, you will lose a try. You have 8 tries in total.

If you correctly guess all the letters of the word before running out of tries, you will win the game. Otherwise, you will lose and the word will be revealed.

In addition, you can store words and view them, as well as add your own words to your list. On the word list page, you can hover over a word to display its definition without leaving the page, or check the full definition by opening a new page. You can also remove words from your saved list once you have mastered them.
