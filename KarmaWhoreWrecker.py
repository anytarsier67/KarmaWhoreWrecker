import asyncprawcore
import asyncpraw
import asyncio
import random

reddit = asyncpraw.Reddit(client_id = "--client-id-here--",
                     client_secret = "--client-secret-here--",
                     username='--bot-username-here--',
                     password='--bot-password-here--',
                     user_agent = " --user-agent-here--")

async def Post_Reply():
    num = 0
    KarmaWhore = await reddit.redditor('Callusedthenics')
    async for post in KarmaWhore.stream.submissions(skip_existing=True):
        if post.archived == False:
            if post.locked == False:
                try:
                    await post.downvote()
                    await post.reply("--message-here--")
                    num += 1
                    with open("list.txt","a") as f:
                        f.writelines(f"{post.url} | {post.id} | {post.permalink} | {post.created_utc}\n")

                    print(f"sleeping after reply number: {num}")
                    await asyncio.sleep(random.randint(30, 60))
                except asyncprawcore.exceptions.Forbidden:
                    print("locked??? passing...")
                    await asyncio.sleep(random.randint(1, 10))
                except Exception as e:
                    print(f"uh oh :( , traceback: \n\n {e}")
                    await asyncio.sleep(random.randint(1, 10))
            else:
                await asyncio.sleep(random.randint(1, 10))    
        else:
            await asyncio.sleep(random.randint(1, 10))
                
async def Comment_DownVote():
    num = 0
    KarmaWhore = await reddit.redditor('Callusedthenics')
    async for comment in KarmaWhore.stream.comments(skip_existing=True):
        if comment.archived == False:
            if comment.locked == False:
                try:
                    await comment.downvote()
                    num += 1
                    print(f"downvoted! (comment) {num}")
                except Exception as e:
                    print(f"uh oh :( , traceback: \n\n {e}")
                await asyncio.sleep(random.randint(1, 10))
            else:
                await asyncio.sleep(random.randint(1, 5))
        else:
            await asyncio.sleep(random.randint(1, 5))

        
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(Post_Reply(), Comment_DownVote()))
loop.close()
print("exit")


