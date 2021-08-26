import json

def extract_route(req):

    lista1 = req.split(" /")
    lista2 = lista1[1].split(" ")
    return lista2[0]

def read_file(filepath):
    string = str(filepath)
    extensao = string.split(".")
    tipo = extensao[1]
    if tipo == "txt" or tipo == "html" or tipo == "css" or tipo == "js":
        with open(filepath, "rt", encoding="UTF-8") as text:
            lido = text.read()
            return lido
    with open(filepath, "rb") as binary:
        lido = binary.read()
        return lido

def load_data(nomeJson):
    filepath = "data/"+nomeJson
    with open(filepath,"rt", encoding="UTF-8") as text:
        content = text.read()
        contentPython = json.loads(content)
        return contentPython

def load_template(nomeHtml):
    filepath = "templates/"+nomeHtml
    content = read_file(filepath)
    return content

def writeNote(dictionary):
    filepath = "data/note.json"
    with open(filepath, "r", encoding="UTF-8") as note:
        pyhtonNote = json.load(note)
    with open(filepath, "w", encoding="UTF-8") as note:
        pyhtonNote.append(dictionary)