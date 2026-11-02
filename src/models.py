from utils import generate_uid
from typing import Literal
import datetime
class Task:
  def __init__(
          self,
          description: str,
          status : Literal["todo", "in-progress", "done"] = "todo"
    ):
    self.id = generate_uid()
    self.description = description.strip()
    self.status = status
    now = datetime.datetime.now()
    self.updatedAt = now
    self.createdAt = now

class taskTracker:
  pass