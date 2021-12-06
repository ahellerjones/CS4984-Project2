# CS4984-Project2

This project utilises Python3, PyQt5, PRAW, and PSAW

```bash
pip install PyQt5
pip install praw
pip install psaw 
```


`python3 app.py` shows an example of the main screen
`python3 app3.py` shows an example of a display of relevant users. 
`python3 RedditStuff.py` shows an example of querying PRAW and serves as the back end
for our project

This tool has three main modes. The first mode is the search for subreddits based on a search term, or terms, provided. The second feature is user search.
This allows for the investigator to see information that isnt noramlly found about a user, such as when the account was created, if it has a verified email, and more.
The last feeature is an overlap counter of users using multiple subreddits. An example is if I wanted to know who in the VT Corps of Cadets was on Reddit I could choose
to search for 'VirginiaTech', 'VTCC', and 'ROTC' and it will create a users.txt file of who is uses all of them or just two of them.

Mode 3 is from https://github.com/Watchful1