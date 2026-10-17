class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        # preMap adjList mapping each course to a list of their prereqs. 
        # a visitng set for courses on the current path
        # dfs on all courses
        # if cycle detected (if course in visiting:) return an empty array because its not possible to finish all courses
        # return an array with valid order if you can take all courses

        preMap = {i : [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        visit, cycle = set(), set()
        order = []

        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True

            cycle.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            cycle.remove(course)
            visit.add(course)
            order.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return order

