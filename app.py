from flask import Flask, render_template, request, jsonify
import os
from requests_oauthlib import OAuth1Session

app = Flask(__name__)

# Twitter API credentials
api_key = os.getenv('TWITTER_API_KEY')
api_key_secret = os.getenv('TWITTER_API_KEY_SECRET')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

# OAuth 1.0a Session
twitter = OAuth1Session(api_key,
                        client_secret=api_key_secret,
                        resource_owner_key=access_token,
                        resource_owner_secret=access_token_secret)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/post_tweet', methods=['POST'])
def post_tweet():
    tweet_content = request.form['content']
    url = "https://api.twitter.com/2/tweets"
    payload = {"text": tweet_content}
    response = twitter.post(url, json=payload)

    if response.status_code == 201:
        return jsonify({'message': 'Tweeted!'})
    else:
        return jsonify({'message': f'Error: {response.status_code} {response.text}'})

if __name__ == '__main__':
    app.run(debug=True)
