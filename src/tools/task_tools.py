import json
import os
from typing import Optional
from langchain_core.tools import tool
from pydantic import BaseModel, Field

# --- Persistence Layer ---
TASKS_FILE = "todo_list.json"

def _load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def _save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

# --- Tool Inputs ---

class AddTaskInput(BaseModel):
    description: str = Field(..., description="The description of the task.")
    priority: str = Field("medium", description="Priority of the task: 'high', 'medium', 'low'.")

class UpdateTaskInput(BaseModel):
    task_id: int = Field(..., description="The ID of the task to update.")
    description: Optional[str] = Field(None, description="New description.")
    status: Optional[str] = Field(None, description="New status: 'pending', 'completed'.")
    priority: Optional[str] = Field(None, description="New priority.")

class DeleteTaskInput(BaseModel):
    task_id: int = Field(..., description="The ID of the task to delete.")

# --- Tool Implementations ---

@tool("add_task", args_schema=AddTaskInput)
def add_task(description: str, priority: str = "medium") -> str:
    """Adds a new task to the task list."""
    tasks = _load_tasks()
    new_id = 1 if not tasks else max(t['id'] for t in tasks) + 1
    new_task = {
        "id": new_id,
        "description": description,
        "priority": priority,
        "status": "pending"
    }
    tasks.append(new_task)
    _save_tasks(tasks)
    return f"Task added with ID {new_id}: {description}"

@tool("list_tasks")
def list_tasks() -> str:
    """Lists all tasks with their details."""
    tasks = _load_tasks()
    if not tasks:
        return "The task list is empty."
    
    result = "Current Tasks:\n"
    for t in tasks:
        result += f"[ID: {t['id']}] {t['description']} (Priority: {t['priority']}, Status: {t['status']})\n"
    return result

@tool("update_task", args_schema=UpdateTaskInput)
def update_task(task_id: int, description: str = None, status: str = None, priority: str = None) -> str:
    """Updates an existing task."""
    tasks = _load_tasks()
    for t in tasks:
        if t['id'] == task_id:
            if description: 
                t['description'] = description
            if status: 
                t['status'] = status
            if priority: 
                t['priority'] = priority
            _save_tasks(tasks)
            return f"Task {task_id} updated."
    return f"Error: Task with ID {task_id} not found."

@tool("delete_task", args_schema=DeleteTaskInput)
def delete_task(task_id: int) -> str:
    """Deletes a task by its ID."""
    tasks = _load_tasks()
    initial_count = len(tasks)
    tasks = [t for t in tasks if t['id'] != task_id]
    
    if len(tasks) < initial_count:
        _save_tasks(tasks)
        return f"Task {task_id} deleted."
    return f"Error: Task with ID {task_id} not found."
