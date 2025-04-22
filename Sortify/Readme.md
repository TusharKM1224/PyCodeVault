

# Welcome to Sortify - File Organization Tool


![File Organization](https://www.flaticon.com/free-icon/folder_16247929?term=file+manager&page=1&position=41&origin=search&related_id=16247929)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)


A powerful Python tool to automatically organize your files by categorizing them into folders based on their extensions.

## ⚠️ Important Warnings

1. **System Protection**: The tool will **not** organize system directories (like C: drive) for safety reasons.
2. **File Movement**: Files will be physically moved to new locations. Original folder structure will be altered.
3. **Schema Persistence**: The tool remembers your preferences for future use via JSON schema files.
4. **No Undo**: There is no built-in undo functionality. Consider backing up important files before organizing.

## ✨ Features

- Automatically sorts files by extension
- Supports both default and custom folder naming schemes
- Interactive customization for unrecognized file types
- Preserves your organization preferences for future use
- Visual progress indicators and logging
- Safety checks to prevent accidental system modifications

## 📁 Default Folder Structure

The tool comes with pre-defined folders for common file types:

| Extension | Folder Name          |
|-----------|----------------------|
| .py       | Python Files         |
| .ipynb    | Jupyter Notebooks    |
| .java     | Java Files           |
| .cpp      | C++ Files            |
| .html     | HTML Files           |
| .css      | CSS Files            |
| .js       | JavaScript Files     |
| .txt      | Text Files           |
| .pdf      | PDFs                 |
| .docx     | Word Documents       |
| .pptx     | PowerPoint Files     |
| .xlsx     | Excel Files          |
| .zip      | Archives             |
| .rar      | Archives             |
| .mp3      | Audio                |
| .mp4      | Videos               |
| .avi      | Videos               |
| .mkv      | Videos               |
| .png      | Images               |
| .jpg      | Images               |
| .jpeg     | Images               |
| .gif      | GIFs                 |
| .bmp      | Images               |
| .svg      | SVG Images           |

## 🛠️ How It Works

1. **Initialization**:
   - Checks for existing organization schema
   - Creates new schema if none exists

2. **Customization**:
   - For unrecognized file extensions, prompts user for folder name
   - Allows modification of existing folder names
   - Saves customizations for future use

3. **Organization**:
   - Creates necessary folder structure
   - Moves files to appropriate folders
   - Provides detailed operation log

## 🚀 Usage

1. Run the script in the directory you want to organize:
   ```bash
   python sortify.py
   or
   Run Sortify.exe
   ```

2. Follow the interactive prompts:
   - Choose to use default or custom parent folder
   - Customize folder names for file types
   - Review operation log

3. Your files will be organized into the folder structure!

## 🔧 Customization Options

1. **Parent Folder**:
   - Default: "Organized_Files/"
   - Can specify custom name

2. **Folder Names**:
   - Modify existing folder names
   - Add names for new file types

3. **Schema Files**:
   - `DefaultNamingSchema.json` - Default configuration
   - `CustomNamingSchema.json` - Your custom configuration

## ⚡ Example Workflow



==========================================

Found 3 new file types:
Enter folder name for .psd files: Photoshop Files
Enter folder name for .ai files: Illustrator Files
Enter folder name for .indd files: InDesign Files

Creating folder structure...
Moving files:
  5 .jpg files → Images
  3 .docx files → Word Documents
  2 .psd files → Photoshop Files
  1 .ai file → Illustrator Files

Organization complete!


## 📜 License

This project is open-source and available under the MIT License.

## 🙏 Credits

Developed with ❤️ by Tushar

---

**Note**: Always back up important files before running organization tools!

