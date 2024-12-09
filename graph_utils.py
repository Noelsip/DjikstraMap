from math import radians, sin, cos, sqrt, atan2
import heapq

def haversine(lat1, lon1, lat2, lon2):
    """Menghitung jarak antara dua koordinat geografis."""
    R = 6371  # Radius bumi dalam km
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

def create_graph(nodes, ways):
    """Membuat graf dari data simpul dan jalan."""
    graph = {node: {} for node in nodes}

    for way in ways:
        for i in range(len(way) - 1):
            node1, node2 = way[i], way[i+1]
            lat1, lon1 = nodes[node1]
            lat2, lon2 = nodes[node2]
            distance = haversine(lat1, lon1, lat2, lon2)
            graph[node1][node2] = distance
            graph[node2][node1] = distance

    return graph, nodes

def dijkstra(graph, start, end):
    """Mencari rute terpendek menggunakan algoritma Dijkstra."""
    heap = [(0, start)]  # (jarak, simpul)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    prev_nodes = {node: None for node in graph}

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_node == end:
            break

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                prev_nodes[neighbor] = current_node
                heapq.heappush(heap, (distance, neighbor))

    # Rekonstruksi jalur
    path = []
    current = end
    while current:
        path.insert(0, current)
        current = prev_nodes[current]

    return distances[end], path
