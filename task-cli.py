#!/usr/bin/env python3
"""
Task Tracker CLI - A simple command-line task management application
Usage: python task_cli.py <command> [arguments]
"""

import json
import sys
import os
from datetime import datetime
from typing import List, Dict, Optional

class TaskTracker:
    def __init__(self, filename: str = "tasks.json"):
        self.filename = filename
        self.tasks = self._load_tasks()
    
    def _load_tasks(self) -> List[Dict]:
        """Load tasks from JSON file, create empty file if doesn't exist"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    return json.load(file)
            else:
                return []
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading tasks: {e}")
            return []
    
    def _save_tasks(self) -> bool:
        """Save tasks to JSON file"""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.tasks, file, indent=2)
            return True
        except IOError as e:
            print(f"Error saving tasks: {e}")
            return False
    
    def _get_next_id(self) -> int:
        """Get the next available task ID"""
        if not self.tasks:
            return 1
        return max(task['id'] for task in self.tasks) + 1
    
    def _find_task_by_id(self, task_id: int) -> Optional[Dict]:
        """Find a task by its ID"""
        for task in self.tasks:
            if task['id'] == task_id:
                return task
        return None
    
    def _get_current_timestamp(self) -> str:
        """Get current timestamp in ISO format"""
        return datetime.now().isoformat()
    
    def add_task(self, description: str) -> bool:
        """Add a new task"""
        if not description.strip():
            print("Error: Task description cannot be empty")
            return False
        
        task_id = self._get_next_id()
        current_time = self._get_current_timestamp()
        
        new_task = {
            'id': task_id,
            'description': description.strip(),
            'status': 'todo',
            'createdAt': current_time,
            'updatedAt': current_time
        }
        
        self.tasks.append(new_task)
        
        if self._save_tasks():
            print(f"Task added successfully (ID: {task_id})")
            return True
        return False
    
    def update_task(self, task_id: int, new_description: str) -> bool:
        """Update a task's description"""
        if not new_description.strip():
            print("Error: Task description cannot be empty")
            return False
        
        task = self._find_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found")
            return False
        
        task['description'] = new_description.strip()
        task['updatedAt'] = self._get_current_timestamp()
        
        if self._save_tasks():
            print(f"Task {task_id} updated successfully")
            return True
        return False
    
    def delete_task(self, task_id: int) -> bool:
        """Delete a task"""
        task = self._find_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found")
            return False
        
        self.tasks = [t for t in self.tasks if t['id'] != task_id]
        
        if self._save_tasks():
            print(f"Task {task_id} deleted successfully")
            return True
        return False
    
    def mark_task_status(self, task_id: int, status: str) -> bool:
        """Mark a task with a specific status"""
        valid_statuses = ['todo', 'in-progress', 'done']
        if status not in valid_statuses:
            print(f"Error: Invalid status '{status}'. Valid statuses are: {', '.join(valid_statuses)}")
            return False
        
        task = self._find_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found")
            return False
        
        task['status'] = status
        task['updatedAt'] = self._get_current_timestamp()
        
        if self._save_tasks():
            status_display = status.replace('-', ' ').title()
            print(f"Task {task_id} marked as {status_display}")
            return True
        return False
    
    def list_tasks(self, status_filter: Optional[str] = None) -> None:
        """List tasks, optionally filtered by status"""
        if status_filter:
            valid_statuses = ['todo', 'in-progress', 'done']
            if status_filter not in valid_statuses:
                print(f"Error: Invalid status filter '{status_filter}'. Valid filters are: {', '.join(valid_statuses)}")
                return
            
            filtered_tasks = [task for task in self.tasks if task['status'] == status_filter]
            status_display = status_filter.replace('-', ' ').title()
            print(f"\n{status_display} Tasks:")
        else:
            filtered_tasks = self.tasks
            print("\nAll Tasks:")
        
        if not filtered_tasks:
            print("No tasks found.")
            return
        
        print("-" * 60)
        for task in filtered_tasks:
            status_display = task['status'].replace('-', ' ').title()
            created_date = datetime.fromisoformat(task['createdAt']).strftime('%Y-%m-%d %H:%M')
            print(f"ID: {task['id']}")
            print(f"Description: {task['description']}")
            print(f"Status: {status_display}")
            print(f"Created: {created_date}")
            print("-" * 60)

def print_usage():
    """Print usage information"""
    usage = """
Task Tracker CLI - Usage:

Adding tasks:
    python task_cli.py add "Task description"

Updating tasks:
    python task_cli.py update <id> "New description"

Deleting tasks:
    python task_cli.py delete <id>

Marking task status:
    python task_cli.py mark-in-progress <id>
    python task_cli.py mark-done <id>
    python task_cli.py mark-todo <id>

Listing tasks:
    python task_cli.py list                 # All tasks
    python task_cli.py list done           # Completed tasks
    python task_cli.py list todo           # Todo tasks
    python task_cli.py list in-progress    # In-progress tasks

Examples:
    python task_cli.py add "Buy groceries"
    python task_cli.py update 1 "Buy groceries and cook dinner"
    python task_cli.py mark-in-progress 1
    python task_cli.py mark-done 1
    python task_cli.py delete 1
    python task_cli.py list
"""
    print(usage)

def main():
    """Main function to handle command-line arguments"""
    if len(sys.argv) < 2:
        print_usage()
        return
    
    tracker = TaskTracker()
    command = sys.argv[1].lower()
    
    try:
        if command == "add":
            if len(sys.argv) < 3:
                print("Error: Please provide a task description")
                print("Usage: python task_cli.py add \"Task description\"")
                return
            description = " ".join(sys.argv[2:])
            tracker.add_task(description)
        
        elif command == "update":
            if len(sys.argv) < 4:
                print("Error: Please provide task ID and new description")
                print("Usage: python task_cli.py update <id> \"New description\"")
                return
            try:
                task_id = int(sys.argv[2])
                new_description = " ".join(sys.argv[3:])
                tracker.update_task(task_id, new_description)
            except ValueError:
                print("Error: Task ID must be a number")
        
        elif command == "delete":
            if len(sys.argv) < 3:
                print("Error: Please provide task ID")
                print("Usage: python task_cli.py delete <id>")
                return
            try:
                task_id = int(sys.argv[2])
                tracker.delete_task(task_id)
            except ValueError:
                print("Error: Task ID must be a number")
        
        elif command == "mark-in-progress":
            if len(sys.argv) < 3:
                print("Error: Please provide task ID")
                print("Usage: python task_cli.py mark-in-progress <id>")
                return
            try:
                task_id = int(sys.argv[2])
                tracker.mark_task_status(task_id, "in-progress")
            except ValueError:
                print("Error: Task ID must be a number")
        
        elif command == "mark-done":
            if len(sys.argv) < 3:
                print("Error: Please provide task ID")
                print("Usage: python task_cli.py mark-done <id>")
                return
            try:
                task_id = int(sys.argv[2])
                tracker.mark_task_status(task_id, "done")
            except ValueError:
                print("Error: Task ID must be a number")
        
        elif command == "mark-todo":
            if len(sys.argv) < 3:
                print("Error: Please provide task ID")
                print("Usage: python task_cli.py mark-todo <id>")
                return
            try:
                task_id = int(sys.argv[2])
                tracker.mark_task_status(task_id, "todo")
            except ValueError:
                print("Error: Task ID must be a number")
        
        elif command == "list":
            status_filter = None
            if len(sys.argv) > 2:
                status_filter = sys.argv[2].lower()
            tracker.list_tasks(status_filter)
        
        else:
            print(f"Error: Unknown command '{command}'")
            print_usage()
    
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()