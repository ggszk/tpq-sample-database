#
# Transform 'Map' format to node-edge format
# and merge it to original node, edge files
#

org_map_file = "./data/cal.map.txt"
node_poi_file = "./node_poi.txt"
edge_poi_file = "./edge_poi.txt"

debug = False

def map_to_node_edge() :
    # first id of POI nodes and edges
    node_id = 21048 
    edge_id = 21693
    category_max = 0
    with open(org_map_file) as f :
        with open(node_poi_file, mode='w') as n_f :
            with open(edge_poi_file, mode='w') as e_f :
                i = 0
                poi = False
                poi_edge = None
                for s_line in f:
                    t = s_line.split()
                    # POI line
                    if poi :
                        j = 0
                        while j <  len(t):
                            # write node file
                            n_f.write(str(node_id) + "," + t[j] + "\n")
                            if int(t[j]) > category_max :
                                category_max = int(t[j])
                            # POI edge
                            poi_edge_to = node_id
                            node_id = node_id + 1
                            poi_edge_dist = abs(float(t[j + 1]) - dist_offset)
                            dist_offset = float(t[j + 1])
                            edge_id = edge_id + 1
                            # write POI edge
                            e_f.write(str(edge_id) + "," + str(poi_edge_from) + "," + str(poi_edge_to) + "," + str(poi_edge_dist) + "\n")
                            poi_edge_from = poi_edge_to
                            # last poi edge
                            if j == len(t) - 2 :
                                edge_id = edge_id + 1
                                poi_edge_to = edge_to
                                poi_edge_dist = edge_dist - dist_offset
                                # write POI edge
                                e_f.write(str(edge_id) + "," + str(poi_edge_from) + "," + str(poi_edge_to) + "," + str(poi_edge_dist) + "\n")
                            j = j + 2
                        poi = False
                        continue
                    # Next line represets POIs
                    elif int(t[3]) > 0 :
                        poi = True
                        edge_from = t[0]
                        edge_to = t[1]
                        edge_dist = float(t[2])
                        dist_offset = 0
                        poi_edge_from = edge_from
                    # for debug
                    if debug :
                        i = i + 1
                        if i > 50 :
                            break
                print(category_max)

map_to_node_edge()
