# Pete & Drew's Boards - MVP

A clean, working interface for task and message management across Pete and Drew's boards.

## Features

✅ **Two Separate Boards**
- Pete's Board (purple theme)
- Drew's Board (green theme)

✅ **Full CRUD Operations**
- Create tasks with titles and descriptions
- Send messages
- View all tasks and messages
- Real-time status indicators

✅ **Clean UI**
- Modern, responsive design
- Tab-based navigation
- Status badges
- Time-relative timestamps

## Quick Start

### 1. Install Dependencies

```bash
cd /root/clawd/mvp
pip install -r requirements.txt
```

### 2. Start the Backend

```bash
cd /root/clawd/mvp/backend
python server.py
```

Server will start on `http://localhost:8000`

### 3. Open the Frontend

Open `/root/clawd/mvp/frontend/index.html` in your browser.

Or serve it with Python:

```bash
cd /root/clawd/mvp/frontend
python3 -m http.server 3000
```

Then visit `http://localhost:3000`

## API Endpoints

### Pete's Board
- `GET /api/pete/tasks` - Get all tasks
- `POST /api/pete/tasks` - Create task
- `GET /api/pete/messages` - Get messages
- `POST /api/pete/messages` - Send message

### Drew's Board
- `GET /api/drew/tasks` - Get all tasks
- `POST /api/drew/tasks` - Create task
- `GET /api/drew/messages` - Get messages
- `POST /api/drew/messages` - Send message

### System
- `GET /api/status` - System status

## Architecture

```
┌─────────────────┐
│   Frontend      │
│  (index.html)   │
└────────┬────────┘
         │ HTTP
         ▼
┌─────────────────┐
│   FastAPI       │
│   Backend       │
│  (server.py)    │
└────────┬────────┘
         │ REST API
         ▼
┌─────────────────┐
│   Supabase      │
│   Database      │
└─────────────────┘
```

## Testing

1. Create a task on Pete's Board
2. Send a message to Drew's Board
3. View tasks and messages in their respective tabs
4. Verify everything persists to Supabase

## What's Next

- [ ] WebSocket support for real-time updates
- [ ] Task status updates (inbox → in_progress → done)
- [ ] Priority filtering
- [ ] Search functionality
- [ ] User authentication
