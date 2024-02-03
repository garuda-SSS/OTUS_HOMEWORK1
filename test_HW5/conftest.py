import pytest


def pytest_addoption(parser):
    parser.addoption(
        '--url', default='https://ya.ru', type=str
    )
    parser.addoption(
        '--status_code', default=200, type=int
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")