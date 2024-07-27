from typing import List, Tuple
import heapq
from math import inf


class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        graph: List[List[Tuple[int, int]]] = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        min_reachable: int = inf
        min_city: int = -1

        for u in range(n):
            reachable: int = sum(
                1 for d in self.dijkstra(u, graph) if d <= distanceThreshold
            )
            if reachable < min_reachable or (
                reachable == min_reachable and u > min_city
            ):
                min_reachable = reachable
                min_city = u

        return min_city

    def dijkstra(self, start: int, graph: List[List[Tuple[int, int]]]) -> List[int]:
        heap: List[Tuple[int, int]] = [(0, start)]
        distances: List[int] = [inf] * len(graph)
        distances[start] = 0

        while heap:
            d, u = heapq.heappop(heap)
            if d > distances[u]:
                continue
            for v, w in graph[u]:
                d2 = d + w
                if distances[v] > d2:
                    distances[v] = d2
                    heapq.heappush(heap, (d2, v))

        return distances
