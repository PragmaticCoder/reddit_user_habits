# subreddit_analysis
Discover the posting and commenting habits of the users of a particular subreddit with subreddit_analysis

[Example analysis](http://www.codeblackgroup.com/news/race-and-class/1/archive-coontown-breakdown-part-1/) 

To analyze a subreddit, do:

    python analyze.py your_subreddit
    
This will create a json file called data.json. You'll then want to do:

    python clean_cb_data.py data.json

And then you'll have your csv files (comments.csv,submissions.csv,users.csv). Happy crunching!

To analyze by post frequency instead of karma score, go to lines 44 and 48 in analyze.py and change both s.score and c.score to 1. 

Further reading: https://praw.readthedocs.org/

________

The MIT License (MIT)

Copyright (c) 2015 Mike Johnson Jr

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
    
