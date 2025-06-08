import requests

URL = "http://127.0.0.1:8000/graphql"


def test_query_hello():
    query = """
    query {
      hello
    }
    """
    response = requests.post(URL, json={"query": query})
    assert response.status_code == 200
    assert response.json()["data"]["hello"] == "Hello from GraphQL!"


def test_login_valid():
    mutation = """
    mutation {
      login(email: "test@example.com", password: "1234")
    }
    """
    response = requests.post(URL, json={"query": mutation})
    assert response.status_code == 200
    assert response.json()["data"]["login"] == "Login successful!"


def test_login_invalid():
    mutation = """
    mutation {
      login(email: "wrong@example.com", password: "wrong_pass")
    }
    """
    response = requests.post(URL, json={"query": mutation})
    assert response.status_code == 200
    assert response.json()["data"]["login"] == "Invalid credentials."
