import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 15


@pytest.mark.smoke
@pytest.mark.api
def test_get_all_posts():
    r = requests.get(f"{BASE_URL}/posts", timeout=TIMEOUT)
    assert r.status_code == 200
    assert len(r.json()) == 100


@pytest.mark.smoke
@pytest.mark.api
def test_get_single_post_schema():
    r = requests.get(f"{BASE_URL}/posts/1", timeout=TIMEOUT)
    body = r.json()
    assert r.status_code == 200
    assert set(body.keys()) == {"userId", "id", "title", "body"}
    assert body["id"] == 1
    assert "application/json" in r.headers["Content-Type"]


@pytest.mark.regression
@pytest.mark.api
def test_get_posts_filtered_by_user():
    r = requests.get(f"{BASE_URL}/posts", params={"userId": 1}, timeout=TIMEOUT)
    assert r.status_code == 200
    assert all(post["userId"] == 1 for post in r.json())


@pytest.mark.regression
@pytest.mark.api
def test_create_post():
    payload = {"title": "QA practice", "body": "testing POST", "userId": 1}
    r = requests.post(f"{BASE_URL}/posts", json=payload, timeout=TIMEOUT)
    assert r.status_code == 201
    body = r.json()
    assert body["title"] == payload["title"]
    assert "id" in body


@pytest.mark.regression
@pytest.mark.api
def test_update_post():
    payload = {"id": 1, "title": "updated", "body": "updated body", "userId": 1}
    r = requests.put(f"{BASE_URL}/posts/1", json=payload, timeout=TIMEOUT)
    assert r.status_code == 200
    assert r.json()["title"] == "updated"


@pytest.mark.regression
@pytest.mark.api
def test_delete_post():
    r = requests.delete(f"{BASE_URL}/posts/1", timeout=TIMEOUT)
    assert r.status_code == 200


@pytest.mark.regression
@pytest.mark.api
def test_get_non_existing_post_returns_404():
    r = requests.get(f"{BASE_URL}/posts/99999", timeout=TIMEOUT)
    assert r.status_code == 404
