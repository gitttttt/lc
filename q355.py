import time

class T:
    def __init__(self, u, t):
        self.u = u
        self.t = t
        self.n = time.time()

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.feed = []
        self.user = {}


    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.feed.append(T(userId, tweetId))


    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        u = [userId]
        if userId in self.user:
            u = u + self.user[userId]
        return filter(lambda x: x.u in u, self.feed)[:10]




    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId not in self.user:
            self.user[followerId] = []
        self.user[followerId].append(followeeId)



    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """

        self.user[followerId].remove(followeeId)

userId = 1
tweetId = 1
followerId = 1
followeeId = 2
obj = Twitter()
obj.postTweet(userId,tweetId)
param_2 = obj.getNewsFeed(userId)
obj.follow(followerId,followeeId)
obj.unfollow(followerId,followeeId)