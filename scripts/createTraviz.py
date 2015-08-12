import json
import os
import cgi

def unicodeToHTMLEntities(text):
    """Converts unicode to HTML entities.  For example '&' becomes '&amp;'."""
    text = cgi.escape(text).encode('ascii', 'xmlcharrefreplace')
    return text

def make_json_table():
    years, texts = zip(*[(text, open('../data/' + text).read().split('\n\n')) for text in os.listdir('../data') if text.endswith('.txt')])
    tables = {}
    for paragraph in range(1, len(texts[0])):
        table = []
        for i, text in enumerate(texts):
            table.append({"edition": "Edition of " + years[i].replace(".txt", ""), "text": text[paragraph]})
        tables[paragraph] = table
    return tables

with open("../static/js/grimms.json", "w") as out:
    json.dump(make_json_table(), out, indent=2)
