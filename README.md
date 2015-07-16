# subreddit_analysis
analyse the habits of the users of a subreddit on Reddit

The main file is called coontown_breakdown because it was originally used to analyze the habits of coontown users. 

Right now these are just scripts, I plan to make them a bit easier to reuse soon.

For now you will have to go into coontown_breakdown.py and edit accordingly to whatever parameters you desire (subreddit, limit, etc)

    python coontown_breakdown.py #will create a json file, you'll want to rename this in coontown_breakdown.py
    
After that

    python clean_cb_data.py #will create a couple csv's to be used for data visualization
    
