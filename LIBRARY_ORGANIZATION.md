# Library Organization Guide

## Rationale

Our `libraries/` directory contains over 8,000 files. To ensure maintainability and ease of browsing, all libraries are organized alphabetically into subdirectories.

## Structure

Libraries are organized as follows:

```
libraries/
├── a/          # A-1, A-2, A-3, A-4
├── b/          # B-1, B-2, B-3, B-4
├── c/          # C-1, C-2, C-3, C-4
├── ...
├── s/          # S-1, S-2, S-3, S-4
├── ...
├── z/          # Z-1, Z-2
├── symbols/    # Symbols-1, Symbols-2
└── nonenglish/ # NonEnglish-1, NonEnglish-2, NonEnglish-3
```

## Naming Convention

Each subdivision holds approximately 250-500 libraries:

- **A-1**: A-Ac (e.g., Aardvark, Abacus, Acacia)
- **A-2**: Ac-Aj (e.g., Acer, Acid, Ajour)
- **A-3**: Aj-Ar (e.g., Akan, Alam, Arbor)
- **A-4**: Ar-Az (e.g., Ariel, Arrow, Azimuth)

## Organization Status

The alphabetical subdivision is fully implemented across all sections (A-Z, Symbols, and Non-English).

## How to Browse

1. Use the main README's collapsible sections
2. Click on the subdivision links (e.g., [A-1], [S-3])
3. Each subdirectory is optimized for fast loading and easy browsing

## Adding New Libraries

When adding new libraries:

1. Determine the first letter of the library name
2. Find the appropriate subdivision based on the first 2 letters
3. Add the file to the correct subdirectory
4. Update the corresponding list file if needed

## File Naming

- All files use the format: `LibraryName.extension`
- Content is always: `print("Hello World")`
- Extensions match the library name for consistency

## Example

```
libraries/s/S-4/
├── Sandstone.sandstone
├── Sarcolite.sarcolite
├── Tephroite.tephroite
├── Uralite.uralite
└── Vesuvianite.vesuvianite
```

Each file contains:
```python
print("Hello World")
```
