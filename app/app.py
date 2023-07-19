
from flask import Flask, request
from flask_cors import CORS, cross_origin
from pathfinding.graph_constructor import Graph
from pathfinding.depth_first_search import DFSGraph
from pathfinding.dijkstra import DijkstraGraph
from pathfinding.floyd_warshall import FloydWarshallGraph
from pathfinding.breadth_first_search import BFSGraph
from pathfinding.bellman_ford import BellmanGraph
from pathfinding.a_star import AStarGraph


app = Flask(__name__)
cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'
app.debug = True

# @app.after_request
# def after_request(resp):
#     resp.headers.add('Access-Control-Allow-Origin', '*')
#     resp.headers.add('Access-Control-Allow-Headers', 'Content-Type, X-Token')
#     resp.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
#     print(resp.headers)

def jsonToInt(x):
    return {
        int(outerKey):{
            int(innerKey): innerVal for innerKey, innerVal in outerVal.items()
        }
        for outerKey, outerVal in x.items()
    }


@app.post('/a_star')
# @cross_origin()
def a_star():
    json = request.get_json() #loads json from the body
    print("before")

    start = json["start"]
    end = json["end"]
    edges = json["edges"]

    print(start)
    print(end)
    print(edges)

    graph = AStarGraph.from_existing(jsonToInt(edges)) #converts to integer
    print("checking")
    path = graph.a_star(start, end) #calculates the path

    
    return {'path': path} 

@app.post('/dijkstra')
def dijkstra():
    graph = DijkstraGraph(4)
    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 2, 3)
    graph.add_edge(0, 3, 4)
    graph.add_edge(1, 2, 6)

    start = 0
    distances = graph.dijkstra(start)
    
    

    return jsonify(distances)

@app.post('/bellman_ford')
def bellman_ford():
    graph = BellmanGraph(10)
    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 2, 3)
    graph.add_edge(1, 2, 4)
    graph.add_edge(1, 3, 5)
    graph.add_edge(2, 3, 6)
    graph.add_edge(3, 4, 7)
    graph.add_edge(4, 5, 8)
    graph.add_edge(5, 6, 9)
    graph.add_edge(6, 7, 10)

    return jsonify(graph.bellman_ford(0))



@app.post('/breadth_first_search')
def breadth_first_search():
    graph = BFSGraph(4)
    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 2, 3)
    graph.add_edge(1, 2, 4)
    graph.add_edge(2, 3, 1)
    graph.add_edge(0, 3, 5)

    return graph.breadth_first_search(0)


@app.post('/depth_first_search')
def dfs():
    graph = DFSGraph(vertices=4)
    graph.add_edge(0,1,1)
    graph.add_edge(1,2,3)
    graph.add_edge(2,3, 2)

    return graph.dfs(0)


@app.post('/floyd_warshall')
def floyd_warshall():
    graph = FloydWarshallGraph(4)
    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 2, 3)
    graph.add_edge(1, 2, 4)
    graph.add_edge(2, 3, 1)
    graph.add_edge(0, 3, 5)

    return graph.floyd_warshall()









if __name__ == '__main__':
    app.run()