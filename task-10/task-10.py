import tweepy
import tokens
# OAuth authentication
auth = tweepy.OAuthHandler(tokens.consumer_key, tokens.consumer_secret)
auth.set_access_token(tokens.access_token, tokens.access_token_secret)
# Create an API object
api = tweepy.API(auth)
# Get the message to tweet from the user
message = input("Enter the message to tweet: ")
# Update the status with the message
api.update_status(message)
print("Tweet sent successfully!")