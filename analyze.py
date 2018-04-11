import sys
import praw
import json
users = []
submissions = []

f = open("password_and_cs.txt")
password = f.readlines()[0]
client_secret = f.readlines()[1]
r = praw.Reddit(
	user_agent='analysis',
    client_id='uWunFaORo5NzEA', 
    client_secret=client_secret,
    username='mjjjokes',
    password=password
)

subreddit = r.subreddit(sys.argv[1])
#get submission object ids
for i,submission in enumerate(subreddit.hot(limit=50)):
	print 'getting submission object %s' % (i)
	submissions.append(r.submission(
		id=submission.id))

comments = []
for i,s in enumerate(submissions):
	if s.author.name not in users:
		users.append(s.author.name)
	print 'getting users for commenters in submission %s of %s' % (
		i, len(submissions))
	for c in s.comments.list():
		try:
			if c.author.name not in users:
				#get user of each comment in thread
				users.append(c.author.name)
		except:
			print 'Nonetype object has no attribute name'
		
kb_submissions = {}
kb_comments = {}
for idx,username in enumerate(users):
	try:
		print 'getting info for %s, %s of %s' % (username,idx,len(users))
		user = r.redditor(username)
		submissions = user.submissions.new(limit=None)
		comments = user.comments.new(limit=None)
		for s in submissions:
			subreddit = s.subreddit.display_name
			kb_submissions[subreddit] = (
				kb_submissions.get(subreddit, 0) + 1
			)
		for c in comments:
			subreddit = c.subreddit.display_name
			kb_comments[subreddit] = (
				kb_comments.get(subreddit, 0) + 1
			)
	except:
		print 'user deleted'

karma_by_subreddit = {
	'submissions':kb_submissions,
	'comments':kb_comments,
	'users':users,
}
#save object to disk as json 
with open('data.json','w') as fp:
	json.dump(karma_by_subreddit,fp)
