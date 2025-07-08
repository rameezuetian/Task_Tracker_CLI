# Task Tracker CLI

A simple command-line application to track and manage your tasks. Built with Python using only native libraries.

## Features

- ✅ Add, update, and delete tasks
- ✅ Mark tasks as todo, in-progress, or done
- ✅ List all tasks or filter by status
- ✅ Persistent storage using JSON file
- ✅ Automatic ID generation
- ✅ Timestamps for creation and updates
- ✅ Error handling and input validation

## Installation

1. Ensure you have Python 3.6 or higher installed
2. Download the `task_cli.py` file
3. Make it executable (optional): `chmod +x task_cli.py`

## Usage

### Adding Tasks
```bash
python task_cli.py add "Buy groceries"
# Output: Task added successfully (ID: 1)

python task_cli.py add "Complete project documentation"
# Output: Task added successfully (ID: 2)
```

### Updating Tasks
```bash
python task_cli.py update 1 "Buy groceries and cook dinner"
# Output: Task 1 updated successfully
```

### Deleting Tasks
```bash
python task_cli.py delete 1
# Output: Task 1 deleted successfully
```

### Managing Task Status

#### Mark as In Progress
```bash
python task_cli.py mark-in-progress 1
# Output: Task 1 marked as In Progress
```

#### Mark as Done
```bash
python task_cli.py mark-done 1
# Output: Task 1 marked as Done
```

#### Mark as Todo (reset status)
```bash
python task_cli.py mark-todo 1
# Output: Task 1 marked as Todo
```

### Listing Tasks

#### List All Tasks
```bash
python task_cli.py list
```

#### List Tasks by Status
```bash
# List completed tasks
python task_cli.py list done

# List todo tasks
python task_cli.py list todo

# List in-progress tasks
python task_cli.py list in-progress
```

## Task Properties

Each task contains the following properties:

- **id**: Unique identifier (auto-generated)
- **description**: Task description
- **status**: Current status (`todo`, `in-progress`, `done`)
- **createdAt**: ISO timestamp when task was created
- **updatedAt**: ISO timestamp when task was last modified

## Data Storage

- Tasks are stored in a `tasks.json` file in the current directory
- The file is automatically created if it doesn't exist
- Data persists between application runs

## Error Handling

The application handles various error scenarios:

- Invalid task IDs
- Missing or empty task descriptions
- Invalid status values
- File I/O errors
- Malformed JSON data

## Example Session

```bash
# Add some tasks
python task_cli.py add "Buy groceries"
# Task added successfully (ID: 1)

python task_cli.py add "Write documentation"
# Task added successfully (ID: 2)

python task_cli.py add "Review code"
# Task added successfully (ID: 3)

# Update a task
python task_cli.py update 1 "Buy groceries and cook dinner"
# Task 1 updated successfully

# Mark tasks with different statuses
python task_cli.py mark-in-progress 1
# Task 1 marked as In Progress

python task_cli.py mark-done 2
# Task 2 marked as Done

# List all tasks
python task_cli.py list

# List only completed tasks
python task_cli.py list done

# List only todo tasks
python task_cli.py list todo

# Delete a task
python task_cli.py delete 3
# Task 3 deleted successfully
```

## Development

### Project Structure
```
task-tracker-cli/
├── task_cli.py      # Main application file
├── README.md        # This file
└── tasks.json       # Data file (auto-generated)
```

### Running Tests
Test the application manually by running through the example commands above. The JSON file will be created automatically and you can inspect it to verify tasks are being stored correctly.

### Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Troubleshooting

**Q: I get a "command not found" error**
A: Make sure you're using `python task_cli.py` instead of just `task_cli.py`

**Q: Tasks aren't persisting between runs**
A: Check that the application has write permissions in the current directory

**Q: I get a JSON decode error**
A: The `tasks.json` file may be corrupted. You can delete it and start fresh, or restore from a backup

**Q: How do I backup my tasks?**
A: Simply copy the `tasks.json` file to a safe location

For additional help, run the application without arguments to see the usage information:
```bash
python task_cli.py
```
