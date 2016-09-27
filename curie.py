# thank you @furion for the amazing steemtools library

from steemtools.blockchain import Blockchain
from steemtools.base import Account, Post
from datetime import datetime

b = Blockchain()
ac = Account

# getting the number of the current block and the start block
# the start block is current block minus ~20 hours

curr_block = b.get_current_block()
st_block = curr_block - 24000

# creating two lists, one will display results with duplicates
# the second list will be the clean one, without the duplicates
# removing duplicates could also be done with the set() function

postlist1 = []
postlist2 = []

# 'replaying' the blockchain, starting 20 hours ago and ending ~6 hours ago
# filtering by comments (blogposts and comments)

for event in b.replay(start_block=st_block, end_block=curr_block - 7200, filter_by=['comment']):

    post = event['op']['permlink']
    author = event['op']['author']
    reputation = ac(author).reputation()
    steem = ac(author).get_sp()
    followers = ac(author).get_followers()

# looking for blogposts from authors with reputation < 60, steem power < 3000 and
# 100 or fewer followers

    if post[:3] != 're-' and reputation < 60 and steem < 3000 and len(followers) < 100:

# looking into their blogs and retrieving the last 4 blogposts
# if the post has a payout of 10 SBD or less and is posted in the desired timeframe
# give me the link

        blog = ac(author).get_blog()
        for post in blog[:4]:
            payout = Post.payout(post)
            timeEl = Post.time_elapsed(post)/60
            if payout < 10 and timeEl > 360 and timeEl < 1200:

                try:
                    print(Post.get_url(post))
                    postlist1.append(Post.get_url(post))

                except:
                    continue

# removing duplicates

for item in postlist1:
    if item not in postlist2:
        postlist2.append(item)

# writing the final results to file
# the file contains a list of links to posts that meet the desired criteria

with open('curie.txt', 'wt') as f:
    for line in postlist2:
        f.write(line+'\n')

f.close()
