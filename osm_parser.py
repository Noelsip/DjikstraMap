import xmltodict

def parse_osm(file_path):
    """Membaca file OSM dan mengembalikan data simpul dan jalan."""
    with open(file_path, 'rb') as file:
        osm_data = xmltodict.parse(file)

    nodes = {}
    ways = []

    # Ambil simpul
    for node in osm_data['osm']['node']:
        node_id = node['@id']
        nodes[node_id] = (float(node['@lat']), float(node['@lon']))

    # Ambil jalan
    for way in osm_data['osm'].get('way', []):
        way_nodes = way.get('nd', [])
        if len(way_nodes) > 1:
            way_points = [nd['@ref'] for nd in way_nodes]
            ways.append(way_points)

    return nodes, ways
