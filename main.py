import sys
from pathlib import Path
from PIL import Image

def _convert_jpg_to_png(image_folder, converted_folder):
    target_directory = converted_folder
    for file in image_folder.iterdir():
        if file.is_file() and (file.suffix.casefold() == '.jpg' or file.suffix.casefold() == '.jpeg'):
            target_filepath = target_directory / file.name
            new_folder = target_filepath.with_suffix('.png')

            im = Image.open(file)
            try:
                im.save(new_folder, "PNG")
            except OSError:
                raise
    print(f"Successfully converted files into folder: {target_directory}")

def _handle_directory_validation(folder):
    folder = Path(folder)

    if folder.exists() and folder.is_dir():
        print(f'{folder} exists and is a directory')
        return folder
    elif folder.exists() and not folder.is_dir():
        print(f'{folder} exists but it is not a directory')
        raise FileExistsError
    else:
        try:
            folder.mkdir(parents=False, exist_ok=False)
            print(f'{folder} successfully created')
        except FileNotFoundError:
            raise
        except FileExistsError:
            raise

def check_folders(source, destination):
    s = _handle_directory_validation(source)
    d = _handle_directory_validation(destination)

    _convert_jpg_to_png(s, d)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <source folder> <destination folder>")
        sys.exit(1)

    source_folder = sys.argv[1]
    destination_folder = sys.argv[2]

    check_folders(source_folder, destination_folder)