from models import TaskCreate, TaskUpdate, TaskResponse, Priority, Status
from datetime import datetime
from typing import Dict, List, Optional

class TaskDB:
    def __init__(self):
        self.tasks: Dict[int, dict] = {}
        self.counter = 1

    def create(self, user_id: int, task: TaskCreate) -> dict:
        now = datetime.now()
        task_dict = {
            "id": self.counter,
            "title": task.title,
            "description": task.description,
            "priority": task.priority,
            "status": task.status,
            "created_at": now,
            "updated_now": now,
            "user_id": user_id
        }

        self.tasks[self.counter] = task_dict
        self.counter += 1
        return task_dict
    
    def get_all(self, 
                user_id: int, 
                skip: int = 0, 
                limit: int = 10,
                status: Optional[str] = None) -> List[dict]:
        user_tasks = [t for t in self.tasks.values() if t["user_id"] == user_id]
        user_tasks = [t for t in self.tasks.values() if t["status"] == status]

        return user_tasks[skip:skip:limit]

