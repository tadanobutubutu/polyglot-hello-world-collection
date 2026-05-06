import os
import json
import shutil

# Load TIO languages
tio_langs = set()
try:
    with open('tio_languages.json', 'r') as f:
        tio_langs_data = json.load(f)
        for key, val in tio_langs_data.items():
            name = val.get('name', '').lower()
            tio_langs.add(name)
except Exception as e:
    print(f"Error loading TIO languages: {e}")

# Load Leachim6 Source of Truth
# Map: lowercase_name -> (original_path, code)
truth_map = {}
truth_root = 'source_of_truth_leachim6'
for root, dirs, files in os.walk(truth_root):
    if '.git' in root or '.github' in root:
        continue
    for file in files:
        if file.lower() in ['readme.md', '.editorconfig', '.gitignore', 'license', 'contributing.md', 'update_list.py']:
            continue
        lang_name = os.path.splitext(file)[0].lower()
        file_path = os.path.join(root, file)
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                code = f.read()
            truth_map[lang_name] = (file, code)
        except:
            pass

placeholder_content = 'print("Hello World")\n'

stats = {
    "corrected": 0,
    "deleted": 0,
    "kept_valid": 0,
    "unknown_placeholders": []
}

# Iterate and Repair
for root, dirs, files in os.walk('libraries'):
    for file in files:
        if file == 'README.md' or 'BATCH' in file:
            continue
            
        file_path = os.path.join(root, file)
        lang_name = os.path.splitext(file)[0].lower()
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            is_placeholder = (content == placeholder_content)
            
            # 1. Match with Truth Map
            if lang_name in truth_map:
                truth_filename, truth_code = truth_map[lang_name]
                if content != truth_code:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(truth_code)
                    stats["corrected"] += 1
                else:
                    stats["kept_valid"] += 1
                continue
            
            # 2. Check if it's a known TIO language but we don't have code in Truth Map
            if lang_name in tio_langs:
                if is_placeholder:
                    # It's a real language but we have a placeholder. 
                    # We should keep it for now but flag for manual/web search check.
                    stats["kept_valid"] += 1
                else:
                    # It's a real language and has custom code. Keep it.
                    stats["kept_valid"] += 1
                continue
            
            # 3. If it's a placeholder and NOT in Truth Map or TIO
            if is_placeholder:
                # Likely a fake language
                os.remove(file_path)
                stats["deleted"] += 1
            else:
                # Unknown language but has custom code. Keep it.
                stats["kept_valid"] += 1
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

print(f"Summary:")
print(f"  Corrected (from Leachim6): {stats['corrected']}")
print(f"  Deleted (unverified placeholders): {stats['deleted']}")
print(f"  Kept/Valid: {stats['kept_valid']}")
