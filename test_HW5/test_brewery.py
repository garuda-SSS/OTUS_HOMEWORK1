import requests
import pytest


def test_brewery_random():
    link = 'https://api.openbrewerydb.org/v1/breweries/random'
    response = requests.get(link)
    assert response.status_code == 200, 'Случайная пивоварня не получена'


@pytest.mark.parametrize('ids', ['701239cb-5319-4d2e-92c1-129ab0b3b440,06e9fffb-e820-45c9-b107-b52b51013e8f',
                                 'b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0,06e9fffb-e820-45c9-b107-b52b51013e8f'])
def test_brewery_by_ids(ids):
    link = f'https://api.openbrewerydb.org/v1/breweries?by_ids={ids}'
    response = requests.get(link)
    assert len(response.json()) == 2, 'Неверное число пивоварен'
    assert response.status_code == 200, 'Ошибка при получении нескольких пивоварен'


@pytest.mark.parametrize('number_page', [1, 2, 7, 11])
def test_brewery_all_list(number_page):
    link = f'https://api.openbrewerydb.org/v1/breweries?per_page={number_page}'
    response = requests.get(link)
    assert response.status_code == 200, 'Ошибка при получении списка пивоварен'
    assert len(response.json()) == number_page, 'Неверное число пивоварен на странице'


@pytest.mark.parametrize('name', ['Gates', 'Fermen', 'Co'])
def test_brewery_by_name(name):
    link = f'https://api.openbrewerydb.org/v1/breweries?by_name={name}&per_page=1'
    response = requests.get(link)
    assert response.status_code == 200, 'Ошибка при использовании фильтра по названиям'
    assert name in response.json()[0]['name'], f'Некорректная выдача при использовании фильтра по названиям c {name}'


@pytest.mark.parametrize('brewery_type', ['bar', 'contract', 'closed'])
def test_brewery_by_type(brewery_type):
    link = f'https://api.openbrewerydb.org/v1/breweries?by_type={brewery_type}&per_page=1'
    response = requests.get(link)
    assert response.status_code == 200, 'Ошибка при использовании фильтра по типам'
    assert brewery_type == response.json()[0]['brewery_type'], \
        f'Некорректная выдача при использовании фильтра по типам с {brewery_type}'
