# fix_media_tags.py
import re

def fix_media_tags(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. {% media %} ko {% static %} mein change karein
    content = content.replace("{% media", "{% static")
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print("✅ All media tags fixed to static tags!")

# Run the fix
fix_media_tags('templates/index.html')
