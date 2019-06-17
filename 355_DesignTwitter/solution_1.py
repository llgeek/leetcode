import heapq
class Twitter(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.MOSTNUM = 10
        self.user2tweet = {}
        self.followers = {}
        self.timer = 0
        

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        if userId not in self.followers:
            self.followers[userId] = {userId}
        if userId not in self.user2tweet:
            self.user2tweet[userId] = []
        self.user2tweet[userId].append((tweetId, self.timer))
        self.timer += 1

        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if userId not in self.followers:
            return []
        heap = []
        res = []
        for follower in self.followers[userId]:
            if follower in self.user2tweet:
                heapq.heappush(heap, (-self.user2tweet[follower][-1][1], follower, len(self.user2tweet[follower])-1))
        while heap:
            if len(res) == self.MOSTNUM:
                break
            _, follower, idx = heapq.heappop(heap)
            res.append(self.user2tweet[follower][idx][0])
            idx -= 1
            if idx >= 0:
                heapq.heappush(heap, (-self.user2tweet[follower][idx][1], follower, idx))
        return res        

        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.followers[followerId] = self.followers.get(
            followerId, {followerId}) | {followeeId}
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId == followeeId:
            return
        if followerId in self.followers and followeeId in self.followers[followerId]:
            self.followers[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
