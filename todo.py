#!/usr/bin/env python3
import json
import os
import sys
from typing import List, Dict

DATA_FILE = os.environ.get("TODO_DATA_FILE", "data/tasks.json")

def _ensure_storage():
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)

def _load() -> List[Dict]:
    _ensure_storage()
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
        except json.JSONDecodeError:
            return []

def _save(tasks: List[Dict]) -> None:
    _ensure_storage()
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)

def _next_id(tasks: List[Dict]) -> int:
    return (max([t.get("id", 0) for t in tasks]) + 1) if tasks else 1

def cmd_add(args: List[str]) -> None:
    if not args:
        print("Usage: add \"task description\"")
        return
    tasks = _load()
    task_text = " ".join(args).strip()
    tasks.append({"id": _next_id(tasks), "task": task_text})
    _save(tasks)
    print(f"Added: {task_text}")

def cmd_list(_args: List[str]) -> None:
    tasks = _load()
    if not tasks:
        print("No tasks.")
        return
    print("ID  Task")
    print("--  ----")
    for t in tasks:
        print(f"{t['id']:>2}  {t['task']}")

def cmd_remove(args: List[str]) -> None:
    if not args:
        print("Usage: remove <ID>")
        return
    try:
        target = int(args[0])
    except ValueError:
        print("ID must be an integer.")
        return
    tasks = _load()
    new_tasks = [t for t in tasks if t.get("id") != target]
    if len(new_tasks) == len(tasks):
        print(f"Task with ID {target} not found.")
        return
    _save(new_tasks)
    print(f"Removed task {target}.")

def main():
    if len(sys.argv) < 2:
        print("Usage:\n  add \"task description\"\n  list\n  remove <ID>")
        return
    command, *rest = sys.argv[1:]
    if command == "add":
        cmd_add(rest)
    elif command == "list":
        cmd_list(rest)
    elif command == "remove":
        cmd_remove(rest)
    else:
        print(f"Unknown command: {command}\nUse: add | list | remove")

if __name__ == "__main__":
    main()
