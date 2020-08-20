##What tags generate the most comments/votes/views?

import json
from collections import Counter
with open ('/Users/xiaogo627301968qq.com/exercise1/xhamster.json') as f:
    data = json.load(f)

alltages=[]
i = 0
for identifyer,clip in data.items():
    i += 1
    alltages.extend(clip["channels"])

print(len(alltages),"tags have been used to describe the",i,"different videos")
print("Thus, we have an average of",len(alltages)/i,"tags per video")
c= Counter(alltages)
print(c.most_common(100))

alldescribtions = []
i = 0
for identifyer, clip in data.items():
    i += 1
    alldescribtions.extend(clip["nb_comments"])
print(len(alldescribtions),"descriptions have been used to describe the",i,"different videos")
print("Thus, we have an average of",len(alldescribtions)/i,"tags per video")
