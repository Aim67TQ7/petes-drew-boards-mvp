#!/usr/bin/env python3
"""
Pete & Drew's Boards - MVP Backend
Simple FastAPI server to interface with Supabase boards
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional, List
import os
import httpx
from datetime import datetime

# Load environment variables
from dotenv import load_dotenv
load_dotenv('/root/clawd/.env.pete')

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_SERVICE_KEY')

if not SUPABASE_URL or not SUPABASE_KEY:
    raise RuntimeError("Missing Supabase credentials in .env.pete")

app = FastAPI(title="Pete & Drew's Boards API", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class Task(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = "inbox"
    priority: Optional[str] = "medium"

class Message(BaseModel):
    content: str
    sender: str = "user"

# Helper function for Supabase requests
async def supabase_request(method: str, endpoint: str, data: dict = None):
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json"
    }
    url = f"{SUPABASE_URL}/rest/v1/{endpoint}"
    
    async with httpx.AsyncClient() as client:
        if method == "GET":
            response = await client.get(url, headers=headers)
        elif method == "POST":
            headers["Prefer"] = "return=representation"
            response = await client.post(url, headers=headers, json=data)
        elif method == "PATCH":
            headers["Prefer"] = "return=representation"
            response = await client.patch(url, headers=headers, json=data)
        else:
            raise ValueError(f"Unsupported method: {method}")
        
        response.raise_for_status()
        return response.json()

# Pete's Board Endpoints
@app.get("/api/pete/tasks")
async def get_pete_tasks(status: Optional[str] = None):
    """Get Pete's tasks"""
    endpoint = "tasks?select=*&order=created_at.desc"
    if status:
        endpoint += f"&status=eq.{status}"
    return await supabase_request("GET", endpoint)

@app.post("/api/pete/tasks")
async def create_pete_task(task: Task):
    """Create a new task for Pete"""
    data = {
        "title": task.title,
        "description": task.description,
        "status": task.status,
        "priority": task.priority,
        "created_at": datetime.utcnow().isoformat()
    }
    return await supabase_request("POST", "tasks", data)

@app.patch("/api/pete/tasks/{task_id}")
async def update_pete_task(task_id: str, status: str):
    """Update Pete task status"""
    endpoint = f"tasks?id=eq.{task_id}"
    data = {"status": status}
    return await supabase_request("PATCH", endpoint, data)

@app.get("/api/pete/messages")
async def get_pete_messages(limit: int = 20):
    """Get Pete's messages"""
    endpoint = f"messages?select=*&order=created_at.desc&limit={limit}"
    return await supabase_request("GET", endpoint)

@app.post("/api/pete/messages")
async def create_pete_message(message: Message):
    """Send a message to Pete's board"""
    data = {
        "content": message.content,
        "sender": message.sender,
        "created_at": datetime.utcnow().isoformat()
    }
    return await supabase_request("POST", "messages", data)

# Drew's Board Endpoints
@app.get("/api/drew/tasks")
async def get_drew_tasks(status: Optional[str] = None):
    """Get Drew's tasks"""
    endpoint = "drew_tasks?select=*&order=created_at.desc"
    if status:
        endpoint += f"&status=eq.{status}"
    return await supabase_request("GET", endpoint)

@app.post("/api/drew/tasks")
async def create_drew_task(task: Task):
    """Create a new task for Drew"""
    data = {
        "title": task.title,
        "description": task.description,
        "status": task.status,
        "priority": task.priority,
        "created_at": datetime.utcnow().isoformat()
    }
    return await supabase_request("POST", "drew_tasks", data)

@app.patch("/api/drew/tasks/{task_id}")
async def update_drew_task(task_id: str, status: str):
    """Update Drew task status"""
    endpoint = f"drew_tasks?id=eq.{task_id}"
    data = {"status": status}
    return await supabase_request("PATCH", endpoint, data)

@app.get("/api/drew/messages")
async def get_drew_messages(limit: int = 20):
    """Get Drew's messages"""
    endpoint = f"drew_messages?select=*&order=created_at.desc&limit={limit}"
    return await supabase_request("GET", endpoint)

@app.post("/api/drew/messages")
async def create_drew_message(message: Message):
    """Send a message to Drew's board"""
    data = {
        "content": message.content,
        "sender": message.sender,
        "created_at": datetime.utcnow().isoformat()
    }
    return await supabase_request("POST", "drew_messages", data)

# System Status
@app.get("/api/status")
async def get_status():
    """Get system status"""
    pete_tasks = await supabase_request("GET", "tasks?select=*")
    pete_messages = await supabase_request("GET", "messages?select=*")
    drew_tasks = await supabase_request("GET", "drew_tasks?select=*")
    drew_messages = await supabase_request("GET", "drew_messages?select=*")
    
    return {
        "pete": {
            "tasks": len(pete_tasks),
            "messages": len(pete_messages),
            "inbox": len([t for t in pete_tasks if t.get('status') == 'inbox'])
        },
        "drew": {
            "tasks": len(drew_tasks),
            "messages": len(drew_messages),
            "inbox": len([t for t in drew_tasks if t.get('status') == 'inbox'])
        }
    }

# Serve static files
@app.get("/")
async def root():
    return {"message": "Pete & Drew's Boards API", "docs": "/docs"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
