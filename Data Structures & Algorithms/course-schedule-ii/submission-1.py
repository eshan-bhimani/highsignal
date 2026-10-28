'''
You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.
Return a valid ordering of courses you can take to finish all courses. If there are many valid answers, return any of them. If it's not possible to finish all courses, return an empty array.

Example 1:
Input: numCourses = 3, prerequisites = [[1,0]]

Output: [0,1,2]
Explanation: We must ensure that course 0 is taken before course 1.

# [0,1]
'''

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set() # saves time by checking if we've visited --> returns True
        visiting = set() # return False
        order = [] # order of classes

        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)


        def dfs(course):
            if course in visiting: # catch cycles
                return False
            if course in visited:
                return True
            
            
            visiting.add(course) # marking course as currently being check

            # check all prerequisites for X course
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False

            visiting.remove(course) # remove from currently being checked
            visited.add(course) # add to visited
            order.append(course) # adds deepest course to order
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return order

            