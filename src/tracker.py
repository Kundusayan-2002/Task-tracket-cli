from datetime import datetime

from .models import Task
from .storage import read_data, write_data
class taskTracker:
# read data from storage
  def __init__(self):
    self.tasks = read_data()

#add task
  def add(self,description: str) -> Task:
    new_task =Task(description,"pending")
    self.tasks.append(new_task)

    write_data(self.tasks)
    return new_task

#update task
  def update(self,id: str, description: str) -> Task:
    for task in self.tasks:
      if task.id == id:
        task.description = description
        task.updatedAt = datetime.now().isoformat()

    write_data(self.tasks)

#delete task
  def delete(self,id: str) -> None:
    for task in self.tasks:
      if task.id == id:
        self.tasks.remove(task)
        break

    write_data(self.tasks)

#toggle task status
  def toggle_status(self,id: str) -> Task:
    for task in self.tasks:
      if task.id == id:
        task.status = "pending" if task.status == "done" else "done"
        task.updatedAt = datetime.now().isoformat()

        write_data(self.tasks)
        return task.status
#list all tasks
  def list_all(self) -> list[Task]:
    return self.tasks      