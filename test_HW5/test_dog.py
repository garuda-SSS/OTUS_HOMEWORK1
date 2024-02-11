import requests
import pytest


@pytest.mark.parametrize('breed', ["affenpinscher", "cattledog", "tervuren", "hound"])
def test_dog_all_images(breed):
    link = f'https://dog.ceo/api/breed/{breed}/images'
    response = requests.get(link)
    assert response.status_code == 200, 'Изображения не получены'


@pytest.mark.parametrize('breed', ["mastiff", "vizsla", "pointer", "hound"])
def test_dog_sub_breed(breed):
    link = f'https://dog.ceo/api/breed/{breed}/list'
    response = requests.get(link)
    assert response.status_code == 200, 'Подпороды не получены'


@pytest.mark.parametrize('breed', ["regerg", "g34t34", "re34", "345534"])
def test_dog_sub_breed_error(breed):
    link = f'https://dog.ceo/api/breed/{breed}/list'
    response = requests.get(link)
    assert response.status_code == 404, 'Почему то вы не получили ошибку'


def test_dog_random_images():
    link = 'https://dog.ceo/api/breeds/image/random'
    response = requests.get(link)
    print(response.text)
    assert response.status_code == 200, 'Случайное фото не получено'


def test_dog_all_breeds():
    link = 'https://dog.ceo/api/breeds/list/all'
    response = requests.get(link)
    assert response.status_code == 200, 'Список пород не получен'
    