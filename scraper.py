#Beginning of the file. Need to learn how to use vim/change to sublime

# Created by Josh Bowman
# Tweet scraper for the NLP project

#Using tweepy to scrape the data
import tweepy
from tweepy import OAuthHandler

# The data will be stored in a csv file for use
import csv

# API authentication credentials
# Some more text on what they do
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

def scrapeTweets(username):
	# Twitter only allows access to a users most recent 3240 tweets with this method
	# Authorize twitter, intialize tweepy

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token = (access_token, access_secret)
	api = tweepy.API(auth)	

	# Create a list to hold all of the tweets
	tweet_list = []
	
	# Request for the most recent tweets, limit is 200
	new_tweets = api.user_timeline(screen_name = username, count = 200)
	
	# Add the newest tweets to the list
	tweet_list.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest_id = tweet_list[-1].id - 1
	
	# Loop through all of the tweets until there are no more left
	while len(new_tweets) > 0:
		
		new_tweets = api.user_timeline(screen_name = username,count=200,max_id=oldest_id)
		tweet_list.extend(new_tweets)
		oldest_id = tweet_list[-1].id - 1
	
	# Turn the list into a 2D array that will be used to populate the csv file
	output = [[tweet.text.encode("utf-8")] for tweet in tweet_list]
	
	# Write data to csv file
	with open('%s_tweets.csv' % username, 'wb') as file:
		writer = csv.writer(file)
		writer.writerow(["id","text"])
		writer.writerows(output)
	return

if __name__ == "__main__":
	username = raw_input("Enter a username to scrape tweets\n")
	scrapeTweets(username)
