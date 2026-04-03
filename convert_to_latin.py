#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skripta za konverziju HTML stranica sa ćirilice na latinicu
"""

import os
import re

# Mapiranje ćirilica -> latinica
CYRILLIC_TO_LATIN = {
    'А': 'A', 'а': 'a',
    'Б': 'B', 'б': 'b',
    'В': 'V', 'в': 'v',
    'Г': 'G', 'г': 'g',
    'Д': 'D', 'д': 'd',
    'Ђ': 'Đ', 'ђ': 'đ',
    'Е': 'E', 'е': 'e',
    'Ж': 'Ž', 'ж': 'ž',
    'З': 'Z', 'з': 'z',
    'И': 'I', 'и': 'i',
    'Ј': 'J', 'ј': 'j',
    'К': 'K', 'к': 'k',
    'Л': 'L', 'л': 'l',
    'Љ': 'Lj', 'љ': 'lj',
    'М': 'M', 'м': 'm',
    'Н': 'N', 'н': 'n',
    'Њ': 'Nj', 'њ': 'nj',
    'О': 'O', 'о': 'o',
    'П': 'P', 'п': 'p',
    'Р': 'R', 'р': 'r',
    'С': 'S', 'с': 's',
    'Т': 'T', 'т': 't',
    'Ћ': 'Ć', 'ћ': 'ć',
    'У': 'U', 'у': 'u',
    'Ф': 'F', 'ф': 'f',
    'Х': 'H', 'х': 'h',
    'Ц': 'C', 'ц': 'c',
    'Ч': 'Č', 'ч': 'č',
    'Џ': 'Dž', 'џ': 'dž',
    'Ш': 'Š', 'ш': 'š',
}

def cyrillic_to_latin(text):
    """Konvertuje tekst sa ćirilice na latinicu"""
    result = []
    for char in text:
        if char in CYRILLIC_TO_LATIN:
            result.append(CYRILLIC_TO_LATIN[char])
        else:
            result.append(char)
    return ''.join(result)

def convert_html_file(filepath):
    """Konvertuje jedan HTML fajl"""
    print(f"Konvertujem: {filepath}")

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Konvertuj sadržaj
        converted_content = cyrillic_to_latin(content)

        # Sačuvaj nazad
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(converted_content)

        print(f"✓ Uspešno konvertovan: {filepath}")
        return True
    except Exception as e:
        print(f"✗ Greška pri konverziji {filepath}: {e}")
        return False

def main():
    # Direktorijum sa HTML fajlovima
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Lista HTML fajlova za konverziju
    html_files = [
        'index.html',
        'about.html',
        'founder.html',
        'team.html',
        'workshops.html',
        'projects.html',
        'statute.html',
        'contact.html'
    ]

    print("=" * 60)
    print("KONVERZIJA HTML STRANICA: ĆIRILICA → LATINICA")
    print("=" * 60)
    print()

    success_count = 0
    total_count = len(html_files)

    for html_file in html_files:
        filepath = os.path.join(base_dir, html_file)
        if os.path.exists(filepath):
            if convert_html_file(filepath):
                success_count += 1
        else:
            print(f"⚠ Fajl ne postoji: {filepath}")

    print()
    print("=" * 60)
    print(f"KONVERZIJA ZAVRŠENA: {success_count}/{total_count} fajlova")
    print("=" * 60)

if __name__ == "__main__":
    main()
