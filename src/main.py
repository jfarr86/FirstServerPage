import os
import shutil

from copystatic import copy_files_recursive
from generate_page import generate_pages_recursively


dir_path_static = "./static"
dir_path_public = "./public"
content_path = os.path.join("./content/")
template_pth = os.path.join("./template.html")
dest_pth = os.path.join("./public/")

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
    generate_pages_recursively(content_path, template_pth, dest_pth)
    
main()