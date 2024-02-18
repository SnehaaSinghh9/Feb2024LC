#2402. Meeting Rooms III

#You are given an integer n. There are n rooms numbered from 0 to n - 1.
#You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). 
#All the values of starti are unique.
#Meetings are allocated to rooms in the following manner:
#Each meeting will take place in the unused room with the lowest number.
#If there are no available rooms, the meeting will be delayed until a room becomes free. 
#The delayed meeting should have the same duration as the original meeting.
#When a room becomes unused, meetings that have an earlier original start time should be given the room.
#Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.
#A half-closed interval [a, b) is the interval between a and b including a and not including b.

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
            ans = [0] * n
            times = [0] * n
            meetings.sort()

            for start, end in meetings:
                flag = False
                min = -1
                val = float('inf')
                for j in range(n):
                    if times[j] < val:
                        val = times[j]
                        min = j
                    if times[j] <= start:
                        flag = True
                        ans[j] += 1
                        times[j] = end
                        break
                if not flag:
                    ans[min] += 1
                    times[min] += (end - start)

            max = -1
            id = -1

            for i in range(n):
                if ans[i] > max:
                    max = ans[i]
                    id = i
                    
            return id
        
