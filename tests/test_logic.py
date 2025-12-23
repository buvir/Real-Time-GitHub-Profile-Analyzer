import pytest
from app import fetch_github_data
import asyncio

@pytest.mark.asyncio
async def test_api_fetch_invalid_user():
    # Test how our app handles a fake user
    data = await fetch_github_data("this_user_does_not_exist_12345")
    assert data is None

@pytest.mark.asyncio
async def test_api_fetch_valid_user():
    # Test a known user (like 'octocat')
    data = await fetch_github_data("octocat")
    assert data is not None
    assert "profile" in data
    assert data["profile"]["login"] == "octocat"
