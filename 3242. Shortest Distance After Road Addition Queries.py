class Solution(object):
    def shortestDistanceAfterQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        solutions = []
        self.paths = [[city + 1] for city in range(n)]
        for query in queries: 
            self.pre_calculated = {}
            self.paths[query[0]].append(query[1])
            solution = self.shortesDistance(0, n)
            solutions.append(solution)
        return solutions    

    def shortesDistance(self, a, b):
        if a == b:
            return 0
        if a + 1 == b:
            return 0
        if a in self.pre_calculated:
            return self.pre_calculated[a]

        posible_paths = self.paths[a]
        posible_distances = []
        for posible_path in posible_paths:
            posible_distance = self.shortesDistance(posible_path, b)
            self.pre_calculated[posible_path] = posible_distance
            posible_distances.append(posible_distance)

        return 1 + min(posible_distances) 