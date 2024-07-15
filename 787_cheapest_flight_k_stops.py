class Solution:
    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        """
        The `findCheapestPrice` method calculates the cheapest price to travel from `src` to `dst`
        with at most `k` stops using a modified Bellman-Ford algorithm.

        Example:
        Consider the following scenario:
        - n = 4 (cities are 0, 1, 2, 3)
        - flights = [
            [0, 1, 100],
            [1, 2, 100],
            [2, 0, 100],
            [1, 3, 600],
            [2, 3, 200]
          ]
        - src = 0 (starting city)
        - dst = 3 (destination city)
        - k = 1 (at most 1 stop allowed)

        Step-by-step calculation:
        1. Initialize distances: [0, inf, inf, inf]
        2. Iteration 0:
           - Check flight [0, 1, 100]: Update distance to city 1: [0, 100, inf, inf]
           - Check flight [1, 2, 100]: No update, as distance to city 1 is inf.
           - Check flight [2, 0, 100]: No update, as distance to city 2 is inf.
           - Check flight [1, 3, 600]: No update, as distance to city 1 is inf.
           - Check flight [2, 3, 200]: No update, as distance to city 2 is inf.
        3. Iteration 1:
           - Check flight [0, 1, 100]: No update, as distance to city 1 is already 100.
           - Check flight [1, 2, 100]: Update distance to city 2: [0, 100, 200, inf]
           - Check flight [2, 0, 100]: No update, as distance to city 2 is 200.
           - Check flight [1, 3, 600]: Update distance to city 3: [0, 100, 200, 700]
           - Check flight [2, 3, 200]: Update distance to city 3: [0, 100, 200, 400]

        Final distances: [0, 100, 200, 400]
        The cheapest price to travel from city 0 to city 3 with at most 1 stop is 400.
        """

        distances = [float("+inf")] * n
        distances[src] = 0
        for i in range(k + 1):
            tmp_distances = distances[:]
            for source, dest, weight in flights:
                if distances[source] + weight < tmp_distances[dest]:
                    tmp_distances[dest] = distances[source] + weight
            distances = tmp_distances

        if distances[dst] == float("inf"):
            return -1
        else:
            return int(distances[dst])


if __name__ == "__main__":
    s = Solution()
    s.findCheapestPrice(
        4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1
    )
