import tweetpy
import time

while True:
    content = tweetpy.main()
    tweetpy.tweet(content)
    print(content)
    time.sleep(60)