# Sample database for trip planning query

## Overview

* Neo4j database using the following sample data.
  * On Trip Planning Queries in Spatial Databases
    * https://www.cs.utah.edu/~lifeifei/tpq.html
  * Original data is in data directory.
* tpq_sample.py: generate poi node, edge data from original "Map" format file(cal.map.txt) 

## Installation (when using Neo4j desktop)

* Create empty database.
* Place the folloing csv files to Neo4j import folder.
  * cal.cnode.txt, cal.cedge.txt in data folder
  * node_poi.txt, edge_poi.txt in current folder
  * Import folder can be found in Neo4j Desktop ->select database->Manage->Open Folder.
* Execute load command in load.cypher in Neo4j Browser.

## Remark

* category id -1 means not POI (max category id is 62)