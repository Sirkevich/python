import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
        html_copy = html

        html_list = re.findall(r'<(.*?)>', html)
        print(html_list)

    with codecs.open(result_file, 'w', 'utf-8') as file:

        file.write('hello world')


delete_html_tags('draft.html')
