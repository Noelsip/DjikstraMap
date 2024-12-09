from osm_parser import parse_osm
from graph_utils import create_graph, dijkstra
from map_visualizer import visualize_map
import folium

def create_initial_map(nodes, output_file="nodes_map.html"):
    """Membuat peta awal dengan semua simpul sebagai marker."""
    # Ambil koordinat dari simpul pertama untuk membuat peta awal
    first_node = list(nodes.values())[0]
    map = folium.Map(location=first_node, zoom_start=14)

    # Tambahkan marker untuk setiap simpul
    for node_id, (lat, lon) in nodes.items():
        folium.Marker(
            location=(lat, lon),
            popup=f"ID: {node_id}",
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(map)

    # Simpan peta ke file
    map.save(output_file)
    print(f"Peta simpul disimpan sebagai {output_file}. Buka file ini di browser Anda untuk melihat simpul.")

def main():
    # 1. Baca file OSM
    file_path = 'map.osm'  # Ganti dengan nama file OSM Anda
    nodes, ways = parse_osm(file_path)

    # 2. Buat graf
    graph, node_coords = create_graph(nodes, ways)

    # 3. Tampilkan peta awal dengan semua simpul
    create_initial_map(node_coords)

    # 4. Input simpul awal dan tujuan
    print("Lihat peta pada 'nodes_map.html' untuk melihat ID simpul.")
    start_node = input("Masukkan ID simpul awal: ").strip()
    end_node = input("Masukkan ID simpul akhir: ").strip()

    if start_node not in graph or end_node not in graph:
        print("Simpul yang dipilih tidak valid. Pastikan ID yang dimasukkan benar.")
        return

    # 5. Jalankan Dijkstra
    distance, path = dijkstra(graph, start_node, end_node)
    if not path:
        print("Tidak ditemukan jalur antara simpul awal dan akhir.")
        return

    print(f"Jarak terpendek: {distance} km")
    print(f"Jalur: {path}")

    # 6. Visualisasi peta dengan jalur terpendek
    visualize_map(node_coords, path, output_file='shortest_path_map.html')
    print("Peta jalur terpendek telah disimpan sebagai 'shortest_path_map.html'. Buka file ini di browser Anda.")

if __name__ == "__main__":
    main()
