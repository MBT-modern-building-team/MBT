#!/usr/bin/env python3
"""
update_all_po.py - Updates django.po files for cs, de, en, hu, sk, uk
with comprehensive translations and repairs truncated strings, then compiles all MO files.
"""

import os
import re
import json
import glob

from compile_translations import parse_po_file, generate_mo, compile_all
import translations_data
import extra_translations

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOCALE_DIR = os.path.join(BASE_DIR, 'MBTApp', 'locale')
TARGET_LANGS = ['cs', 'de', 'en', 'hu', 'sk', 'uk']

def format_po_entry(msgid, msgstr):
    """Formats msgid and msgstr into valid PO format."""
    def escape_str(s):
        return json.dumps(s, ensure_ascii=False)

    lines = []
    if "\n" in msgid:
        lines.append('msgid ""')
        for part in msgid.splitlines(keepends=True):
            lines.append(escape_str(part))
    else:
        lines.append(f'msgid {escape_str(msgid)}')

    if "\n" in msgstr:
        lines.append('msgstr ""')
        for part in msgstr.splitlines(keepends=True):
            lines.append(escape_str(part))
    else:
        lines.append(f'msgstr {escape_str(msgstr)}')

    return "\n".join(lines) + "\n\n"


def update_po_files():
    all_data = {}
    all_data.update(translations_data.DATA)
    all_data.update(extra_translations.EXTRA_DATA)
    print(f"Total translation entries in catalog: {len(all_data)}")

    for lang in TARGET_LANGS:
        po_path = os.path.join(LOCALE_DIR, lang, 'LC_MESSAGES', 'django.po')
        if not os.path.exists(po_path):
            print(f"PO file not found: {po_path}")
            continue

        existing_entries = parse_po_file(po_path)

        # Header entry
        header_text = existing_entries.get('', (
            f"Project-Id-Version: 1.0\\n"
            f"Report-Msgid-Bugs-To: \\n"
            f"POT-Creation-Date: 2026-03-24 12:00+0000\\n"
            f"PO-Revision-Date: 2026-11-17 12:00+0000\\n"
            f"Last-Translator: MBT Team\\n"
            f"Language: {lang}\\n"
            f"MIME-Version: 1.0\\n"
            f"Content-Type: text/plain; charset=UTF-8\\n"
            f"Content-Transfer-Encoding: 8bit\\n"
        ))

        # Merge translations
        merged = dict(existing_entries)
        new_count = 0
        updated_count = 0

        for msgid, trans_dict in all_data.items():
            if lang in trans_dict and trans_dict[lang]:
                val = trans_dict[lang]
                if msgid not in merged or not merged[msgid]:
                    new_count += 1
                elif merged[msgid] != val:
                    updated_count += 1
                merged[msgid] = val

        # Ensure header is preserved
        merged[''] = header_text

        # Sort entries: header first, then alphabetical by msgid
        sorted_keys = [''] + sorted([k for k in merged.keys() if k != ''])

        # Write out PO file
        output_content = "#\n"
        for k in sorted_keys:
            output_content += format_po_entry(k, merged[k])

        with open(po_path, 'w', encoding='utf-8') as f:
            f.write(output_content)

        filled_count = sum(1 for k in sorted_keys if k == '' or merged[k])
        print(f"[{lang.upper()}] Updated {po_path}: {new_count} new, {updated_count} updated, {filled_count} total entries.")

    # Now compile all MO files
    print("\nCompiling all MO files...")
    compile_all(BASE_DIR)


if __name__ == '__main__':
    update_po_files()
