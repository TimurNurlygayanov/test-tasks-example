import requests


def test_get_key():
    result = requests.get('https://petfriends1.herokuapp.com/api/key',
                          headers={'email': 'api@mail.ru', 'password': 'test'})

    assert result.status_code == 200
    assert 'key' in result.json()


def test_get_all_pets():
    result = requests.get('https://petfriends1.herokuapp.com/api/key',
                          headers={'email': 'api@mail.ru', 'password': 'test'})
    api_key = result.json()['key']

    res = requests.get('https://petfriends1.herokuapp.com/api/pets',
                       headers={'auth_key': api_key})

    data = res.json()
    all_pets = data['pets']

    assert len(all_pets) == 100


def test_create_pet():
    # Get key
    result = requests.get('https://petfriends1.herokuapp.com/api/key',
                          headers={'email': 'api@mail.ru', 'password': 'test'})
    api_key = result.json()['key']

    # Create new pet
    res = requests.post('https://petfriends1.herokuapp.com/api/create_pet_simple',
                        headers={'auth_key': api_key},
                        json={'name': 'Барсик', 'age': 1, 'animal_type': 'Cat'})
    new_pet_id = res.json()['id']

    assert res.status_code == 200

    # Get all my pets
    res_all_pets = requests.get('https://petfriends1.herokuapp.com/api/pets?filter=my_pets',
                                headers={'auth_key': api_key})
    my_pets = res_all_pets.json()['pets']

    pets_ids = []
    for pet in my_pets:
        pets_ids.append(pet['id'])

    assert new_pet_id in pets_ids
