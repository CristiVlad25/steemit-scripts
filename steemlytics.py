# thanks to @furion @bitcalm @xeroc and @trogdor for inspiring the code

from steemapi.steemnoderpc import SteemNodeRPC
rpc = SteemNodeRPC('ws://node.steem.ws')
from collections import Counter
import csv

# September 6 - beginning of the day - block 4718264
# September 12 - end of the day - block 4919136

voters = ['blocktrades', 'jamesc', 'smooth', 'dantheman', 'tombstone', 'summon',
            'steemed', 'rainman', 'wang', 'complexring', 'riverhead', 'roadscape',
            'nextgencrypto', 'silversteem', 'donkeypong', 'proskynneo', 'blackjack',
            'firstclass', 'enki', 'clayop', 'wackou', 'steemit200', 'kushed', 'xeldal',
            'arhag', 'fuzzyvest', 'pharesim', 'steempty', 'bitcube', 'onceuponatime', 'witnes.svk',
            'abit', 'berniesanders', 'ned', 'dan', 'val-a', 'itsascam', 'skywalker', 'smooth.witness',
            'datasecuritynode', 'au1nethyb1', 'bitcoin2016', 'analisa', 'paladin', 'satoshifund', 'alphabet',
            'excalibur', 'recursive', 'lafona-miner', 'badassmother', 'xeroc']

voterlst = []
authorlst = []
permlinklst = []

# parsing the blocks between Sept 6 - Sept 12 (end of day)

for i in range(4718264, 4919136):
    dys = rpc.get_block(i)['transactions']
    for tx in dys:
        for operation in tx['operations']:
            if operation[0] == 'vote' and operation[1]['voter'] in voters:
                voter = operation[1]['voter']
                author = operation[1]['author']
                permlink = operation[1]['permlink']


# we're looking for votes on posts, not on comments

                if permlink[:3] != "re-":
                    voterlst.append(voter)
                    authorlst.append(author)

voteCounts = Counter(voterlst)
authorCounts = Counter(authorlst)

# indexing results for voters (name + votes given)

writefileV = open('voterresults4.csv', 'w', newline='')
writerV = csv.writer(writefileV)

for vkey, vcount in voteCounts.items():
    writerV.writerow([vkey, vcount])

# indexing results for authors (name + votes received)

writefileA = open('authorresults4.csv', 'w', newline='')
writerA = csv.writer(writefileA)

for akey, acount in authorCounts.items():
    writerA.writerow([akey, acount])
