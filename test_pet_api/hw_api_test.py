import requests
import json
from post_put_objects import post_object
from post_put_objects import put_object

LINK = "https://petstore.swagger.io/v2"

'''
Code explanation and execution instructions are present in readme.txt file.
'''

def get_available_pets():
    '''
    Test purpose: Get "available" pets. Assert expected result
    '''
    response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=available")
    with open("response.json", "w") as json_file:
        json.dump(response.json(), json_file, indent=4, sort_keys=True)

    assert response.status_code == 200, "Get available pets not working properly"

def get_response_status_code(id):
    link = LINK + "/pet/{0}".format(post_object["id"])
    get_response = requests.get(link)
    return get_response.status_code

def post_new_available_pet():
    '''
    Test purpose: Post a new available pet to the store. Assert new pet added.
    '''
    post_response = requests.post(LINK + "/pet", json = post_object)
    print(post_response.text)
    postObjRevised = json.dumps(post_object)
    postObjRevised = postObjRevised.replace(" ", "")
    print(postObjRevised)

    assert post_response.text == postObjRevised, "First check of Post failed"
    assert get_response_status_code(post_object["id"]) == 200, "Second check of Post failed"

def update_pet_sold():
    '''
    Test purpose: Update this pet status to "sold". Assert status updated.
    '''
    put_response = requests.put(LINK + "/pet", json = put_object)
    print(put_response.text)
    putObjRevised = json.dumps(put_object)
    putObjRevised = putObjRevised.replace(" ", "")
    print(putObjRevised)

    assert put_response.text == putObjRevised, "First check of Put failed"
    assert get_response_status_code(put_object["id"]) == 200, "Second check of Put failed"

def delete_pet(id):
    '''
    Test purpose: Deletes pet. Assert deletion.
    '''
    link = LINK + "/pet/{0}".format(id)
    del_response = requests.delete(link)
    assert del_response.status_code == 200, "Pet was not removed"


menu = {}
menu['1'] = "Check available pets. (GET)"
menu['2'] = "Add new available pet. (POST)"
menu['3'] = "Change availability to sold. (PUT)"
menu['4'] = "Delete pet by ID. (DELETE)"
menu['5'] = "Exit"
print(menu)

while True:
    selection = input("Executed: ")
    if selection =='1':
        print(menu['1'])
        get_available_pets()
        print("Available pets could be found in response.json file")
    elif selection == '2':
        print(menu['2'])
        post_new_available_pet()
        print("Successful")
    elif selection == '3':
        print(menu['3'])
        update_pet_sold()
        print("Successul")
    elif selection == '4':
        print(menu['4'])
        id = input("Pet ID to be deleted: ")
        delete_pet(id)
        print("Successful")
    elif selection == '5':
        break
    else:
        print("Unknown Option Selected!")