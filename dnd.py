import requests
import json

url = "https://www.dnd5eapi.co"

## List items
def list_endpoints():
    endpointUrl = url + "/api"
    response = requests.get(endpointUrl)
    obj = json.loads(response.text)
    options = ", ".join(list(obj.keys()))
    return options

def list_spells():
    spellsUrl = url + "/api/spells"
    return list_json(requests.get(spellsUrl))

def list_monsters():
    monstersUrl = url + "/api/monsters"
    return list_json(requests.get(monstersUrl))

### Get index of an item
def get_endpoints(endpoints):
    endpointsUrl = url + "/api/{}".format(endpoints)
    return list_json(requests.get(endpointsUrl))

def get_spells(spell):
    spellUrl = url + "/api/spells/{}".format(spell)
    return handle_json(requests.get(spellUrl))

def get_monsters(monsters):
    monstersUrl = url + "/api/monsters/{}".format(monsters)
    return handle_json(requests.get(monstersUrl))

def get_feature(feature):
    featureUrl = url + "/api/features/{}".format(feature)
    return handle_json(requests.get(featureUrl))

def get_details(resource: str, option: str):
    details = url + "/api/{}/{}".format(resource, option)
    return handle_this(requests.get(details))

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
    return ', '.join(names)

def handle_this(jsonText):
    obj = json.loads(jsonText.text)
    for key in obj.keys():
        print(key, obj[key])
        if isinstance(obj[key], list) == True:
            for item in obj[key]:
                if 'name' in item:
                    print(key, item['name'])

print(get_details("races", "dwarf"))