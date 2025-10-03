from app import app

def test_hello():
    client = app.test_client()
    resp = client.get("/")
    assert resp.data == b"Hello, DevOps World!"

def test_add():
    client = app.test_client()
    resp = client.get("/add/2/3")
    assert resp.data == b"5"
