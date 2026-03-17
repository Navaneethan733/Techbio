import re
import os
import sys

def remove_comments(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine file type
    ext = os.path.splitext(file_path)[1].lower()

    if ext == '.html':
        # Remove HTML comments
        content = re.sub(r'<!--[\s\S]*?-->', '', content)
        # Also handle potential script/style blocks inside HTML
        # This is more complex, but for now we'll just handle HTML comments.
    elif ext == '.css':
        # Remove CSS block comments
        content = re.sub(r'/\*[\s\S]*?\*/', '', content)
    elif ext == '.js':
        # Remove JS block comments
        content = re.sub(r'/\*[\s\S]*?\*/', '', content)
        # Remove JS single line comments (careful with URLs)
        # This regex avoids matching // inside strings like "http://" or "file://"
        content = re.sub(r'(?<![:])//.*', '', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    for path in sys.argv[1:]:
        if os.path.exists(path):
            print(f"Cleaning {path}...")
            remove_comments(path)
        else:
            print(f"File not found: {path}")
