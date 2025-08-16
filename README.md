# Python JPG to PNG Converter

A simple yet robust Python command-line utility for batch converting JPG and JPEG images to PNG format.

---

## Description

This project provides a practical command-line tool designed to streamline image format conversion. It efficiently processes all `.jpg` and `.jpeg` files within a specified source directory, converting them to `.png` format and saving them into a designated destination folder. The tool leverages modern Python features like `pathlib` for intuitive file system operations and `Pillow` (PIL) for image manipulation, demonstrating strong principles of modularity, robust error handling, and adherence to the DRY (Don't Repeat Yourself) principle through well-structured functions. It's built for reliability, ensuring proper directory validation and graceful management of file system conflicts.

---

## Getting Started

### Dependencies

* **Python 3.x:** (Tested with Python 3.8+)
* **Pillow Library:** A powerful image processing library for Python.
* **Operating System:** Cross-platform (Windows, macOS, Linux).

### Installing

1.  **Clone the Repository:**
    Download or clone this repository to your local machine.

2.  **Install Pillow:**
    Open your terminal or command prompt and navigate to the project directory. Then, install the Pillow library using pip:
    ```bash
    pip install Pillow
    ```

### Executing Program

1.  **Prepare your folders:**
    * Have a **source folder** containing your `.jpg` or `.jpeg` images.
    * Decide on a **destination folder** where you want the converted `.png` files to be saved. This folder will be created by the script if it doesn't already exist.

2.  **Run the script from your terminal/command prompt:**
    Navigate to the directory where you've saved `your_script_name.py` (or whatever you've named your Python file, e.g., `converter.py`).
    Execute the script, providing the source and destination folder paths as arguments:

    ```bash
    python your_script_name.py <source_folder_path> <destination_folder_path>
    ```
    * Replace `<source_folder_path>` with the actual path to your source images folder.
    * Replace `<destination_folder_path>` with the desired path for your converted PNGs.

    **Example:**
    ```bash
    python converter.py my_jpg_images converted_pngs
    ```
    (This assumes `my_jpg_images` and `converted_pngs` are in the same directory as the script, or you provide full paths like `C:\Users\YourName\Desktop\my_jpg_images`)

---

## Help

* **"Usage: python script.py <source folder> <destination folder>"**: This message appears if you don't provide exactly two arguments (source and destination paths) when running the script. Ensure you specify both.
* **`FileExistsError` (e.g., "exists but it is not a directory")**: This error occurs if you provide a path that already exists, but it's a file (not a folder). The script cannot proceed because it expects a directory or a non-existent path. You'll need to either delete/rename the conflicting file or choose a different path.
* **`FileNotFoundError`**: This error typically happens if you've set `parents=False` in `mkdir()` (which is the current setting in `_handle_directory_validation`) and a parent directory in your specified path doesn't exist. Ensure all intermediate directories leading up to your target folder exist, or consider modifying the `parents` argument in the script if you want it to create all missing parent directories.
* **`OSError` (during image conversion/saving)**: While the script attempts to catch basic OS errors during saving, issues like insufficient disk space, corrupted source images, or specific file permissions problems might trigger this. Check your disk space, image integrity, and folder permissions if this occurs.

---

## Authors

Simon Valenzuela 
[GitHub](https://github.com/CaptSV)
[LinkedIn](https://www.linkedin.com/in/simonrpvalenzuela/)

---

## Version History

* 0.2
    * Refactored directory validation into a dedicated helper function for improved modularity and DRY principles.
    * Enhanced error handling for directory creation and file conflicts.
    * Improved clarity of path handling with `pathlib` methods.
* 0.1
    * Initial Release: JPG to PNG conversion functionality with basic command-line argument parsing.

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.
---

## Acknowledgments

Inspiration and template for this README file adapted from:
* [Dom Pizzie's README Template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
