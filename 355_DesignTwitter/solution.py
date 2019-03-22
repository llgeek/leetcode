import heapq
class Twitter:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = {}
        self.follower = {}
        self.timer = 0
        

    def postTweet(self, userId: int, tweetId: int):
        """
        Compose a new tweet.
        """
        self.timer += 1
        self.users[userId] = self.users.get(userId, []) + [(self.timer, tweetId)]
        

    def getNewsFeed(self, userId: int):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        # return self.users[userId][-5:]
        heap = []
        for user in self.follower.get(userId, set()) | {userId}:
            if user in self.users and self.users[user][-1]:
                heapq.heappush(
                    heap, (-self.users[user][-1][0], self.users[user][-1][1], user, 0))
        res = []
        while len(res) < 10 and heap:
            timer, tweet, user, idx = heapq.heappop(heap)
            res.append(tweet)
            if user in self.users and idx+1 < len(self.users[user]):
                idx += 1
                heapq.heappush(
                    heap, (-self.users[user][::-1][idx][0], self.users[user][::-1][idx][1], user, idx))
        return res          


        

    def follow(self, followerId: int, followeeId: int):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follower[followerId] = self.follower.get(followerId, set()) | {followeeId}
        

    def unfollow(self, followerId: int, followeeId: int):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.follower and followeeId in self.follower[followerId]:
            self.follower[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
