#!/usr/local/bin/python3

# https://www.lintcode.com/problem/design-twitter/description?_from=ladder&&fromId=8
# Example
# 实现一个迷你的推特，支持下列几种方法
# 1.postTweet(user_id, tweet_text). 发布一条推特.
# 2.getTimeline(user_id). 获得给定用户最新发布的十条推特，按照发布时间从最近的到之前排序
# 3.getNewsFeed(user_id). 获得给定用户的朋友或者他自己发布的最新十条推特，从发布时间最近到之前排序
# 4.follow(from_user_id, to_user_id). from_user_id 关注 to_user_id.
# 5.unfollow(from_user_id, to_user_id). from_user_id 取消关注 to_user_id.
#
# 样例
# postTweet(1, "LintCode is Good!!!")
# >> 1
# getNewsFeed(1)
# >> [1]
# getTimeline(1)
# >> [1]
# follow(2, 1)
# getNewsFeed(2)
# >> [1]
# unfollow(2, 1)
# getNewsFeed(2)
# >> []

"""
Solution:

Corner cases:
"""

'''
Definition of Tweet:
class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
'''

class MiniTwitter:

    def __init__(self):
        # do intialization if necessary
        self.globalTweetId = 0
        self.tweet_table = {}
        self.friends_table = {}

    """
    @param: user_id: An integer
    @param: tweet_text: a string
    @return: a tweet
    """
    def postTweet(self, user_id, tweet_text):
        # write your code here
        tweet = Tweet.create(user_id, tweet_text)
        # auto-incr id for newly created tweet
        self.globalTweetId += 1
        if user_id in self.tweet_table:
            # insert into tweet_table using user_id as key (shardingkey)
            # append a tuple of tweet id and tweet object
            self.tweet_table[user_id].append((self.globalTweetId, tweet))
        else:
            self.tweet_table[user_id] = [(self.globalTweetId, tweet)]

        return tweet
    """
    @param: user_id: An integer
    @return: a list of 10 new feeds recently and sort by timeline
    """
    def getNewsFeed(self, user_id):
        # write your code here
        # get all user follows
        rt = []
        if user_id in self.tweet_table:
            rt = self.tweet_table[user_id][-10:]

        if user_id in self.friends_table:
            for friend in self.friends_table[user_id]:
                if friend in self.tweet_table:
                    rt.extend(self.tweet_table[friend][-10:])

        def keyFunc(tweet):
            return tweet[0]

        rt.sort(key = keyFunc)
        return [twt[1] for twt in rt[-10:][::-1]]
    """
    @param: user_id: An integer
    @return: a list of 10 new posts recently and sort by timeline
    """
    def getTimeline(self, user_id):
        # write your code here
        if user_id in self.tweet_table:
            #if has tweet
            #[-10:] last 10 tweets
            #[::-1] get it in reversed order, one by one
            return [tweet[1] for tweet in self.tweet_table[user_id][-10:][::-1]]
        else:
            #if not found in tweet table no tweet yet
            return []
    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def follow(self, from_user_id, to_user_id):
        # write your code here
        # use set to contain friends to headle duplicates
        if from_user_id not in self.friends_table:
            self.friends_table[from_user_id] = set()
        self.friends_table[from_user_id].add(to_user_id)
    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def unfollow(self, from_user_id, to_user_id):
        # write your code here
        # if can do unfollow should have had record in friends_table
        # for safety do a check
        if from_user_id not in self.friends_table:
            return
        self.friends_table[from_user_id].remove(to_user_id)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
