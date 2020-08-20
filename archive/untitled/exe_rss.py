import requests
import json

print(1)
print(1)

base_url = 'https://www.rijksmuseum.nl/api/pages/en/{}?key={}&format=json'
page_of_interest = 'whats-on/exhibitions-past' ##how to find the page
key = 'rap2CN14'

full_url = base_url.format(page_of_interest, key)

r = requests.get(full_url)
print("Response HTTP Status Code: {status_code}".format(status_code=r.status_code))

data = json.loads(r.content.decode('utf-8'))
for item in data['contentPage']['overviewItems'][:10]:
    print("Title:{}".format(item['page']['title']))
    print('Date:{}'.format((item['text'])))
    print('URL:{}'.format(item["page"]["url"]))

from collections import defaultdict
import dateutil.parser

counts = defaultdict(int)

for item in data['contentPage']['overviewItems']:
    end_date = ' '.join(item['text'].split(' ')[-3:]) ###?
    dt = dateutil.parser.parse(end_date)
    counts[dt.year] += 1

print(counts)
