# Word Guess Game

#### Description:
Word Guess Game is a web application that allows users to play a guessing game where they have to guess a randomly generated word or a word from their own list. The user has to guess the word letter by letter, and they have a limited number of tries to guess the word correctly.

#### About the web app
This is a Flask application that includes a login system and a feature for saving word lists. Users can use the application to produce random words, add words to a list, delete words from the list, and see their saved word lists. To access the saved word list feature, users must first register and log in. The saved words are stored in a SQLite database, and user data is saved using Flask session. Additionally, the application uses Flask-SQLAlchemy to interact with the SQLite database and the Werkzeug security module to hash and verify user passwords.

#### Getting Started
To get started with the Word Guess Game, simply download or clone the repository to your local machine. You will need to have Python installed on your machine to run the application.

Once you have the repository on your local machine, navigate to the directory in your terminal and run the following command:
```
1. pip install -r requirements.txt
2. export FLASK_SECRET_KEY=mysecretkey
3. flask run
```

(Note that in step 2, you need to set the FLASK_SECRET_KEY environment variable to run the Flask app locally. This is used by Flask to sign session cookies and should be kept secret.)

This will start the Flask server and the application will be available at http://localhost:5000/ in your web browser.

#### How to Play
When you first open the application, you will be presented with two options - to generate a random word or to pull a word from your own list. If you choose to generate a random word, you can optionally specify the length of the word by entering a number between 3 and 9 in the text box provided.

Once you have chosen your word, you will see a series of blank spaces representing the letters of the word. You can click on the letters below the blank spaces to guess the letters of the word. If the letter you guess is in the word, it will be revealed in the appropriate blank space. If it is not in the word, you will lose a try. You have 8 tries in total.

If you correctly guess all the letters of the word before running out of tries, you will win the game. Otherwise, you will lose and the word will be revealed.

In addition, you can store words and view them, as well as add your own words to your list. On the word list page, you can hover over a word to display its definition without leaving the page, or check the full definition by opening a new page. You can also remove words from your saved list once you have mastered them.
