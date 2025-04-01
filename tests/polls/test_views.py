from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_index_view(client):
    url = reverse("index")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_results_view(client):
    url = reverse("results", kwargs={"question_id": 1})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_detail_view(client):
    url = reverse("detail", kwargs={"question_id": 1})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_vote_view(client):
    url = reverse("vote", kwargs={"question_id": 1})
    response = client.get(url)
    assert response.status_code == 200
