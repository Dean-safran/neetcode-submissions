import heapq
class Twitter:

    def __init__(self):
        self.time = 0

        self.tweets = set()

        self.users = set()

        # stores {user_id : set(user_ids)}
        self.follows = dict()
    
        # stores {user_id : min_heap[tweet_ids]}
        self.posts = dict()

        # stores {user_id: min_heap[tweet_ids]}
        self.news_feeds = dict()
    
    def check(self, userId) : 
        if userId not in self.users: 
            self.users.add(userId)
        if userId not in self.follows: 
            self.follows[userId] = set()
        if userId not in self.posts: 
            self.posts[userId] = []
        if userId not in self.news_feeds: 
            self.news_feeds[userId] = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        if tweetId in self.tweets :
            return
        self.tweets.add(tweetId)

        self.check(userId)

        heapq.heappush(self.posts[userId], (self.time, tweetId))
        heapq.heappush(self.news_feeds[userId], (self.time, tweetId))
        
        if len(self.posts[userId]) > 10 :
            heapq.heappop(self.posts[userId])
        if len(self.news_feeds[userId]) > 10 :
            heapq.heappop(self.news_feeds[userId])

        # add new post to anyones' news feed who follows 
        # userId
        for user in self.follows : 
            if userId in self.follows[user] :

                if user not in self.news_feeds :
                    self.news_feeds[user] = []
                heapq.heappush(self.news_feeds[user], (self.time, tweetId))

            if len(self.news_feeds[user]) > 10 :
                heapq.heappop(self.news_feeds[user])

        self.time += 1




    def getNewsFeed(self, userId: int) -> List[int]:
        self.check(userId)
        copy = self.news_feeds[userId].copy()
        copy.sort(reverse=True)
        res = []
        for _, tweetId in copy :
            res.append(tweetId)
        return res




    def follow(self, followerId: int, followeeId: int) -> None:
        self.check(followerId)
        self.check(followeeId)
        if followerId == followeeId :
            return 
        if followeeId in self.follows[followerId] :
            return
        
        self.follows[followerId].add(followeeId)

        # update follower newsfeed
        for time, tweetId in self.posts[followeeId] :
            heapq.heappush(self.news_feeds[followerId], (time, tweetId))
            if len(self.news_feeds[followerId]) > 10 :
                heapq.heappop(self.news_feeds[followerId])
        return




    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows :
            return
        if followeeId not in self.follows[followerId] :
            return 
        self.follows[followerId].remove(followeeId)
        
        self.check(followerId)
        self.check(followeeId)

        # update follower newsfeed 
        self.news_feeds[followerId] = self.posts[followerId].copy()
        for userId in self.follows[followerId] : 
            for time, tweetId in self.posts[userId] :
                heapq.heappush(self.news_feeds[followerId], (time, tweetId))
                if len(self.news_feeds[followerId]) > 10 :
                    heapq.heappop(self.news_feeds[followerId])
        return
