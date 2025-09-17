import heapq
from collections import defaultdict

class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        # food -> [cuisine, rating]
        self.food_info = {}
        # cuisine -> max-heap of (-rating, name)
        self.cuisine_heap = defaultdict(list)

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_info[f] = [c, r]
            heapq.heappush(self.cuisine_heap[c], (-r, f))

    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        cuisine, _ = self.food_info[food]
        self.food_info[food][1] = newRating
        # push new pair; old rating remains but will be skipped later
        heapq.heappush(self.cuisine_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        heap = self.cuisine_heap[cuisine]
        # pop until top matches current rating
        while heap:
            rating_neg, name = heap[0]
            if -rating_neg == self.food_info[name][1]:
                return name
            heapq.heappop(heap)  # discard outdated entry
        return ""

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)