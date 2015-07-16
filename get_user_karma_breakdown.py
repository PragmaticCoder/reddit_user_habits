import praw
users = ['audioburn','listen_up_buddy']
r = praw.Reddit(user_agent='africanawiki')
kb_submissions = {}
kb_comments = {}
for username in users:
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
			kb_comments.get(subreddit, 0) + s.score)
karma_by_subreddit = {
	'submissions':kb_submissions,
	'comments':kb_comments,
}
print karma_by_subreddit