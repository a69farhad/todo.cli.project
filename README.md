# To-Do CLI App (DevOps Project)

A simple CLI To-Do app that works both outside Docker and inside Docker, with data persisted in `data/tasks.json` via a Docker volume.

## Features
- `add "task description"` — add a task
- `list` — show all tasks with **stable IDs**
- `remove <ID>` — remove a task by ID
- Data persists in `data/tasks.json`

## Run locally (no Docker)
```bash
python3 todo.py add "Read a book"
python3 todo.py list
python3 todo.py remove 1
```

## Build Docker image
```bash
docker build -t todo-cli:latest .
```

## Option A — Pass arguments directly (uses ENTRYPOINT)
> Matches Task 4 (ENTRYPOINT): set up so the script accepts args via Docker.

```bash
# Mount local ./data to persist tasks
docker run --rm -v "$(pwd)/data:/app/data" todo-cli:latest add "Read a book"
docker run --rm -v "$(pwd)/data:/app/data" todo-cli:latest list
docker run --rm -v "$(pwd)/data:/app/data" todo-cli:latest remove 1
```

## Option B — **Interactive inside the container** (Updated Task 5)
> Recommended by the updated assignment: enter the container and run commands **inside**.

```bash
# Start an interactive shell with volume mounted
docker run -it --rm -v "$(pwd)/data:/app/data" --entrypoint /bin/bash todo-cli:latest

# Now inside the container:
python3 todo.py add "Read a book"
python3 todo.py list
python3 todo.py remove 1


## Option C — Docker Compose (interactive friendly)
```bash
docker-compose up -d
docker-compose exec todo bash     # enter the container
# then inside:
python3 todo.py list

