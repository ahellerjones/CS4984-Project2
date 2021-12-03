import praw
from psaw import PushshiftAPI

username = input("Enter username: ")
password = input("Enter password: ")
clientID = input("Please enter client ID: ")
clientSecret = input("Please enter client secret: ")

reddit = praw.Reddit(
    client_id=clientID,
    client_secret=clientSecret,
    user_agent="Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
    username=username,
    password=password
)
api = PushshiftAPI(reddit)

listOfSubs = []
for subredditor in reddit.subreddits.search("ivermectin"):
    listOfSubs.append(subredditor)
stuffFromSubs = []
for s in listOfSubs:
    print(s.url)
gen = api.search_comments(author='Plastic_Rock_4768', subreddit=str(listOfSubs[1].title), filter=['selftext'])
print(listOfSubs[1].title)
print(gen)
'''
    stuffFromSubs.append(s.search("Fauci"))
    for b in i:
        print(b)
'''