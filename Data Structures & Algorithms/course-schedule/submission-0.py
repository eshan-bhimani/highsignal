from collections import defaultdict
class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        visited = set()
        visiting = set()
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[course].append(prereq)

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            visiting.add(course)

            for prereq in adj[course]:
                if dfs(prereq) == False:
                    return False
            visiting.remove(course)
            visited.add(course)
            return True
        for course in range(numCourses):
            if dfs(course) == False:
                return False
        return True