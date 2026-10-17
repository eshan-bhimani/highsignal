from collections import defaultdict
class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #mapping each course to its prereqs: {course: [list of prereqps], course :[list of prereqs]...}
        preMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        #stores all courses along the current dfs path
        visiting = set()
        
        def dfs(course):
            if course in visiting:
                #cycle detected
                return False
            if preMap[course] == []:
                return True
            visiting.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            preMap[course] = []
            return True

        #loop thru numCourses, not dfs(course) returns False, then return False, else return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True








        preMap = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        visiting = set()

        def dfs(course):
            if course in visiting: #detect cycle
                return False
            if preMap[course] == []:
                return True
            visiting.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            preMap[course] = []
            return True
            



        for course in range(numCourses):
            if not dfs(course):
                return False
        return True