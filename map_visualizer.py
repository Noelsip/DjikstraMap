import folium

def visualize_map(nodes, path, output_file='map.html'):
    """Menampilkan peta dengan jalur terpendek."""
    if not path:
        print("Tidak ada jalur yang ditemukan.")
        return

    # Ambil koordinat untuk jalur
    path_coords = [nodes[node] for node in path]

    # Buat peta di lokasi awal
    start_lat, start_lon = path_coords[0]
    map = folium.Map(location=[start_lat, start_lon], zoom_start=14)

    # Tambahkan marker untuk setiap simpul di jalur
    for coord in path_coords:
        folium.Marker(location=coord).add_to(map)

    # Tambahkan jalur
    folium.PolyLine(path_coords, color='blue', weight=2.5).add_to(map)

    # Simpan peta ke file
    map.save(output_file)
    print(f"Peta disimpan sebagai {output_file}")
