import os
import json
import shutil

# --- 設定 ---
SOURCE_DIR = '/tmp/leachim6-hello-world'
DEST_BASE = '/Users/afif/Documents/暇つぶしその１/polyglot-hello-world-collection'
LANG_DIR = os.path.join(DEST_BASE, 'languages')
LISTS_DIR = os.path.join(DEST_BASE, 'lists')

# --- カテゴリー定義と有名度スコア ---
FAMOUS_SCORES = {
    'Python': 100, 'JavaScript': 100, 'Java': 95, 'C': 95, 'C++': 90, 'C#': 90, 'PHP': 85, 'TypeScript': 85,
    'Swift': 80, 'Go': 80, 'Rust': 80, 'Ruby': 75, 'Kotlin': 75, 'SQL': 75, 'Dart': 70, 'Shell': 70, 
    'MATLAB': 65, 'R': 65, 'Objective-C': 65, 'Perl': 60, 'Scala': 60, 'Haskell': 50, 'Julia': 50, 'Lua': 50
}

LEGACY_LANGS = ['Fortran', 'Cobol', 'Algol', 'Pascal', 'Basic', 'Assembly', 'Lisp', 'Ada', 'Smalltalk', 'PL/I', 'Logo']
ESOTERIC_LANGS = ['Brainfuck', 'Malbolge', 'Befunge', 'Whitespace', 'Rockstar', 'Piet', 'Cow', 'Chicken']
RESEARCH_LANGS = ['Agda', 'Coq', 'Idris', 'Curry', 'Standard ML', 'OCaml', 'Erlang', 'Elixir']

def get_category(name):
    low = name.lower()
    if name in FAMOUS_SCORES: return 'Famous'
    if any(l.lower() in low for l in LEGACY_LANGS): return 'Legacy'
    if any(l.lower() in low for l in ESOTERIC_LANGS): return 'Esoteric'
    if any(l.lower() in low for l in RESEARCH_LANGS): return 'Research'
    return 'Minor'

def get_score(name):
    return FAMOUS_SCORES.get(name, 10 if get_category(name) != 'Minor' else 1)

def build():
    if os.path.exists(LISTS_DIR):
        shutil.rmtree(LISTS_DIR)
    os.makedirs(LISTS_DIR, exist_ok=True)
    os.makedirs(LANG_DIR, exist_ok=True)

    data = {'Famous': [], 'Legacy': [], 'Esoteric': [], 'Research': [], 'Minor': []}
    
    for letter in os.listdir(SOURCE_DIR):
        letter_path = os.path.join(SOURCE_DIR, letter)
        if not os.path.isdir(letter_path) or len(letter) != 1: continue
        
        for entry in os.listdir(letter_path):
            src_path = os.path.join(letter_path, entry)
            if not os.path.isfile(src_path): continue
            
            lang_name, ext = os.path.splitext(entry)
            ext_lower = ext.lstrip('.').lower()
            is_binary = ext_lower in ['catrobat', 'sb', 'sb2', 'sb3', 'png', 'jpg', 'jpeg', 'ti', 'zip']
            
            code = ""
            if not is_binary:
                try:
                    with open(src_path, 'r', encoding='utf-8') as f:
                        code = f.read().strip()
                except UnicodeDecodeError:
                    is_binary = True
                    code = "[Binary data]"

            cat = get_category(lang_name)
            item = {
                'name': lang_name,
                'ext': ext_lower,
                'code': code,
                'is_binary': is_binary,
                'score': get_score(lang_name),
                'path': f'languages/{lang_name}{ext}'
            }
            data[cat].append(item)
            
            dst_file = os.path.join(LANG_DIR, entry)
            if not os.path.exists(dst_file):
                shutil.copy2(src_path, dst_file)

    for cat in data:
        data[cat].sort(key=lambda x: (-x['score'], x['name']))

    category_order = [
        ('Famous', '有名言語'),
        ('Legacy', 'レガシー言語'),
        ('Esoteric', 'ジョーク言語'),
        ('Research', '研究用言語'),
        ('Minor', 'マイナー言語')
    ]
    
    all_pages = []
    CHUNK_SIZE = 50
    
    for cat_id, cat_name in category_order:
        items = data[cat_id]
        if not items: continue
        
        for j in range(0, len(items), CHUNK_SIZE):
            part_num = j // CHUNK_SIZE + 1
            chunk = items[j:j + CHUNK_SIZE]
            all_pages.append({
                'id': cat_id,
                'title': f'{cat_name} Part {part_num}' if len(items) > CHUNK_SIZE else f'{cat_name} カテゴリー',
                'items': chunk,
                'fname': f'{cat_id.lower()}_{part_num}.md' if len(items) > CHUNK_SIZE else f'{cat_id.lower()}.md'
            })

    for i, page in enumerate(all_pages):
        path = os.path.join(LISTS_DIR, page['fname'])
        prev_page = all_pages[i-1] if i > 0 else None
        next_page = all_pages[i+1] if i + 1 < len(all_pages) else None
        
        lines = [f"# {page['title']}", "", f"収録数: {len(page['items'])}", "", "---", ""]
        for item in page['items']:
            lines.append(f"## {item['name']}")
            if item['is_binary']:
                lines.append(f"> [!NOTE]\n> この言語のプログラムはバイナリまたは専用形式のため、ソースファイル自体をご確認ください。")
            else:
                lines.append(f"```{item['ext']}\n{item['code']}\n```")
            lines.append(f"[ソースファイル](../languages/{os.path.basename(item['path'])})")
            lines.append("")
        
        lines.append("---")
        nav = []
        if prev_page:
            nav.append(f"**[前のページ ({prev_page['title']})]({prev_page['fname']})**")
        if next_page:
            nav.append(f"**[次のページ ({next_page['title']})]({next_page['fname']})**")
        
        if nav:
            lines.append(" | ".join(nav))
        
        lines.append("")
        lines.append("[トップページへ戻る](../README.md)")
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write("\n".join(lines))

    with open(os.path.join(DEST_BASE, 'README.md'), 'w', encoding='utf-8') as f:
        f.write("# 究極の Hello World コレクション (1,000+ 言語)\n\n")
        f.write("世界中のあらゆるプログラミング言語のハローワールドを網羅した博物館です。\n\n")
        
        f.write("## 有名言語リスト\n")
        famous_items = data['Famous']
        for item in famous_items:
            f.write(f"### {item['name']}\n")
            if item['is_binary']:
                 f.write(f"> [!NOTE]\n> この言語のプログラムはバイナリまたは専用形式です。\n")
            else:
                 f.write(f"```{item['ext']}\n{item['code']}\n```\n")
            f.write(f"[ソースファイル](languages/{os.path.basename(item['path'])})\n\n")
        
        f.write("---\n")
        f.write("## その他のカテゴリー\n")
        f.write("さらに多くの言語を探索する：\n\n")
        
        linked_cats = []
        for cat_id, cat_name in category_order[1:]:
            first_page = next((p for p in all_pages if p['id'] == cat_id), None)
            if first_page:
                linked_cats.append(f"- [{cat_name} カテゴリー](lists/{first_page['fname']})")
        
        f.write("\n".join(linked_cats))
        f.write("\n")

if __name__ == '__main__':
    build()
    print("Build Complete!")
