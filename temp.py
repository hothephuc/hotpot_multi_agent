import os
from pathlib import Path

def create_project_structure(root_path):
    """Create the complete project folder structure"""
    structure = {
        'backend': {
            'app': {
                'domain': ['models', 'repositories'],
                'application': ['services'],
                'infrastructure': {
                    'db': ['models', 'migrations'],
                    'langchain': [],
                    'ai': [],
                    'repositories': []
                },
                'presentation': ['api', 'schemas'],
                'main.py': None
            },
            'Dockerfile': None,
            'requirements.txt': None
        },
        'frontend': {
            'public': [],
            'src': {
                'assets': [],
                'components': [],
                'pages': [],
                'services': [],
                'App.jsx': None
            },
            'Dockerfile': None,
            'package.json': None
        },
        'docker-compose.yml': None,
        'README.md': None
    }
    
    def create_path(current_path, structure):
        for name, content in structure.items():
            new_path = current_path / name
            if content is None:  # It's a file
                new_path.touch()
                print(f"Created file: {new_path}")
            else:  # It's a directory
                new_path.mkdir(parents=True, exist_ok=True)
                print(f"Created directory: {new_path}")
                if isinstance(content, dict):
                    create_path(new_path, content)
                elif isinstance(content, list):
                    for subdir in content:
                        subdir_path = new_path / subdir
                        subdir_path.mkdir(parents=True, exist_ok=True)
                        print(f"Created directory: {subdir_path}")
    
    root = Path(root_path)
    root.mkdir(parents=True, exist_ok=True)
    print(f"Creating project structure at: {root}")
    create_path(root, structure)

if __name__ == "__main__":
    project_root = input("Enter the path where you want to create the project (or press Enter for current directory): ").strip()
    if not project_root:
        project_root = os.getcwd()
    create_project_structure(project_root)
    print("Project structure created successfully!")