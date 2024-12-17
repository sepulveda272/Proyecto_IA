import streamlit as st
from database import Task, Session
from utils import export_tasks, import_tasks

def add_task(title, description):
    session = Session()
    new_task = Task(title=title, description=description)
    session.add(new_task)
    session.commit()
    session.close()

def get_all_tasks():
    session = Session()
    tasks = session.query(Task).all()
    session.close()
    return tasks

def mark_task_completed(task_id):
    session = Session()
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        task.completed = True
        session.commit()
    session.close()

def delete_completed_tasks():
    session = Session()
    session.query(Task).filter_by(completed=True).delete()
    session.commit()
    session.close()

st.title("Aplicación de Gestión de Tareas")

# Agregar tarea
st.header("Agregar Tarea")
title = st.text_input("Título de la tarea")
description = st.text_area("Descripción de la tarea")
if st.button("Agregar Tarea"):
    if title:
        add_task(title, description)
        st.success("Tarea agregada con éxito!")
    else:
        st.error("El título de la tarea es obligatorio.")

# Listar tareas
st.header("Lista de Tareas")
tasks = get_all_tasks()
for task in tasks:
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        st.write(f"**{task.title}**")
        st.write(task.description)
    with col2:
        if not task.completed:
            if st.button("Completar", key=f"complete_{task.id}"):
                mark_task_completed(task.id)
                st.rerun()
    with col3:
        st.write("Completada" if task.completed else "Pendiente")

# Eliminar tareas completadas
if st.button("Eliminar Tareas Completadas"):
    delete_completed_tasks()
    st.success("Tareas completadas eliminadas!")
    st.rerun()

# Exportar tareas
if st.button("Exportar Tareas"):
    export_tasks("tareas_exportadas.json")
    st.success("Tareas exportadas con éxito!")

# Importar tareas
uploaded_file = st.file_uploader("Importar Tareas", type="json")
if uploaded_file is not None:
    import_tasks(uploaded_file.name)
    st.success("Tareas importadas con éxito!")
    st.rerun()

