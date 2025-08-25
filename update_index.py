# update_index.py

def update_index_page():
    with open('index.qmd', 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Logic to update the index.qmd goes here
    # For example, let's add a timestamp to the index.qmd
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content += f'\n\n**Last updated:** {timestamp}\n'
    
    with open('index.qmd', 'w', encoding='utf-8') as file:
        file.write(content)

if __name__ == "__main__":
    update_index_page()
