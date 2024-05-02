from markdown_blocks import markdown_to_html_node
from pathlib import Path
import os

def extract_title(markdown) -> str:
    lines = markdown.splitlines()  # Split the content into lines
    for line in lines:
        line = line.strip()  # Remove any leading/trailing whitespace
        if line.startswith('# '):  # Check if the line starts with '# '
            return line[2:]  # Return the title, removing the '# ' prefix
    # If no heading found, raise a custom exception
    raise Exception("No H1 Heading Found")

def read_file(file_path):
    """
    Reads an entire Markdown file and stores its contents in a variable.

    Args:
    file_path (str): The path to the Markdown file.

    Returns:
    str: The contents of the Markdown file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            output = file.read()  # Read the entire file into a variable
        return output
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

def write_to_file(content, filename):
    """
    Writes the given content to a specified file.

    Args:
    content (str): The content to write to the file.
    filename (str): The name of the file where the content will be written.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)  # Write the content to the file
        print(f"Content successfully written to {filename}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page {from_path} to {dest_path} using {template_path}")
    markdown = read_file(from_path)
    template = read_file(template_path)
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    write_to_file(content=template, filename=dest_path)

def generate_pages_recursively(dir_path_content, template_path, dest_dir_path):
    source_path = Path(dir_path_content)
    target_dir = Path(dest_dir_path)
    
    content_list = os.listdir(source_path)
    for content in content_list:
        md_file = source_path / content
        if os.path.isfile(md_file):
            html_file_path = target_dir / (content[:-3] + ".html")
            generate_page(md_file, template_path, html_file_path)
        else:
            new_directory = os.path.join(target_dir, content)
            os.makedirs(new_directory)
            generate_pages_recursively(os.path.join(source_path, content) , template_path, new_directory)            
        