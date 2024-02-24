#2092. Find All People With Secret

#You are given an integer n indicating there are n people numbered from 0 to n - 1. 
#You are also given a 0-indexed 2D integer array meetings where meetings[i] = [xi, yi, timei] indicates that person xi and person yi have a meeting at timei. 
#A person may attend multiple meetings at the same time. Finally, you are given an integer firstPerson.
#Person 0 has a secret and initially shares the secret with a person firstPerson at time 0. 
#This secret is then shared every time a meeting takes place with a person that has the secret. 
#More formally, for every meeting, if a person xi has the secret at timei, then they will share the secret with person yi, and vice versa.
#The secrets are shared instantaneously. That is, a person may receive the secret and share it with people in other meetings within the same time frame.
#Return a list of all the people that have the secret after all the meetings have taken place. You may return the answer in any order.


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        groups = [i for i in range(n)]
        groups[firstPerson] = 0
        meetings.sort(key=lambda x: x[2])
        size = len(meetings)
        i = 0
        while i < size:
            current_time = meetings[i][2]
            temp = []
            while i < size and meetings[i][2] == current_time:
                g1 = self.find(groups, meetings[i][0])
                g2 = self.find(groups, meetings[i][1])
                groups[max(g1, g2)] = min(g1, g2)
                temp.extend([meetings[i][0], meetings[i][1]])
                i += 1
            for j in temp:
                if self.find(groups, j) != 0:
                    groups[j] = j
        result = []
        for j in range(n):
            if self.find(groups, j) == 0:
                result.append(j)
        return result

    def find(self, groups: List[int], index: int) -> int:
        while index != groups[index]:
            index = groups[index]
        return index
