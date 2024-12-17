import json
from database import Task, Session

def export_tasks(filename):
    session = Session()
    tasks = session.query(Task).all()
    tasks_list = [task.to_dict() for task in tasks]
    with open(filename, 'w') as f:
        json.dump(tasks_list, f)
    session.close()

def import_tasks(filename):
    session = Session()
    with open(filename, 'r') as f:
        tasks_list = json.load(f)

    for task_data in tasks_list:
        existing_task = session.query(Task).filter_by(title=task_data['title']).first()
        if not existing_task:
            task = Task(
                title=task_data['title'],
                description=task_data['description'],
                completed=task_data['completed']
            )
            session.add(task)
        else:
            print(f"La tarea '{task_data['title']}' ya existe.")
    
    session.commit()
    session.close()

