# thanks @furion for the tip

from steemapi.steemnoderpc import SteemNodeRPC
rpc = SteemNodeRPC('ws://node.steem.ws')
import csv

allauthors = rpc.lookup_accounts('', 1000000)
postdict = dict()
repdict = dict()
rewdict = dict()

# counting author posts and adding them to the postdict dictionary
# retrieving authors with more than 700 posts (blogposts and comments)

for author in allauthors:
    postcount = rpc.get_account(author)['post_count']
    if postcount > 700:
        postdict[author] = postcount

# retrieving reputation and post rewards for the authors in postdict

for author2 in postdict.keys():
    repcount = rpc.get_account(author2)['reputation']
    rewcount = rpc.get_account(author2)['posting_rewards']
    repdict[author2] = repcount
    rewdict[author2] = rewcount

# indexing results for posts

writefile1 = open('productivesteemians-posts.csv', 'w', newline='')
writer1 = csv.writer(writefile1)

for pauth, pcount in postdict.items():
    writer1.writerow([pauth, pcount])

# indexing results for reputation

writefile2 = open('productivesteemians-rep.csv', 'w', newline='')
writer2 = csv.writer(writefile2)

for rpauth, rpcount in repdict.items():
    writer2.writerow([rpauth, rpcount])

# indexing results for rewards

writefile3 = open('productivesteemians-rew.csv', 'w', newline='')
writer3 = csv.writer(writefile3)

for rwauth, rwcount in rewdict.items():
    writer3.writerow([rwauth, rwcount])
