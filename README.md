# TaskManagerAgent

TaskManagerAgent is a Python-based task management assistant designed to help users efficiently organize, manage, and interact with their to-do lists. It utilizes advanced LLM (Large Language Model) technology, along with Chainlit and LangChain for building, debugging, and enhancing applications. With TaskManagerAgent, users can add, update, list, and delete tasks seamlessly.

---

### Demo Video
<video controls>
    <source src="agent-demo.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>

---

## Table of Contents
- [Features](#features)
- [Setup](#setup)
  - [Pre-requisites](#pre-requisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
- [Usage](#usage)
  - [Command Line (CLI)](#command-line-cli)
  - [Chat Interface](#chat-interface)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Add Tasks:** Add tasks to your to-do list with descriptions, priorities, and statuses.
- **List Tasks:** View all tasks systematically organized with details such as ID, priority, and status.
- **Update Tasks:** Modify the details of your tasks to keep them up-to-date.
- **Delete Tasks:** Remove tasks from your list when they are no longer relevant.
- **Safe Calculations:** Perform simple arithmetic operations safely to manage calculations during task planning.
- **System Tools:** Built-in utilities for tasks like fetching system time and operating system information.

---

## Setup

### Pre-requisites

Ensure you have the following installed:
- Python 3.8 or higher
- Virtualenv (`pip install virtualenv`)
- [Chainlit](https://docs.chainlit.io)
- Environment variables for external integrations (see below)

---

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/dhruv-0707/taskManagerAgent.git
   cd taskManagerAgent
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   For CLI:
   ```bash
   python main.py
   ```
   For chat-based interface:
   ```bash
   chainlit run app.py -w
   ```

---

### Environment Variables

TaskManagerAgent relies on external APIs and requires some environment variables to be set. Create a `.env` file in the root directory and add the following (replace placeholders with actual values):

```
API_KEY=<your-api-key>
```

---

## Usage

### Command Line (CLI)

Launch the CLI application using:
```bash
python main.py
```

Example commands:
- Add a task: `Add a task to buy groceries`
- List tasks: `List my tasks`
- Update a task: `Mark task 1 as completed`
- Delete a task: `Delete task 1`

### Chat Interface

You can also interact with TaskManagerAgent through the Chainlit chat interface. Start the chat by running:
```bash
chainlit run app.py -w
```

You will be greeted by the assistant with: 
"Hello! I am your Task Management Agent. How can I help you today?"

---

## Project Structure

```plaintext
taskManagerAgent/
    ├── app.py - Entry point for the Chainlit chat interface version of the Task Manager
    ├── main.py - Command line interface (CLI) entry point
    ├── chainlit.md - Configurations for the Chainlit welcome page
    ├── src/
    │   ├── agent/
    │   │   ├── core.py - Core logic for creating and managing the task management agent
    │   └── tools/
    │       ├── task_tools.py - Task-related functionalities such as add, list, update, and delete
    │       └── system_tools.py - System utilities like safe calculations and system info
```

---

## Contributing

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b my-new-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add some feature"
   ```
4. Push to the branch:
   ```bash
   git push origin my-new-feature
   ```
5. Open a Pull Request.

---

## Author

Created by [dhruv-0707](https://github.com/dhruv-0707). Feel free to reach out for feedback or collaboration opportunities!

