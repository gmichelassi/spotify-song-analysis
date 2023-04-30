from dotenv import load_dotenv
from flask import Flask, redirect
from services.spotify import get_authentication_query_params, get_authentication_url
from services.utils import build_url_args_from_dict


app = Flask(__name__)
load_dotenv()


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'


@app.route('/spotify_authentication')
def spotify_authentication():
    query_params = get_authentication_query_params('http://localhost:5000/')
    url_args = build_url_args_from_dict(query_params)
    auth_url = get_authentication_url(url_args)

    return redirect(auth_url)
