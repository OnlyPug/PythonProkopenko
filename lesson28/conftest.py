import pytest
from lesson28.infrastructure.adaptor import ApiAdaptor
from lesson28.model.lesson28_adapter_users import NewSQLBase


@pytest.fixture
def adapter():
    return ApiAdaptor()


@pytest.fixture
def new_db():
    return NewSQLBase()
