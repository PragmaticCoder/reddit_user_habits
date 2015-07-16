import praw
users = []
r = praw.Reddit(user_agent='africanawiki')
subreddit = r.get_subreddit('coontown')
ids = [submission.id for submission in subreddit.get_hot(limit=25)]
submissions = [r.get_submission(submission_id=id) for id in ids]
root_comments = []
for s in submissions:
	for c in s.comments:
		root_comments.append(c)
print root_comments
def get_comments(comments):

	for c in comments:
		try:
			print 'trying'
			users.append(c.author.name)
		except AttributeError:				
			print 'swagless'
		if hasattr(c,'replies'):
			get_comments(c.replies)
get_comments(root_comments)
print users