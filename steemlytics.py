# thanks to @furion @bitcalm @xeroc and @trogdor for inspiring the code

from steemapi.steemnoderpc import SteemNodeRPC
rpc = SteemNodeRPC('ws://node.steem.ws')
from collections import Counter
import csv

# August 30 - beginning of the day - block 4517262
# September 5 - end of the day - block 4718263

voters = ['blocktrades', 'jamesc', 'smooth', 'dantheman', 'tombstone', 'summon',
            'steemed', 'rainman', 'wang', 'complexring', 'riverhead', 'roadscape',
            'nextgencrypto', 'silversteem', 'donkeypong', 'proskynneo', 'blackjack',
            'firstclass', 'enki', 'clayop', 'wackou', 'steemit200','kushed', 'xeldal',
            'arhag','fuzzyvest','pharesim','steempty', 'bitcube','onceuponatime','witnes.svk'
            ,'abit','berniesanders']

voterlst = []
authorlst = []
permlinklst = []

for i in range(4517262, 4718263):         # parsing the blocks between Aug 29 - Sept 5 (end of day)
    dys = rpc.get_block(i)['transactions']
    for tx in dys:
        for operation in tx['operations']:
            if operation[0] == 'vote' and operation[1]['voter'] in voters:
                voter = operation[1]['voter']
                author = operation[1]['author']
                permlink = operation[1]['permlink']
                if permlink[:3] != "re-":      # we're looking for votes on posts, not on comments
                    voterlst.append(voter)
                    authorlst.append(author)

voteCounts = Counter(voterlst)
authorCounts = Counter(authorlst)

# indexing results for voters (name + votes given)

writefileV = open('voterresults.csv', 'w', newline='')
writerV = csv.writer(writefileV)

for vkey, vcount in voteCounts.items():
    writerV.writerow([vkey, vcount])

# indexing results for authors (name + votes received)

writefileA = open('authorresults.csv', 'w', newline='')
writerA = csv.writer(writefileA)

for akey, acount in authorCounts.items():
    writerA.writerow([akey, acount])
