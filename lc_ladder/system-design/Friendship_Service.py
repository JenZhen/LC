#!/usr/local/bin/python3

# https://www.lintcode.com/problem/friendship-service/my-submissions?_from=ladder&&fromId=8
# Example
# 支持 follow & unfollow, getFollowers, getFollowings方法
#
# 样例
# follow(1, 3)
# getFollowers(1) // return [3]
# getFollowings(3) // return [1]
# follow(2, 3)
# getFollowings(3) // return [1,2]
# unfollow(1, 3)
# getFollowings(3) // return [2]

"""
Solution:

Corner cases:
"""

class FriendshipService:

    def __init__(self):
        # do intialization if necessary
        # key: user, value: list of followers
        self.follower_table = dict()
        # key: user, value: list of followees
        self.followee_table = dict()
    """
    @param: user_id: An integer
    @return: all followers and sort by user_id
    """
    def getFollowers(self, user_id):
        # write your code here
        if user_id not in self.follower_table:
            return []
        return sorted(self.follower_table[user_id])
    """
    @param: user_id: An integer
    @return: all followings and sort by user_id
    """
    def getFollowings(self, user_id):
        # write your code here
        if user_id not in self.followee_table:
            return []
        return sorted(self.followee_table[user_id])

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def follow(self, from_user_id, to_user_id):
        # write your code here
        if to_user_id not in self.followee_table:
            self.followee_table[to_user_id] = set()
        self.followee_table[to_user_id].add(from_user_id)

        if from_user_id not in self.follower_table:
            self.follower_table[from_user_id] = set()
        self.follower_table[from_user_id].add(to_user_id)


    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def unfollow(self, from_user_id, to_user_id):
        # write your code here
        if to_user_id in self.followee_table:
            if from_user_id in self.followee_table[to_user_id]:
                self.followee_table[to_user_id].remove(from_user_id)

        if from_user_id in self.follower_table:
            if to_user_id in self.follower_table[from_user_id]:
                self.follower_table[from_user_id].remove(to_user_id)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
