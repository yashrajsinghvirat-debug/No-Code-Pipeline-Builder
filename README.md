# Pipeline Builder

A no-code visual pipeline builder with drag-and-drop interface and DAG validation.

## Features

- **Node Abstraction**: Reusable BaseNode component eliminates code duplication
- **Dynamic Text Nodes**: Auto-resize and variable detection with `{{variable}}` syntax  
- **Backend DAG Validation**: Detects cycles and validates pipeline structure
- **Professional UI**: Modern design with hover effects and animations

## Tech Stack

**Frontend**: React 18, ReactFlow, Zustand, CSS design system  
**Backend**: FastAPI, Pydantic, Kahn's algorithm for cycle detection

## Quick Start

```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000

# Frontend  
cd frontend
npm install
npm start
```

Visit `http://localhost:3000`

## How to Use

1. **Add Nodes**: Drag from toolbar or click to add to canvas
2. **Connect Nodes**: Drag from green (source) to blue (target) handles
3. **Submit Pipeline**: Click "Submit Pipeline" to validate and analyze
4. **View Results**: See node count, edge count, and DAG status
