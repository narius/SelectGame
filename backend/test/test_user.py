#from api.login import LoginWebAPI
#def test_empty_db():
#    assert True


def test_get(client):
    response = client.get("/api/login")
    assert True
