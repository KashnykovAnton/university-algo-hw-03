import os
import shutil
import argparse

def recursive_copy(src_dir, dest_dir):

    for item in os.listdir(src_dir):
        item_path = os.path.join(src_dir, item)
        if os.path.isdir(item_path):
            recursive_copy(item_path, dest_dir)
        else:
            try:
                extension = os.path.splitext(item)[1][1:] or "no_extension"
                dest_subdir = os.path.join(dest_dir, extension)
                os.makedirs(dest_subdir, exist_ok=True)
                shutil.copy(item_path, dest_subdir)
                print(f"Copied '{item}' to '{dest_subdir}'")
            except Exception as e:
                print(f"Error copying '{item}': {e}")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Recursively copy files and sort them by extension.")
    parser.add_argument("source_dir", help="Path to the source directory")
    parser.add_argument("destination_dir", nargs="?", default="dist", help="Path to the destination directory (default: dist)")
    return parser.parse_args()

def main():
    args = parse_arguments()

    source_dir = args.source_dir
    dest_dir = args.destination_dir

    if not os.path.isdir(source_dir):
        print(f"Error: '{source_dir}' is not a directory.")
        return

    os.makedirs(dest_dir, exist_ok=True)
    recursive_copy(source_dir, dest_dir)

if __name__ == "__main__":
    main()

# Run the script with the following command:
# python3 task_01.py test_for_task_01/source_dir test_for_task_01/destination_dir