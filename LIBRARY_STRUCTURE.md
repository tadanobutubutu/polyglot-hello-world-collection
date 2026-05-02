# Repository Structure

## Overview

```
polyglot-hello-world-collection/
├── README.md                      # Main entry point with collapsible sections
├── LIBRARY_ORGANIZATION.md        # Detailed organization guide
├── LIBRARY_STRUCTURE.md           # This file - visual tree
├── LICENSE.md                     # MIT License
│
├── languages/                     # ~50 actual programming languages
│   ├── C.c
│   ├── Python.py
│   └── ...
│
├── libraries/                     # ⚠️ LEGACY: ~8,000 files (being migrated)
│   ├── Abenakiite.abenakiite
│   ├── Zektzerite.zektzerite
│   └── ... (truncated by GitHub)
│
├── libraries/a/                   # NEW: Libraries A
│   ├── A-1/                     # A-Ac (~250 files)
│   ├── A-2/                     # Ac-Aj (~250 files)
│   ├── A-3/                     # Aj-Ar (~250 files)
│   └── A-4/                     # Ar-Az (~250 files)
│
├── libraries/b/                   # NEW: Libraries B
│   ├── B-1/                     # B-Be
│   ├── B-2/                     # Be-Bo
│   ├── B-3/                     # Bo-Br
│   └── B-4/                     # Br-Bz
│
├── libraries/c/ through libraries/y/  # Similar structure
│
├── libraries/z/                   # NEW: Libraries Z
│   ├── Z-1/                     # Z-Zi
│   └── Z-2/                     # Zi-Zz
│
├── libraries/symbols/             # NEW: Symbol/Number libraries
│   ├── Symbols-1/               # 0-9
│   └── Symbols-2/               # !@#$%^&*
│
├── libraries/nonenglish/          # NEW: Non-English named libraries
│   ├── NonEnglish-1/            # Asian languages
│   ├── NonEnglish-2/            # European languages
│   └── NonEnglish-3/            # Others
│
└── lists/                         # Categorized language lists
    ├── modern.md
    ├── legacy.md
    ├── esoteric.md
    ├── research.md
    ├── minor_a-i.md
    ├── minor_j-r.md
    └── minor_s-z.md
```

## File Count by Section

| Directory | Status | Estimated Files | Subdivisions |
|-----------|--------|-----------------|--------------|
| languages/ | Stable | ~50 | N/A |
| libraries/ | ⚠️ Migrating | ~8,000 | Too many |
| libraries/a/ | Active | ~800 | 4 subdivisions |
| libraries/b/ | Active | ~600 | 4 subdivisions |
| libraries/s/ | Active | ~1,200 | 4 subdivisions |
| libraries/z/ | Active | ~200 | 2 subdivisions |
| libraries/symbols/ | Active | ~100 | 2 subdivisions |
| libraries/nonenglish/ | Active | ~300 | 3 subdivisions |

## GitHub Limitations

- **1000 files per directory**: GitHub truncates directory listings at 1,000 entries
- **Solution**: Alphabetical subdivision keeps each directory under 500 files
- **Browsing**: Use README's collapsible sections or direct links to subdirectories

## Navigation Tips

1. Start at README.md
2. Find your letter in the Libraries section
3. Click the subdivision (e.g., S-3 for Se-So)
4. Browse files in that subdirectory

## Migration Timeline

- **Phase 1**: Create new structure ✅ (In Progress)
- **Phase 2**: Migrate high-traffic letters (A, S) 🔄 (In Progress)
- **Phase 3**: Migrate remaining letters ⏳
- **Phase 4**: Archive legacy libraries/ directory ⏳
