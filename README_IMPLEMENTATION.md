# Pipeline Builder Implementation

## Overview
This is a production-grade React + FastAPI application implementing a node-based pipeline builder similar to no-code tools. The implementation follows clean architecture principles with reusable components and modern design.

## Features Implemented

### ✅ Part 1 - Node Abstraction
- **BaseNode Component**: Reusable base component handling layout, headers, handles
- **Composable Architecture**: NodeHeader, NodeBody, and BaseNode components
- **Clean Node Definitions**: Each node only defines configuration (title, inputs, outputs, content)
- **5 New Example Nodes**: Math, Filter, API, Database, Condition nodes
- **Minimal Boilerplate**: Node creation requires minimal code

### ✅ Part 2 - Modern Design System
- **CSS Design System**: Comprehensive design tokens and styles
- **Professional UI**: Rounded cards, shadows, hover states, consistent spacing
- **Color Palette**: Unified color scheme with CSS variables
- **Typography**: Consistent font sizes and weights
- **Responsive Layout**: Proper scaling and mobile-friendly

### ✅ Part 3 - Enhanced Text Node
- **Auto-resize**: Text input automatically grows based on content (40px-200px height)
- **Variable Detection**: Detects `{{variableName}}` patterns
- **JavaScript Validation**: Validates identifiers using regex
- **Dynamic Handles**: Automatically creates input handles for detected variables
- **Deduplication**: Removes duplicate handles automatically
- **Performance Optimized**: Handles rapid typing safely

### ✅ Part 4 - Backend Integration
- **FastAPI Backend**: RESTful API with Pydantic models
- **Pipeline Analysis**: Counts nodes and edges
- **DAG Detection**: Uses Kahn's algorithm for cycle detection
- **User-friendly Results**: Modal display with clear status indicators
- **Error Handling**: Graceful error states with user feedback

## Architecture

### Frontend Structure
```
src/
├── components/
│   ├── BaseNode.js          # Reusable base node component
│   ├── NodeHeader.js        # Node header component
│   └── NodeBody.js          # Node body component
├── nodes/
│   ├── inputNode.js         # Input node (refactored)
│   ├── outputNode.js        # Output node (refactored)
│   ├── llmNode.js           # LLM node (refactored)
│   ├── textNode.js          # Enhanced text node
│   ├── mathNode.js          # Mathematical operations
│   ├── filterNode.js        # Data filtering
│   ├── apiNode.js           # API integration
│   ├── databaseNode.js      # Database operations
│   └── conditionNode.js     # Conditional logic
├── styles/
│   └── design-system.css    # Design system and CSS variables
├── store.js                 # Zustand state management
├── ui.js                    # ReactFlow UI components
├── toolbar.js               # Draggable node toolbar
├── submit.js                # Submit functionality with backend integration
└── App.js                   # Main application component
```

### Backend Structure
```
backend/
└── main.py                  # FastAPI application with DAG detection
```

## Key Components

### BaseNode Component
The heart of the node system:
- Handles consistent layout and styling
- Manages input/output handles automatically
- Provides accessibility features
- Supports hover states and interactions

### Enhanced Text Node
Advanced text processing:
- Auto-resizing textarea (40px-200px)
- Variable detection with `{{variableName}}` syntax
- Dynamic handle creation based on detected variables
- Real-time variable validation

### Backend API
Pipeline analysis endpoints:
- `POST /pipelines/parse` - Analyze pipeline structure
- Returns node count, edge count, and DAG status
- Uses Kahn's algorithm for cycle detection

## Design System

### CSS Variables
- **Colors**: Primary, gray, semantic colors
- **Typography**: Font families and sizes
- **Spacing**: Consistent spacing scale
- **Shadows**: Multiple shadow levels
- **Transitions**: Smooth animations

### Component Classes
- `.base-node` - Node container styling
- `.form-input`, `.form-select`, `.form-textarea` - Form controls
- `.btn`, `.btn-primary`, `.btn-secondary` - Button styles
- `.draggable-node` - Toolbar node styling

## Usage Examples

### Creating a New Node
```javascript
export const ExampleNode = ({ id, data }) => {
  const nodeConfig = {
    title: '🔧 Example',
    inputs: [{ id: 'input', label: 'Input' }],
    outputs: [{ id: 'output', label: 'Output' }]
  };

  return (
    <BaseNode id={id} data={data} {...nodeConfig}>
      <NodeBody>
        <div className="form-group">
          <label className="form-label">Field:</label>
          <input className="form-input" type="text" />
        </div>
      </NodeBody>
    </BaseNode>
  );
};
```

### Text Node Variable Detection
```javascript
// Input: "Hello {{name}}, you have {{count}} messages"
// Automatically creates handles for: name, count
```

## Running the Application

### Frontend
```bash
cd frontend
npm install
npm start
```

### Backend
```bash
cd backend
pip install fastapi uvicorn
uvicorn main:app --reload
```

## Quality Features

- **Clean Code**: Meaningful variable names, consistent formatting
- **Error Handling**: Graceful error states and user feedback
- **Performance**: Optimized re-renders and efficient algorithms
- **Accessibility**: Proper ARIA labels and keyboard navigation
- **Responsive**: Works across different screen sizes
- **Type Safety**: Pydantic models and prop validation

## Testing

The implementation includes:
- Component composition testing
- Variable detection edge cases
- DAG cycle detection validation
- Backend API integration
- UI interaction testing

## Future Enhancements

- Real-time collaboration
- Advanced node types
- Pipeline execution engine
- Visual debugging tools
- Export/import functionality
