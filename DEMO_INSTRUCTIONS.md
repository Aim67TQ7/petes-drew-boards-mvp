# 🎯 Pete & Drew's Boards - MVP Demo Instructions

## ✅ System Status

**Backend:** Running on `http://localhost:8000` (process started via start-server.sh)
**Frontend:** Ready at `/root/clawd/mvp/frontend/index.html`

## 🚀 Quick Start Guide

### Option 1: Direct File Access

1. Open in browser:
   ```
   file:///root/clawd/mvp/frontend/index.html
   ```

2. API endpoint is configured to `http://localhost:8000/api`

### Option 2: HTTP Server (Recommended)

1. Start frontend server:
   ```bash
   cd /root/clawd/mvp/frontend
   python3 -m http.server 3000
   ```

2. Visit in browser:
   ```
   http://localhost:3000
   ```

## 📋 Testing Checklist

### Pete's Board

- [ ] View existing tasks
- [ ] Create new task ("Build amazing features")
- [ ] Send message to Pete
- [ ] Verify data appears in Supabase

### Drew's Board

- [ ] View existing tasks
- [ ] Create new task ("Design cool interfaces")
- [ ] Send message to Drew
- [ ] Verify separate storage from Pete's data

### Integration Test

- [ ] Create task on both boards simultaneously
- [ ] Verify they don't interfere with each other
- [ ] Check timestamp formatting
- [ ] Test tab navigation

## 🔍 API Endpoints Available

```
# Pete's Board
GET  /api/pete/tasks         - List all tasks
POST /api/pete/tasks         - Create task
GET  /api/pete/messages      - List messages
POST /api/pete/messages      - Send message

# Drew's Board
GET  /api/drew/tasks         - List all tasks
POST /api/drew/tasks         - Create task
GET  /api/drew/messages      - List messages
POST /api/drew/messages      - Send message

# System
GET  /api/status             - System status
GET  /docs                   - Interactive API docs
```

## 📊 Current Data

**Pete's Board:**
- 64 tasks total
- 262 messages total
- 0 in inbox (all processed!)

**Drew's Board:**
- 1 task total
- 9 messages total
- 0 in inbox

## 🎨 Features Implemented

✅ **Clean UI**
- Gradient purple/magenta background
- Two-column grid layout (Pete left, Drew right)
- Tab-based navigation (Tasks | Messages | Create)
- Responsive design for mobile

✅ **Task Management**
- Create tasks with title + description
- View all tasks with status badges
- Time-relative timestamps ("2m ago", "5h ago")

✅ **Messaging**
- Send messages to either board
- Sender attribution (user/pete/drew)
- Chronological message feed

✅ **Backend Integration**
- FastAPI REST API
- Supabase persistence
- Proper error handling
- CORS enabled

## 🛠️ Technical Stack

**Frontend:**
- Vanilla HTML/CSS/JavaScript
- No frameworks (zero dependencies!)
- Fetch API for HTTP requests
- Grid + Flexbox layouts

**Backend:**
- FastAPI (Python)
- HTTPX for Supabase requests
- python-dotenv for config
- Uvicorn ASGI server

**Database:**
- Supabase PostgreSQL
- Tables: tasks, messages, drew_tasks, drew_messages

## 🚧 Next Steps (Not Yet Implemented)

- [ ] WebSocket support for real-time updates
- [ ] Task status updates (move from inbox → in_progress → done)
- [ ] Priority filtering
- [ ] Search functionality
- [ ] User authentication
- [ ] File attachments

## 📝 Notes

- Backend runs via `/root/clawd/mvp/start-server.sh`
- Logs available at `/tmp/mvp-server.log`
- Virtual environment at `/root/clawd/mvp/venv`
- All env vars loaded from `/root/clawd/.env.pete`

## 🔄 Restarting Services

**Backend:**
```bash
pkill -f "python server.py"
nohup /root/clawd/mvp/start-server.sh > /tmp/mvp-server.log 2>&1 &
```

**Frontend:**
```bash
cd /root/clawd/mvp/frontend
python3 -m http.server 3000
```

## 🎉 Success Criteria

✅ Backend API responds on port 8000
✅ Frontend loads without errors
✅ Can create tasks on both boards
✅ Can send messages on both boards
✅ Data persists to Supabase
✅ UI is clean and professional
✅ Tab navigation works smoothly

---

**MVP delivered!** 🚀

For questions or issues, check:
1. Backend logs: `tail -f /tmp/mvp-server.log`
2. API docs: `http://localhost:8000/docs`
3. Supabase tables via dashboard
