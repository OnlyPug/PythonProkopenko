import pytest

from lesson25.infrastructure import Phone


@pytest.fixture
def phone():
    return Phone()
