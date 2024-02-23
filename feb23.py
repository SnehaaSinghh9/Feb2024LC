#787. Cheapest Flights Within K Stops

#There are n cities connected by some number of flights. 
#You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
#You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [float('inf')] * n
        dp[src] = 0
        for _ in range(k + 1):
            temp = dp[:]
            for flight in flights:
                if dp[flight[0]] != float('inf'):
                    temp[flight[1]] = min(temp[flight[1]], dp[flight[0]] + flight[2])
            dp = temp
        
        return dp[dst] if dp[dst] != float('inf') else -1
