""" Run in the command line to strip ruby text from an Aozora format html file. 
    Assumming the encoding is shift_jisx0213, saves html file to shift_jisx0213 in file
    original_file_name_stripped.html

    example ruby text:
        <ruby><rb>宿無</rb><rp>（</rp><rt>やどなし</rt><rp>）</rp></ruby>

    
"""

import re, os

FURIGANA_HTML = r'<ruby><rb>(?P<base>.*?)</rb><rp>（</rp><rt>(?P<ruby>.*?)</rt><rp>）</rp></ruby>'

def strip_ruby(expr: str) -> str:
    """
    Remove ruby html.
    """
    def replace(match):
        base = match.group('base')
        return f'{base}'

    # run replace() on all matches
    return re.sub(FURIGANA_HTML, replace, expr).strip() # trim leading, trailing whitespace too

def read_html_file(file_name):
    try:
        with open(file_name, 'r', encoding='shift_jisx0213') as file:
            html_content = file.read()
            # print(html_content)
            return html_content
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return None


def save_html_file(file_name, stripped_html):
    try:
        file_name_base = os.path.splitext(file_name)[0]
        new_file_name = file_name_base + '_stripped.html'
        with open(new_file_name, 'w', encoding='shift_jisx0213') as file:
            file.write(stripped_html)
            print(f"Stripped HTML content saved to '{file_name}_stripped.html'.")
    except Exception as e:
        print(f"Error occurred while saving stripped HTML content: {e}")


file_name = input("Enter the HTML file name: ")
read_html_file(file_name)
             
# encodings = ['shift-jis', 'shift_jisx0213', 'utf-8']  # Add more encodings if needed
html_content = read_html_file(file_name)

# print(html_content)

# Strip Ruby HTML
stripped_html = strip_ruby(html_content)

# print(stripped_html)

if stripped_html:
    save_html_file(file_name, stripped_html)
"""
    try:
        # Convert HTML content from Shift JIS to UTF-8
        html_content_utf8 = stripped_html.encode('shift_jisx0213').decode('utf-8')
        # Process the HTML content (e.g., strip Ruby annotations)
        save_html_file(file_name, html_content_utf8)
    except Exception as e:
        print(f"Error occurred while processing HTML content: {e}")
"""