import json

with open('C:\\Users\\mnknt\\OneDrive\\Documents\\Python for data engineering\\session-2\\python scripts\\example.json','r') as js_file:
    json_file = json.load(js_file)

print(json_file['glossary']['GlossDiv']['title'])