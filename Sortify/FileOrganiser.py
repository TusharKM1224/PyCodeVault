"""
File Organizer (Sortify) - A comprehensive file organization system

This script organizes files in a directory by categorizing them into folders based on their extensions.
It supports both default and custom folder naming schemes, preserves organization schemas in JSON files,
and provides interactive customization options.

Key Features:
- Intelligent file categorization by extension
- Customizable folder naming schemes
- Schema persistence for future use
- Interactive user interface
- Safety checks to prevent system directory organization
- Progress feedback and logging

Author: Tushar
Version: 2.0
"""

import os
import shutil
import json
import time
import sys
from typing import Dict, List, Tuple, Optional, Set, Union


class FileOrganizer:
    """
    A comprehensive file organization system that categorizes files into folders based on their extensions.
    
    Attributes:
        DEFAULT_SCHEMA (str): Filename for default schema
        CUSTOM_SCHEMA (str): Filename for custom schema
        CUSTOM_FOLDER_KEY (str): Key for custom parent folder in schema
        DEFAULT_FOLDER_KEY (str): Key for default parent folder in schema
        DEFAULT_APP_NAME (str): Name of the application executable
    """
    
    def __init__(self, user_response: str) -> None:
        """
        Initialize the file organizer with user preferences.
        
        Args:
            user_response: User input ('y' to organize current directory)
        """
        # Configuration constants
        self.DEFAULT_SCHEMA = "DefaultNamingSchema.json"
        self.CUSTOM_SCHEMA = "CustomNamingSchema.json"
        self.CUSTOM_FOLDER_KEY = "CustomParentFolder"
        self.DEFAULT_FOLDER_KEY = "ParentFolder"
        self.DEFAULT_APP_NAME = "Sortify.exe"
        
        # Show initialization animation
        self._show_loading_animation(iterations=50, message="Initializing File Organizer...")
        
        # Process user response
        if user_response.lower() == "y":
            self._process_current_directory()
        else:
            print("Organizing other directories is coming soon!")

    # --------------------------
    # Core Organization Methods
    # --------------------------

    def _process_current_directory(self) -> None:
        """Handle the organization process for the current directory."""
        existing_schema = self._check_existing_schema()
        
        if not existing_schema:
            self._setup_new_organization()
        else:
            self._use_existing_schema(existing_schema)

    def _setup_new_organization(self) -> None:
        """Set up a new organization schema for the directory."""
        parent_folder_name = input(
            '\nPlease provide a folder name for organizing your files\n'
            '(or press "n" to use default name): '
        )
        
        if parent_folder_name.lower() != "n":
            self._create_custom_schema(parent_folder_name)
        else:
            self._create_default_schema()

    def _create_custom_schema(self, folder_name: str) -> None:
        """
        Create a custom organization schema.
        
        Args:
            folder_name: Name for the custom parent folder
        """
        custom_schema = self._create_or_update_schema(
            custom_folder=folder_name + "/", 
            key=self.CUSTOM_FOLDER_KEY
        )
        
        self._show_loading_animation(iterations=20)
        
        if not custom_schema:
            print(f"Error: Could not create custom folder '{folder_name}'")
        else:
            print(f"Custom folder created: {custom_schema[self.CUSTOM_FOLDER_KEY]}")
            self._organize_files(custom_schema)

    def _create_default_schema(self) -> None:
        """Create and use the default organization schema."""
        default_schema = self._create_or_update_schema()
        self._organize_files(default_schema)

    def _use_existing_schema(self, schema: Dict) -> None:
        """
        Use an existing organization schema.
        
        Args:
            schema: Existing organization schema
        """
        print("Existing organization schema detected...")
        self._show_loading_animation(iterations=35, message="Loading schema...")
        self._organize_files(schema)

    # --------------------------
    # File Processing Methods
    # --------------------------

    def _organize_files(self, naming_schema: Dict) -> None:
        """
        Main file organization method.
        
        Args:
            naming_schema: Schema mapping extensions to folder names
        """
        self._clear_screen()
        current_dir = os.getcwd()

        # Safety check to prevent organizing system directories
        if self._is_system_directory(current_dir):
            print("Error: Organization of system directories is not allowed.")
            return
            
        items = os.listdir()
        self._remove_excluded_items(items)
        
        if not items:
            print("No files found to organize.")
            return
        
        # Process files and extensions
        folders, files = self._separate_files_and_folders(items)
        extensions = self._get_file_extensions(files)
        
        # Get user customization
        naming_schema, was_customized = self._get_user_customization(extensions, naming_schema)
        
        # Update schema files if customized
        if was_customized:
            self._update_schema_files(naming_schema)
        
        print("Creating folder structure...")
        self._show_loading_animation(iterations=10, message="Creating folders...")
        
        # Create folder structure mapping
        folder_structure = self._create_folder_structure(extensions, naming_schema)
        
        # Get parent folder from schema
        parent_folder = self._get_parent_folder(naming_schema)
        
        # Verify parent folder exists
        if not self._verify_parent_folder(parent_folder, folders, naming_schema):
            return
        
        # Perform the actual file organization
        self._move_files_to_folders(parent_folder, files, folder_structure)

    def _separate_files_and_folders(self, items: List[str]) -> Tuple[List[str], List[str]]:
        """
        Separate files from folders in a directory listing.
        
        Args:
            items: List of items in directory
            
        Returns:
            Tuple containing (list_of_folders, list_of_files)
        """
        files = []
        folders = []
        
        for item in items:
            if os.path.isfile(item):
                files.append(item)
            elif os.path.isdir(item):
                folders.append(item)
                
        return folders, files

    def _get_file_extensions(self, files: List[str]) -> Set[str]:
        """
        Extract unique file extensions from a list of files.
        
        Args:
            files: List of file paths
            
        Returns:
            Set of unique file extensions (including dots, e.g. '.txt')
        """
        return {os.path.splitext(file)[1] for file in files}

    def _create_folder_structure(self, extensions: Set[str], naming_schema: Dict) -> Dict:
        """
        Create mapping of extensions to folder names based on schema.
        
        Args:
            extensions: Set of file extensions found
            naming_schema: Current naming schema
            
        Returns:
            Mapping of extensions to their destination folders
        """
        return {ext: naming_schema[ext] for ext in extensions if ext in naming_schema}

    # --------------------------
    # User Interaction Methods
    # --------------------------

    def _get_user_customization(self, extensions: Set[str], schema: Dict) -> Tuple[Dict, bool]:
        """
        Interactive customization of folder naming schema.
        
        Args:
            extensions: Set of file extensions found
            schema: Current naming schema
            
        Returns:
            Tuple containing (updated_schema, was_customized)
        """
        new_extensions = [ext for ext in extensions if ext not in schema]
        was_customized = False
        
        # Option to view current naming schema
        if self._get_user_choice("View current folder naming schema? (y/n): "):
            self._display_schema(schema)
            
            # Option to modify existing schema
            if self._get_user_choice("Modify existing folder names? (y/n): "):
                was_customized = self._customize_existing_folders(schema)
        
        # Handle new extensions not in current schema
        if new_extensions:
            was_customized = self._handle_new_extensions(new_extensions, schema) or was_customized
            
        return schema, was_customized

    def _display_schema(self, schema: Dict) -> None:
        """
        Display the current naming schema to the user.
        
        Args:
            schema: Current naming schema
        """
        print("\nCurrent Folder Naming Schema:")
        for ext, folder in schema.items():
            if ext not in [self.CUSTOM_FOLDER_KEY, self.DEFAULT_FOLDER_KEY]:
                print(f"  {ext:8} → {folder}")

    def _customize_existing_folders(self, schema: Dict) -> bool:
        """
        Handle customization of existing schema entries.
        
        Args:
            schema: Current naming schema
            
        Returns:
            True if changes were made
        """
        print("\nAvailable file extensions:", list(schema.keys()))
        print("(Note: Parent folder names cannot be changed)")
        
        try:
            num_changes = int(input("How many folder names would you like to change? "))
        except ValueError:
            print("Invalid input. No changes will be made.")
            return False
            
        was_customized = False
        
        for i in range(1, num_changes + 1):
            ext = input(f"Enter extension #{i} to modify (e.g. '.txt'): ")
            
            if ext in [self.CUSTOM_FOLDER_KEY, self.DEFAULT_FOLDER_KEY]:
                print("Error: Cannot change parent folder name.")
            elif ext not in schema:
                print(f"Error: Extension '{ext}' not in schema.")
            else:
                new_name = input(f"Enter new folder name for {ext}: ")
                if self._rename_folder(schema[ext], new_name, schema):
                    print(f"Folder renamed successfully.")
                
                schema[ext] = new_name
                was_customized = True
                
        return was_customized

    def _handle_new_extensions(self, new_extensions: List[str], schema: Dict) -> bool:
        """
        Handle new file extensions not in current schema.
        
        Args:
            new_extensions: List of new extensions found
            schema: Current naming schema
            
        Returns:
            True (changes are always made for new extensions)
        """
        print(f"\nFound {len(new_extensions)} new file type(s):")
        
        for ext in new_extensions:
            new_name = input(f"Enter folder name for {ext} files: ")
            schema[ext] = new_name
            
        print("\nCustom naming schema updated for future use.")
        self._show_loading_animation(iterations=20, message="Saving schema...")
        
        return True

    # --------------------------
    # File Operations Methods
    # --------------------------

    def _rename_folder(self, old_name: str, new_name: str, schema: Dict) -> bool:
        """
        Rename a folder within the organization structure.
        
        Args:
            old_name: Current folder name
            new_name: New folder name
            schema: Current naming schema
            
        Returns:
            True if rename was successful
        """
        parent_folder = (
            schema[self.CUSTOM_FOLDER_KEY] 
            if self.CUSTOM_FOLDER_KEY in schema 
            else schema[self.DEFAULT_FOLDER_KEY]
        )
        
        old_path = os.path.join(parent_folder, old_name)
        new_path = os.path.join(parent_folder, new_name)
        
        if os.path.isdir(old_path):
            os.rename(old_path, new_path)
            return True
        return False

    def _move_files_to_folders(self, parent_folder: str, files: List[str], folder_structure: Dict) -> None:
        """
        Organize files into their respective folders.
        
        Args:
            parent_folder: Parent folder path
            files: List of files to organize
            folder_structure: Mapping of extensions to folders
        """
        self._clear_screen()
        print("File Organization Log:")
        
        existing_folders = os.listdir(parent_folder)
        all_success = True
        
        for ext, folder_name in folder_structure.items():
            time.sleep(0.5)  # Small delay for better user experience
            
            # Get files for current extension
            ext_files = [f for f in files if os.path.splitext(f)[1] == ext]
            
            # Create folder if needed
            dest_path = os.path.join(parent_folder, folder_name)
            if folder_name not in existing_folders:
                print(f"Creating folder: {folder_name}")
                os.makedirs(dest_path, exist_ok=True)
            
            # Move files
            success, failed = self._move_files(dest_path, ext_files)
            
            if success:
                print(f"  {len(ext_files)} {ext} files → {folder_name}")
            else:
                print(f"  Error moving {len(failed)} {ext} files")
                all_success = False
        
        if all_success:
            print("\nAll files organized successfully!")
        else:
            print("\nCompleted with some errors.")

    def _move_files(self, destination: str, files: List[str]) -> Tuple[bool, Optional[List[str]]]:
        """
        Move files to destination folder with error handling.
        
        Args:
            destination: Destination folder path
            files: List of file paths to move
            
        Returns:
            Tuple: (success, failed_files)
        """
        failed = []
        
        for file in files:
            try:
                shutil.move(file, destination)
            except Exception as e:
                print(f"Error moving {file}: {str(e)}")
                failed.append(file)
        
        return (True, None) if not failed else (False, failed)

    # --------------------------
    # Schema Management Methods
    # --------------------------

    def _create_or_update_schema(self, custom_folder: Optional[str] = None, key: Optional[str] = None) -> Optional[Dict]:
        """
        Create or update the naming schema dictionary.
        
        Args:
            custom_folder: Optional custom parent folder name
            key: Optional key for custom parent folder
            
        Returns:
            Created/updated naming schema, or None on error
        """
        default_schema = {
            ".py": "Python Files",
            ".ipynb": "Jupyter Notebooks",
            ".java": "Java Files",
            ".cpp": "C++ Files",
            ".c": "C Files",
            ".html": "HTML Files",
            ".css": "CSS Files",
            ".js": "JavaScript Files",
            ".txt": "Text Files",
            ".pdf": "PDFs",
            ".docx": "Word Documents",
            ".pptx": "PowerPoint Files",
            ".xlsx": "Excel Files",
            ".zip": "Archives",
            ".rar": "Archives",
            ".mp3": "Audio",
            ".mp4": "Videos",
            ".avi": "Videos",
            ".mkv": "Videos",
            ".png": "Images",
            ".jpg": "Images",
            ".jpeg": "Images",
            ".gif": "GIFs",
            ".bmp": "Images",
            ".svg": "SVG Images",
            "ParentFolder": "Organized_Files/"
        }
        
        try:
            if custom_folder and key:
                return self._create_custom_schema_file(default_schema, custom_folder, key)
            return self._create_default_schema_file(default_schema)
        except Exception as e:
            print(f"Error creating schema: {str(e)}")
            return None

    def _create_custom_schema_file(self, default_schema: Dict, folder_name: str, key: str) -> Dict:
        """
        Create a custom schema file.
        
        Args:
            default_schema: Default schema template
            folder_name: Custom parent folder name
            key: Key for custom parent folder
            
        Returns:
            Custom naming schema
        """
        custom_schema = default_schema.copy()
        del custom_schema["ParentFolder"]
        custom_schema[key] = folder_name
        
        # Clean up old schema files
        self._cleanup_schema_files()
        
        # Save new schema
        with open(self.CUSTOM_SCHEMA, "w") as f:
            json.dump(custom_schema, f, indent=4)
        
        # Create parent folder
        os.makedirs(custom_schema[key], exist_ok=True)
        return custom_schema

    def _create_default_schema_file(self, default_schema: Dict) -> Dict:
        """
        Create default schema file.
        
        Args:
            default_schema: Default schema template
            
        Returns:
            Default naming schema
        """
        # Clean up old schema files
        self._cleanup_schema_files()
        
        # Save default schema
        with open(self.DEFAULT_SCHEMA, "w") as f:
            json.dump(default_schema, f, indent=4)
        
        # Create parent folder
        os.makedirs(default_schema["ParentFolder"], exist_ok=True)
        return default_schema

    def _cleanup_schema_files(self) -> None:
        """Remove existing schema files if they exist."""
        for schema_file in [self.CUSTOM_SCHEMA, self.DEFAULT_SCHEMA]:
            if os.path.exists(schema_file):
                os.remove(schema_file)

    def _check_existing_schema(self) -> Optional[Dict]:
        """
        Check if directory was previously organized by looking for schema files.
        
        Returns:
            Existing naming schema if found, None otherwise
        """
        for schema_file in [self.DEFAULT_SCHEMA, self.CUSTOM_SCHEMA]:
            if os.path.exists(schema_file):
                with open(schema_file, "r") as f:
                    return json.load(f)
        return None

    def _update_schema_files(self, schema: Dict) -> None:
        """
        Update schema files after customization.
        
        Args:
            schema: Updated naming schema
        """
        if self.DEFAULT_FOLDER_KEY in schema:
            schema[self.CUSTOM_FOLDER_KEY] = schema.pop(self.DEFAULT_FOLDER_KEY)
            if os.path.exists(self.DEFAULT_SCHEMA):
                os.remove(self.DEFAULT_SCHEMA)
        
        with open(self.CUSTOM_SCHEMA, "w") as f:
            json.dump(schema, f, indent=4)

    # --------------------------
    # Utility Methods
    # --------------------------

    def _show_loading_animation(self, iterations: int = 50, message: str = "Processing") -> None:
        """
        Display a console loading animation.
        
        Args:
            iterations: Number of animation frames
            message: Message to display
        """
        animation = "|/-\\|"
        for i in range(iterations):
            time.sleep(0.1)
            sys.stdout.write("\r" + message + animation[i % len(animation)])
            sys.stdout.flush()
        print()

    def _remove_excluded_items(self, items: List[str]) -> None:
        """
        Remove excluded items from processing list.
        
        Args:
            items: List of items to filter
        """
        for item in [self.CUSTOM_SCHEMA, self.DEFAULT_SCHEMA, self.DEFAULT_APP_NAME]:
            if item in items:
                items.remove(item)

    def _get_parent_folder(self, schema: Dict) -> str:
        """
        Get the parent folder from naming schema.
        
        Args:
            schema: Current naming schema
            
        Returns:
            Parent folder path
        """
        return (
            schema[self.CUSTOM_FOLDER_KEY] 
            if self.CUSTOM_FOLDER_KEY in schema 
            else schema[self.DEFAULT_FOLDER_KEY]
        )

    def _verify_parent_folder(self, parent_folder: str, existing_folders: List[str], schema: Dict) -> bool:
        """
        Verify parent folder exists or handle its absence.
        
        Args:
            parent_folder: Parent folder path
            existing_folders: List of existing folders
            schema: Current naming schema
            
        Returns:
            True if parent folder exists or was handled
        """
        if parent_folder.split("/")[0] not in existing_folders:
            print("\nParent folder not found.")
            print("Suggestion: Create a new schema and organize again.")
            
            if self._get_user_choice("Would you like to create a new schema? (y/n): "):
                schema_file = self.CUSTOM_SCHEMA if self.CUSTOM_FOLDER_KEY in schema else self.DEFAULT_SCHEMA
                if os.path.exists(schema_file):
                    os.remove(schema_file)
                self.__init__("y")
                return False
            
            print("Organization aborted.")
            return False
        return True

    def _is_system_directory(self, path: str) -> bool:
        """
        Check if a path is a system directory that shouldn't be organized.
        
        Args:
            path: Directory path to check
            
        Returns:
            True if path is a system directory
        """
        return path.lower().startswith(("c:\\", "c:/"))

    def _clear_screen(self) -> None:
        """Clear the console screen."""
        os.system("cls" if os.name == "nt" else "clear")

    def _get_user_choice(self, prompt: str) -> bool:
        """
        Get a yes/no choice from the user.
        
        Args:
            prompt: Question to display
            
        Returns:
            True if user answered 'y', False otherwise
        """
        while True:
            choice = input(prompt).lower()
            if choice in ('y', 'n'):
                return choice == 'y'
            print("Please enter 'y' or 'n'.")


def display_welcome() -> None:
    """Display welcome message and instructions."""
    print("\n" + "="*50)
    print("Welcome to Sortify - File Organization Tool")
    print("="*50)
    print("\nThis tool will organize files in the current directory")
    print("by categorizing them into folders based on file types.")
    print("\nTip: Run this in the directory you want to organize.")

def display_motivational_quote() -> None:
    """Display a motivational quote."""
    quotes = [
        "The secret of getting ahead is getting started. - Mark Twain",
        "Productivity is being able to do things you were never able to do before. - Franz Kafka",
        "For every minute spent organizing, an hour is earned. - Benjamin Franklin"
    ]
    print("\n" + "~"*50)
    print("Today's Motivation:")
    print(quotes[0])
    print("~"*50)

def main() -> None:
    """Main entry point for the application."""
    display_welcome()
    display_motivational_quote()
    
    # Start the file organizer
    FileOrganizer("y")
    
    print("\nThank you for using Sortify!")
    print("Your files are now organized and easy to find.")
    print("\nExiting in 5 seconds...")
    time.sleep(5)

if __name__ == "__main__":
    main()