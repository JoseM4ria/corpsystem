from backend.core.models import *


def test_primeiro():
    client = Cliente()
    assert client == Cliente()
