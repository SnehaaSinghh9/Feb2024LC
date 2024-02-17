#1642. Furthest Building You Can Reach

#You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.
#You start your journey from building 0 and move to the next building by possibly using bricks or ladders.
#While moving from building i to building i+1 (0-indexed),
#If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
#If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
#Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        p = []
        i = 0

        for i in range(len(heights) - 1):
            d = heights[i + 1] - heights[i]
            if d <= 0:
                continue
            bricks -= d
            x = heapq.heappush(p, -d)
            if bricks < 0:
                bricks += -heapq.heappop(p)
                ladders -= 1 
            if ladders < 0:
                return i
        return len(heights)-1
