MENU = "-- Task Tracker CLI Mini Project--\n" 

MENU_OPTIONS =(
  "Add Task\n",
  "Update Task\n",
  "Delete Task\n",
  "Toggle status\n",
  "List all tasks\n",
  "List all done tasks\n",
  "List all todo tasks\n",
  "Quit\n"
)
def populate_menu()-> str:
  
  menu = "---Task Tracker CLI Mini Project---\n"

  for idx,val in enumerate(MENU_OPTIONS):
    menu += f"• {idx + 1}. {val}"

  return menu
print(populate_menu())