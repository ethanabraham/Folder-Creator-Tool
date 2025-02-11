**Folder Creator Tool: Automate Folder Creation from Text File**

---

### README Template for GitHub:

```markdown
# 📂 Folder Creator Tool

A simple Python script to automate the creation of multiple folders based on folder names listed in a text file. This tool is perfect for developers, system administrators, or anyone who needs to quickly generate multiple directories.

---

## ✨ Features
- Reads folder names from a text file (`foldernames.txt`).
- Automatically creates folders in the current working directory.
- Skips empty lines and handles duplicate folder names gracefully.
- Provides clear error messages for invalid inputs or OS-related issues.
- Cross-platform compatibility (Windows, macOS, Linux).

---

## 🚀 How to Use

1. **Clone the Repository**:
   ```
   git clone https://github.com/YourUsername/folder-creator-tool.git
   cd folder-creator-tool
   ```

2. **Prepare the Input File**:
   - Create a file named `foldernames.txt` in the same directory as the script.
   - Add your desired folder names, one per line. Example:
     ```
     Project1
     Project2
     Logs
     Backups
     ```

3. **Run the Script**:
   - Execute the script using Python:
     ```
     python create_folders.py
     ```

4. **Output**:
   - The script will create folders in the current directory and notify you of the results:
     ```
     Folder 'Project1' created successfully.
     Folder 'Project2' created successfully.
     Folder 'Logs' created successfully.
     ```

---

## 🛠️ Requirements
- Python 3.x installed on your system.

---

## 📝 Example Output

For a `foldernames.txt` containing:
```
Project1
Project2
Logs
Backups
```

The script will generate these folders:
```
./Project1/
./Project2/
./Logs/
./Backups/
```

If you run it again, you'll see:
```
Folder 'Project1' already exists.
Folder 'Project2' already exists.
Folder 'Logs' already exists.
Folder 'Backups' already exists.
```

---

## 📂 Project Structure

```
folder-creator-tool/
│
├── create_folders.py       # The main Python script
├── foldernames.txt         # Input file containing folder names (to be created by user)
└── README.md               # Documentation for the project
```

---

## 🤝 Contributing

Contributions are welcome! If you have ideas for improvements or additional features, feel free to open an issue or submit a pull request.

---

## ⚖️ License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## 📧 Contact

Feel free to reach out if you have any questions or suggestions:

- GitHub: [YourUsername](https://github.com/ethanabraham)
- Email: your.email@ethanabraham.com
```
