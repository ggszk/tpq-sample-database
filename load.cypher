LOAD CSV FROM "file:///cal.cnode.txt" AS line FIELDTERMINATOR ' '
CREATE (p:g_tpq { n_id: toInteger(line[0]), category: -1});
LOAD CSV FROM "file:///cal.cedge.txt" AS line FIELDTERMINATOR ' '
MATCH (from_n:g_tpq { n_id: toInteger(line[1])}),(to_n:g_tpq { n_id: toInteger(line[2])})
CREATE (from_n)-[:CONNECTED_TO { e_id: line[0], cost: toFloat(line[3]) }]->(to_n);
LOAD CSV FROM "file:///node_poi.txt" AS line
CREATE (p:g_tpq { n_id: toInteger(line[0]), category: toInteger(line[1])}); 
LOAD CSV FROM "file:///edge_poi.txt" AS line
MATCH (from_n:g_tpq { n_id: toInteger(line[1])}),(to_n:g_tpq { n_id: toInteger(line[2])})
CREATE (from_n)-[:CONNECTED_TO { e_id: line[0], cost: toFloat(line[3]) }]->(to_n);
