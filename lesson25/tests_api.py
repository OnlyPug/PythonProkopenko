# Test GET
import pytest


def test_get_list_off_object(phone):
    response = phone.get_list_of_objects()
    assert response.status_code == 200


def test_get_all_off_object(phone):
    response = phone.get_list_of_objects()
    assert response.status_code == 200


def test_get_save_json_for_list_off_object(phone):
    response = phone.save_list_of_objects()
    assert response.status_code == 200


def test_get_save_json_for_single_phone(phone):
    response = phone.save_single_phone(4)
    assert response.status_code == 200


def test_get_id_list(phone):
    response = phone.get_list_of_device_ids(list_number=(2, 8, 5))
    assert response.status_code == 200


def test_get_id_list_and_save(phone):
    response = phone.save_list_of_device_ids()
    assert response.status_code == 200


# Test POST

def test_create_new_phone(phone):
    response = phone.create_new_object()
    assert response.status_code == 200
    assert response.json()["createdAt"]
    assert response.json()["name"] == 'Maga-ultra-pro G350'


@pytest.mark.negative
def test_create_new_phone_negative(phone):
    response = phone.create_new_object_negative()
    assert response.status_code == 400
    assert response.json()["error"]


# Test Put
def test_update_object(phone):
    response = phone.update_single_default_object()
    assert response.json()["updatedAt"]


# Test PATH

def test_path_of_object(phone):
    response = phone.path_single_default_object()
    assert response.status_code == 200
    assert response.json()['name'] == 'New name'
    assert response.json()['updatedAt']


# Test DELETE
def test_delete_object(phone):
    deleted_object, deleted_object_id = phone.delete_single_default_object()
    assert deleted_object.json()['message'] == f"Object with id = {deleted_object_id} has been deleted."
