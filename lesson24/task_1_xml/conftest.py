import pytest

from lesson24.task_1_xml.base_page import XMLwork


@pytest.fixture
def xmlfile():
    yield XMLwork('example.xml')
