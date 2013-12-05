import oauth2 as oauth
import time

#API
url = https://api.twitter.com/1.1/search/tweets.json

params = {
    'oauth_version': "1.0",
    'oauth_nonce': oauth.generate_nonce(),
    'oauth_timestamp': int(time.time())
    'user': 'joestump'
}

token = oauth.Token(key="tok-test-key", secret="tok-test-secret")
consumer = oauth.Consumer(key="con-test-key", secret="con-test-secret")

# Set our token/key parameters
params['oauth_token'] = tok.key
params['oauth_consumer_key'] = con.key

req = oauth.Request(method="GET", url=url, parameters=params)
