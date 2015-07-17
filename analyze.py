import sys
import praw
import json
users = []
submissions = []
r = praw.Reddit(user_agent='subreddit_analysis')
subreddit = r.get_subreddit(sys.argv[1])
#get submission object ids
for i,submission in enumerate(subreddit.get_hot(limit=3)):
	print 'getting submission object %s' % (i)
	submissions.append(r.get_submission(
		submission_id=submission.id))
root_comments = []
for i,s in enumerate(submissions):
	print 'getting comments %s of %s' % (
		i, len(submissions))
	for c in s.comments:
		root_comments.append(c)
def get_comments(comments,level):
	for i,c in enumerate(comments):
		try:
			print 'getting comment count: %s in level %s' % (
				i,level)
			if c.author.name not in users:
				users.append(c.author.name)
		except AttributeError:				
			print 'nada'
		if hasattr(c,'replies'):
			level += 1
			get_comments(c.replies,level)
		
get_comments(root_comments,0)
kb_submissions = {}
kb_comments = {}
for idx,username in enumerate(users):
	try: 
		print 'getting info for %s, %s of %s' % (username,idx,len(users))
		user = r.get_redditor(username)
		submissions = user.get_submitted(limit=None)
		comments = user.get_comments(limit=None)
		for s in submissions:
			subreddit = s.subreddit.display_name
			kb_submissions[subreddit] = (
				kb_submissions.get(subreddit, 0) + s.score)
		for c in comments:
			subreddit = c.subreddit.display_name
			kb_comments[subreddit] = (
				kb_comments.get(subreddit, 0) + c.score)
	except:
		print 'user deleted his/her account, smart'
karma_by_subreddit = {
	'submissions':kb_submissions,
	'comments':kb_comments,
	'users':users,
}
#save object to disk as json 
with open('data.json','w') as fp:
	json.dump(karma_by_subreddit,fp)