 
import os
import logging
from fastapi import FastAPI, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
from collections import defaultdict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Get port from environment or use default
port = int(os.environ.get("PORT", 8000))

app = FastAPI(
    title="Vector Pipeline API",
    description="API for parsing and analyzing vector pipelines",
    version="1.0.0"
)

# Add CORS middleware
# Allow frontend origin from environment or default to localhost
frontend_origin = os.environ.get("FRONTEND_ORIGIN", "http://localhost:3000")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_origin, "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Node(BaseModel):
    id: str
    type: str
    position: Dict[str, float]
    data: Dict[str, Any]

class Edge(BaseModel):
    id: str
    source: str
    target: str
    sourceHandle: str = None
    targetHandle: str = None

class Pipeline(BaseModel):
    nodes: List[Node]
    edges: List[Edge]

def is_dag(nodes: List[Node], edges: List[Edge]) -> bool:
    """Detect if the graph is a Directed Acyclic Graph (DAG) using DFS."""
    # Build adjacency list
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    # Initialize nodes in graph
    for node in nodes:
        in_degree[node.id] = 0
    
    # Build graph from edges
    for edge in edges:
        graph[edge.source].append(edge.target)
        in_degree[edge.target] += 1
    
    # Kahn's algorithm for topological sort
    queue = [node_id for node_id in in_degree if in_degree[node_id] == 0]
    visited_count = 0
    
    while queue:
        current = queue.pop(0)
        visited_count += 1
        
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # If we visited all nodes, it's a DAG
    return visited_count == len(nodes)

@app.get('/')
def read_root():
    """Health check endpoint"""
    logger.info("Health check endpoint accessed")
    return {'status': 'healthy', 'service': 'vector-pipeline-api'}

@app.post('/pipelines/parse')
def parse_pipeline(pipeline: Pipeline):
    """Parse pipeline and return analysis including DAG detection."""
    
    try:
        logger.info(f"Received pipeline with {len(pipeline.nodes)} nodes and {len(pipeline.edges)} edges")
        
        # Validate input
        if not pipeline.nodes:
            raise HTTPException(status_code=400, detail="Pipeline must contain at least one node")
        
        num_nodes = len(pipeline.nodes)
        num_edges = len(pipeline.edges)
        is_dag_result = is_dag(pipeline.nodes, pipeline.edges)
        
        result = {
            'num_nodes': num_nodes,
            'num_edges': num_edges,
            'is_dag': is_dag_result
        }
        
        logger.info(f"Pipeline analysis completed: {result}")
        return result
        
    except Exception as e:
        logger.error(f"Error processing pipeline: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    logger.info(f"Starting server on port {port}")
    uvicorn.run(app, host="0.0.0.0", port=port)
