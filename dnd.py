import requests
import json

url = "https://www.dnd5eapi.co"

### Get Spells or List them
def get_spells(spell):
    spellUrl = url + "/api/spells/{}".format(spell)
    response = requests.get(spellUrl)
    return handle_json(response)

def list_spells():
    spellsUrl = url + "/api/spells"
    response = requests.get(spellsUrl)
    return list_json(response)

### Get Monsters or List them
def get_monsters(monsters):
    monstersUrl = url + "/api/monsters/{}".format(monsters)
    response = requests.get(monstersUrl)
    return handle_json(response)

def list_monsters():
    monstersUrl = url + "/api/monsters"
    response = requests.get(monstersUrl)
    return list_json(response)

### JSON Formating
def handle_json(jsonText):
    obj = json.loads(jsonText.text)
    json_formatted_str = json.dumps(obj, indent=1)
    return json_formatted_str

def list_json(jsonText):
    obj = json.loads(jsonText.text)
    names = []
    for spellName in obj['results']:
        if 'name' in spellName:
            names.append(spellName['name'])
    return names

print(get_monsters("aboleth"))