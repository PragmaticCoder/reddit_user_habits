import sys
import json
import csv
from collections import OrderedDict

sorted_subms = {}
sorted_comnts = {}
with open(sys.argv[1],'r') as fp:
	data = json.load(fp)

submissions = data['submissions']
comments = data['comments']
users = data['users']

defaults = ['announcements','art','askreddit','askscience','aww','blog','books','creepy','dataisbeautiful','diy','documentaries','earthporn','explainlikeimfive','food','funny','futurology','gadgets','gaming','getmotivated','gifs','history','iama','internetisbeautiful','jokes','lifeprotips','listentothis','mildlyinteresting','movies','Music','news','nosleep','nottheonion','oldschoolcool','personalfinance','philosophy','photoshopbattles','pics','science','showerthoughts','space','sports','television','tifu','todayilearned','upliftingnews','videos','worldnews']

sorted_subms = OrderedDict(
	sorted(submissions.items(), key=lambda x: x[1]))
print sorted_subms

sorted_cmnts = OrderedDict(
	sorted(comments.items(), key=lambda x: x[1]))
print sorted_comnts

#to csv
subm_writer = csv.writer(open('submissions.csv', 'wb'))
for key, value in sorted_subms.items():
   	subm_writer.writerow([key, value])

subm_writer2 = csv.writer(open('nd_submissions.csv', 'wb'))
for key, value in sorted_subms.items():
	if key.lower() not in defaults:
   		subm_writer2.writerow([key, value])

cmnt_writer = csv.writer(open('comments.csv', 'wb'))
for key, value in sorted_cmnts.items():
   	cmnt_writer.writerow([key, value])

cmnt_writer2 = csv.writer(open('nd_comments.csv', 'wb'))
for key, value in sorted_cmnts.items():
	if key.lower() not in defaults:
   		cmnt_writer2.writerow([key, value])



usrs_writer = csv.writer(open('users.csv','wb'))
for u in users:
	usrs_writer.writerow([u])