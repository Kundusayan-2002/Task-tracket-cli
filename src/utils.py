# utility functions/tools for the task tracker CLI application
import uuid

def generate_uid() -> str:
  """
  This function generates a unique identifier using UUID.uui4.
  The output UID is a combination of first and last item from the uui4
  output.
  """
  parts = str(uuid.uuid4()).split("-") # Generate a unique identifier and return the first segment
  # print(parts)
  return "-".join((parts[0],parts[-1]))

print(generate_uid())