import os
import shutil
from gencontent import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def copy_directory(source, destination):
    if not os.path.exists(source):
        print(f"Source directory '{source}' does not exist.")
        return
    
    if os.path.exists(destination):
        shutil.rmtree(destination)
        print(f"Deleted the destination directory '{destination}'.")

    os.mkdir(destination)
    print(f"Created the destination directory '{destination}'.")

    _copy_contents(source, destination)


def _copy_contents(source, destination):
    items = os.listdir(source)

    for item in items:
        src_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)

        if os.path.isdir(src_path):
            os.mkdir(dest_path)
            print(f"Created directory '{dest_path}'.")
            _copy_contents(src_path, dest_path)
        else:
            shutil.copy(src_path, dest_path)
            print(f"Copied file '{src_path}' to '{dest_path}'.")


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_directory(dir_path_static, dir_path_public)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)

main()
