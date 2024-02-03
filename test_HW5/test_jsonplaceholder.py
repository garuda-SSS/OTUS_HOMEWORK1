import requests
import pytest


@pytest.mark.parametrize('number', [4, 8, 33])
def test_placeholder_with_number(number):
    link = f'https://jsonplaceholder.typicode.com/posts/{number}'
    response = requests.get(link)
    assert response.status_code == 200, 'Данные не получены'
    assert response.json()['id'] == number, 'Неверный id в пакете'


def test_placeholder_all():
    link = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(link)
    assert response.status_code == 200, 'Данные не получены'
    assert len(response.json()) == 100, 'Получены не все пользователи'


@pytest.mark.parametrize('id_value', [1, 55, 25])
def test_placeholder_patch(id_value):
    link = f'https://jsonplaceholder.typicode.com/posts/{id_value}'
    data = {"title": "test"}
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    patch = requests.patch(link, json=data, headers=headers)
    assert patch.status_code == 200, 'Ошибка при редактировании'
    assert patch.json()["title"] == "test", 'Поле не отредактировалось'
    assert patch.json()["id"] == id_value, 'Был отредактирован не тот пользователь'


@pytest.mark.parametrize('data', [{"title": "test1", "body": "test1", "userId": 1},
                                  {"title": "test2", "body": "test2", "userId": 2},
                                  {"title": "test3", "body": "test3", "userId": 3}])
def test_placeholder_put(data):
    link = f'https://jsonplaceholder.typicode.com/posts/1'
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    put = requests.put(link, json=data, headers=headers)
    assert put.status_code == 200, 'Ошибка при редактировании'
    assert put.json()["title"] == data["title"], 'Поле "title" не обновилось'
    assert put.json()["body"] == data["body"], 'Поле "body" не обновилось'
    assert put.json()["userId"] == data["userId"], 'Поле "userId" не обновилось'


def test_placeholder_delete():
    link = 'https://jsonplaceholder.typicode.com/posts/1'
    response = requests.delete(link)
    assert response.status_code == 200, 'Пользователь не удален'