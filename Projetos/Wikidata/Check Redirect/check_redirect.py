# -*- coding: utf-8 -*-

"""
Checks if a QID has redirection
50 out of 50 check
"""

import json
import time
import requests


def api_request(lst):
    """
    :param lst: list with QIDs
    :return: insert QIDs in output.txt
    """
    global i
    global len_items
    base_url = "https://www.wikidata.org/w/api.php"
    params = {
        "action": "wbgetentities",
        "ids": "|".join(lst),
        "format": "json",
        "redirects": "yes"
    }

    error = True
    while error:
        try:
            response = requests.get(base_url, params=params)
            if response.status_code == 200:
                data = json.loads(response.text)
                for entity_id, entity_data in data["entities"].items():
                    if "redirects" in entity_data:
                        new_id = entity_data['redirects']['to']
                        print(f"{i} of {len_items}: {entity_id} --> {new_id}")
                        # save
                        with open("output.txt", "a") as out:
                            out.write(f'{new_id}\n')
                    else:
                        print(f"{i} of {len_items}")
                        # save
                        with open("output.txt", "a") as out:
                            out.write(f'{entity_id}\n')
                    i += 1
                error = False
            else:
                print(f"response status {response.status_code}")
                time.sleep(5)
        except requests.exceptions.HTTPError as errh:
            print(f"Error HTTP: {errh}")
            time.sleep(5)
        except requests.exceptions.ConnectionError as errc:
            print(f"Error connection: {errc}")
            time.sleep(5)
        except requests.exceptions.Timeout as errt:
            print(f"Error timeout: {errt}")
            time.sleep(5)
        except requests.exceptions.RequestException as err:
            print(f"Error request: {err}")
            time.sleep(5)


with open("input.txt") as items:
    items = items.readlines()

# get infos
len_items = len(items)
total = len_items // 50
rest = len_items % 50

i = 1
first = 0
last = 50

for n in range(total):
    qids = items[first:last]
    qids = [qid.replace("\n", "") for qid in qids]
    api_request(qids)
    first += 50
    last += 50

last += rest
qids = items[first:last]
qids = [qid.replace("\n", "") for qid in qids]
api_request(qids)
