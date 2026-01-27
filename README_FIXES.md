# Frontend-Backend Connectivity Fixes

## Issues Fixed

### 1. ✅ API URL Updated
- Changed from `http://localhost:8000` to `http://127.0.0.1:8000`
- More reliable for local development

### 2. ✅ CORS Middleware Added
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 3. ✅ Enhanced Error Handling
- Network error detection with specific messages
- Response status and header logging
- Better error messages for debugging

### 4. ✅ Data Validation
- Check if nodes exist before sending
- Payload logging for debugging
- CORS mode explicitly set

### 5. ✅ Debug Tools Added
- Debug panel to inspect data structure
- Connection test button
- Console logging throughout

## Testing Steps

### 1. Start Backend
```bash
cd backend
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### 2. Start Frontend
```bash
cd frontend
npm start
```

### 3. Test Connection
1. Open browser to `http://localhost:3000`
2. Click "Test Connection" button
3. Should see "Backend is reachable!" message

### 4. Test Pipeline Submission
1. Drag some nodes to the canvas
2. Connect them if desired
3. Click "Submit Pipeline"
4. Should see analysis results

## Debug Information

### Console Logs
- Frontend: Check browser console for payload and response logs
- Backend: Check terminal for received requests and processing

### Debug Panel
- Blue "Debug Data" button shows current nodes/edges structure
- Displays node/edge count in real-time

### Test Files
- `test_api.py`: Python script to test backend directly
- `test_frontend.html`: Simple HTML test for API calls
- `curl` commands: Manual testing

## Common Issues & Solutions

### "Failed to fetch" Error
1. **Backend not running**: Start FastAPI server
2. **Wrong URL**: Ensure using 127.0.0.1:8000
3. **CORS issues**: Check CORS middleware configuration
4. **Firewall**: Ensure port 8000 is accessible

### Empty Response
1. **No nodes**: Add nodes to pipeline first
2. **Invalid data**: Check debug panel for data structure
3. **Backend error**: Check backend console for errors

### CORS Errors
1. **Origin not allowed**: Add frontend URL to CORS origins
2. **Methods not allowed**: Ensure POST is allowed
3. **Headers not allowed**: Ensure Content-Type is allowed

## Verification Commands

### Test Backend Directly
```bash
curl -X POST "http://127.0.0.1:8000/pipelines/parse" \
  -H "Content-Type: application/json" \
  -d '{"nodes": [{"id": "test", "type": "customInput", "position": {"x": 100, "y": 100}, "data": {}}], "edges": []}'
```

### Test CORS
```bash
curl -X POST "http://127.0.0.1:8000/pipelines/parse" \
  -H "Content-Type: application/json" \
  -H "Origin: http://localhost:3000" \
  -d '{"nodes": [], "edges": []}' -v
```

## Expected Results

### Successful Response
```json
{
  "num_nodes": 2,
  "num_edges": 1,
  "is_dag": true
}
```

### Error Response
```json
{
  "detail": "validation error"
}
```

## Next Steps

1. **Restart both services** after applying fixes
2. **Test connection** first, then pipeline submission
3. **Check console logs** for debugging
4. **Verify CORS headers** in network tab
5. **Remove debug panel** once working (optional)
