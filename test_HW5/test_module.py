import requests


def test_link(url, status_code):
    response = requests.get('https://ya.ru')
    assert response.status_code == 200, 'Неверный статус код'

