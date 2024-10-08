import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
        html_list = re.findall(r'(<.*?>)', html, re.DOTALL)

        for elem in html_list:
            if elem in html:
                html = html.replace(elem, '')

        cleaned_html = re.sub(r'^\s+', '', html, flags=re.MULTILINE)

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(cleaned_html)


delete_html_tags('draft.html')
