import tweepy
import token
# OAuth authentication
auth = tweepy.OAuthHandler(token.consumer_key, token.consumer_secret)
auth.set_access_token(token.access_token, token.access_token_secret)
# Create an API object
api = tweepy.API(auth)
# Get the message to tweet from the user
message = input("Enter the message to tweet: ")
# Update the status with the message
api.update_status(message)
print("Tweet sent successfully!")