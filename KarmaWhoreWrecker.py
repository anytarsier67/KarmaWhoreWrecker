import praw
import prawcore
import random
import json
import threading
import time

with open('config.json', 'r') as f:
    data = json.load(f)
    account = data["account"]
    message = data["KarmaWhore"]["message"]

reddit = praw.Reddit(client_id = account["client_id"],
                     client_secret = account["client_secret"],
                     username = account["username"],
                     password = account["password"],
                     user_agent = account["user_agent"])

KarmaWhore = reddit.redditor(data["KarmaWhore"]["name"])

print(f"logged in to account: {account['username']}\nkarma whore is: {KarmaWhore}\nmessage is:\n\n{message}\n\n")

def Post_Reply(KarmaWhore, message):
    print('func')
    for post in KarmaWhore.stream.submissions(skip_existing=True):
        print(post)
        if post.archived == False:
            if post.locked == False:
                try:
                    post.downvote()
                    post.reply(message)
                    print(f"sleeping after reply and downvote.")
                    time.sleep(random.randint(30, 60))
                except prawcore.exceptions.Forbidden:
                    print("locked, passing...")
                    time.sleep(random.randint(1, 10))
                except Exception as e:
                    print(e)
                    time.sleep(random.randint(1, 10))
            else:
                time.sleep(random.randint(1, 10))    
        else:
            time.sleep(random.randint(1, 10))
    print('func -_O')

def Comment_DownVote(KarmaWhore):
    print('func 2')
    for comment in KarmaWhore.stream.comments(skip_existing=True):
        if comment.archived == False:
            if comment.locked == False:
                try:
                    comment.downvote()
                    print("downvoted comment.")
                except Exception as e:
                    print(e)
                time.sleep(random.randint(1, 10))
            else:
                time.sleep(random.randint(1, 5))
        else:
            time.sleep(random.randint(1, 5))
    print('func2 -_O')


comment_thread = threading.Thread(target=Comment_DownVote, args=(KarmaWhore,))
post_thread = threading.Thread(target=Post_Reply, args=(KarmaWhore, message))

comment_thread.start()
post_thread.start()

while True:
    pass


