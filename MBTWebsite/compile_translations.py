#!/usr/bin/env python3
"""
compile_translations.py - Pure Python PO to MO compiler for Django.
Generates valid GNU gettext binary MO files without needing GNU gettext installed.
"""

import os
import glob
import struct

def parse_po_file(filepath):
    """Parses a PO file and returns a dict mapping msgid -> msgstr."""
    entries = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.splitlines()
    cur_id = None
    cur_str = None
    state = None

    for line in lines:
        line_s = line.strip()
        if line_s.startswith('#'):
            continue
        if not line_s:
            if cur_id is not None and cur_str is not None:
                msgid = "".join(cur_id)
                msgstr = "".join(cur_str)
                entries[msgid] = msgstr
                cur_id = None
                cur_str = None
                state = None
            continue

        if line_s.startswith('msgid '):
            if cur_id is not None and cur_str is not None:
                entries["".join(cur_id)] = "".join(cur_str)
            raw = line_s[6:].strip()
            cur_id = [eval(raw)]
            cur_str = None
            state = 'msgid'
        elif line_s.startswith('msgstr '):
            raw = line_s[7:].strip()
            cur_str = [eval(raw)]
            state = 'msgstr'
        elif line_s.startswith('"') and line_s.endswith('"'):
            val = eval(line_s)
            if state == 'msgid':
                cur_id.append(val)
            elif state == 'msgstr':
                cur_str.append(val)

    if cur_id is not None and cur_str is not None:
        entries["".join(cur_id)] = "".join(cur_str)

    return entries


def generate_mo(po_entries):
    """Compiles po_entries dict into binary GNU gettext MO bytes."""
    valid_keys = [k for k in po_entries.keys() if k == '' or po_entries[k]]
    keys = sorted(valid_keys)

    num = len(keys)
    header_size = 7 * 4
    orig_table_offset = header_size
    trans_table_offset = orig_table_offset + num * 8
    strings_offset = trans_table_offset + num * 8

    orig_table = []
    trans_table = []
    orig_bytes = bytearray()
    trans_bytes = bytearray()

    cur_orig_off = strings_offset
    for k in keys:
        b_k = k.encode('utf-8') + b'\x00'
        orig_table.append((len(b_k) - 1, cur_orig_off))
        orig_bytes.extend(b_k)
        cur_orig_off += len(b_k)

    cur_trans_off = cur_orig_off
    for k in keys:
        v = po_entries[k]
        b_v = v.encode('utf-8') + b'\x00'
        trans_table.append((len(b_v) - 1, cur_trans_off))
        trans_bytes.extend(b_v)
        cur_trans_off += len(b_v)

    mo = bytearray()
    mo.extend(struct.pack('IIIIIII', 0x950412de, 0, num, orig_table_offset, trans_table_offset, 0, 0))
    for l, off in orig_table:
        mo.extend(struct.pack('II', l, off))
    for l, off in trans_table:
        mo.extend(struct.pack('II', l, off))
    mo.extend(orig_bytes)
    mo.extend(trans_bytes)
    return bytes(mo)


def compile_all(base_dir=None):
    if base_dir is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    locale_dir = os.path.join(base_dir, 'MBTApp', 'locale')
    po_files = sorted(glob.glob(os.path.join(locale_dir, '*', 'LC_MESSAGES', 'django.po')))
    
    print(f"Found {len(po_files)} PO files to compile:")
    for po_path in po_files:
        mo_path = po_path[:-3] + '.mo'
        entries = parse_po_file(po_path)
        mo_data = generate_mo(entries)
        with open(mo_path, 'wb') as f:
            f.write(mo_data)
        valid_count = sum(1 for k in entries if k == '' or entries[k])
        print(f" -> Compiled {po_path} -> {mo_path} ({valid_count} entries)")

if __name__ == '__main__':
    compile_all()
