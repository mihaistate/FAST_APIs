from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
    
tasks = []
    
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks 

@app.get("/tasks/task_id/", response_model=Task)
def get_tasks(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task.id 
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks", response_model=Task)
def set_task(task: Task):
    tasks.append(task)
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(updated_task: int, task_id: int):
    for  id, task in enumerate(tasks):
        if task.id == task_id:
            tasks[id] = updated_task
            return updated_task    
    raise HTTPException(status_code=404, detail= "Task not updated")

@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(delete_id: int):
    for id, task in enumerate(tasks):
        if task.id == delete_id:
            del tasks[id]
            return {"mesage:", "Task deleted successfully"}
    raise HTTPException(status_code=404, detail = "Task not found")           
            