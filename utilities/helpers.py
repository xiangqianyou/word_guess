import requests
import json
from functools import wraps
from flask import redirect, session
import re

def get_word(length=None):
    try:
        api_url = 'https://random-word-api.vercel.app/api?words=1'
        if length:
            api_url += f"&length={length}"
        response = requests.get(api_url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    return json.loads(response.text)


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def contains_numbers(string):
    return bool(re.search(r'\d',string))