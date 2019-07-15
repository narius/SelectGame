import pytest
from api import app as a

# Creates a fixture whose name is "app"
# and returns our flask server instance
@pytest.fixture
def app():
    return a
