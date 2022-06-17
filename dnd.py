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
    jsonText = requests.get(details)
    obj = json.loads(jsonText.text)
    return json_extract(obj)

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

def json_extract(obj):
    
    testArr = []
    keys = ['index', 'url']
    def testRun(obj, testArr):
        if isinstance(obj, dict):
            for i in obj.items():
                if isinstance(i[1], (dict, list)):
                    if isinstance(i[1],  list):
                        testArr.append(i[0] + ' ----------')
                    testRun(i[1], testArr)
                else:
                    if i[0] not in keys:
                        testArr.append('{}: {}'.format(i[0], i[1]))
        elif isinstance(obj, list):
            for item in obj:
                testRun(item, testArr)
        return testArr

    testVal = testRun(obj, testArr)
    return testVal

print(get_details("races", "dwarf"))