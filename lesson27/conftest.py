import pytest
from lesson27.infrastructure import ParserClass


@pytest.fixture
def parser():
    return ParserClass()
