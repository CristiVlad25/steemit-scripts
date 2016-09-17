# this would not have been possible without the amazing steemtools library
# so, thank you @furion

from steemtools.blockchain import Blockchain
from steemtools.base import Account, Post

b = Blockchain()

# getting the number of the current block and the start block
# the start block is current block minus ~24 hours

curr_block = b.get_current_block()
st_block = curr_block - 28800

# creating two lists, one will display results with duplicates
# the second list will be the clean one, without the duplicates
# removing duplicates could also be done with the set() function

postlist1 = []
postlist2 = []

# 'replaying' the blockchain for the timeframe established above
# filtering by comments (blogposts and comments)

for event in b.replay(start_block=st_block, end_block=curr_block, filter_by=['comment']):

    post = event['op']['permlink']
    author = event['op']['author']

# the meat of the code
# looking for blogposts from users with their first post in the last 24 hours
# for redundancy, I'm also displaying the results to the screen, in case something goes
# wrong and it doesn't get executed to the end
# the results diplayed on the screen are valid but they contain duplicates

    if post[:3] != 're-' and len(Account(author).get_blog())==1:

        try:
            if Post.time_elapsed(Account(author).get_blog()[0])/3600 < 24:
                print(Post.get_url(Account(author).get_blog()[0]))
                postlist1.append(Post.get_url(Account(author).get_blog()[0]))

        except:
            continue

# removing duplicates

for item in postlist1:
    if item not in postlist2:
        postlist2.append(item)

# writing the final results to file
# the file contains a list of links to posts of users who created their first blogpost
# in the last 24 hours

with open('newauthors.txt', 'wt') as f:
    for line in postlist2:
        f.write(line+'\n')

f.close()
