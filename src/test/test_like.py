import pytest
from unittest.mock import AsyncMock, MagicMock
from datetime import datetime
#testing for likes
# Mock API client setup
class MockApiClient:
    def __init__(self):
        self.app = MagicMock()
        self.app.bsky = MagicMock()
        self.app.bsky.feed = MagicMock()
        # Set default return value for getActorLikes
        self.app.bsky.feed.getActorLikes = AsyncMock(return_value={'data': {'feed': []}})
        self.app.bsky.graph = MagicMock()
        self.app.bsky.graph.block = MagicMock()
        # Configure create and delete block operations
        self.app.bsky.graph.block.create = AsyncMock(return_value={'uri': 'mock_uri'})
        self.app.bsky.graph.block.delete = AsyncMock()

# Fixture to provide a mock API client
@pytest.fixture
def client():
    return MockApiClient()

# Test: Checks returned posts liked by an actor
@pytest.mark.asyncio
async def test_returns_posts_liked_by_actor(client):
    # Setup expected data
    client.app.bsky.feed.getActorLikes.return_value = {
        'data': {'feed': [{'post': {'author': {'did': 'alice'}}}, {'post': {'author': {'did': 'bob'}}}, {'post': {'author': {'did': 'carol'}}}]}
    }
    bob_likes = await client.app.bsky.feed.getActorLikes({'actor': 'bob'}, {'headers': 'headers_bob'})
    assert len(bob_likes['data']['feed']) == 3

    # Simulating an exception for non-found profile
    client.app.bsky.feed.getActorLikes.side_effect = Exception("Profile not found")
    with pytest.raises(Exception) as excinfo:
        await client.app.bsky.feed.getActorLikes({'actor': 'bob'}, {'headers': 'headers_carol'})
    assert "Profile not found" in str(excinfo.value)

# Test: Validates handling when a viewer has blocked the author of liked posts
@pytest.mark.asyncio
async def test_viewer_has_blocked_author_of_liked_posts(client):
    await client.app.bsky.graph.block.create({'repo': 'bob'}, {'subject': 'alice', 'createdAt': datetime.now().isoformat()}, 'headers_bob')
    client.app.bsky.feed.getActorLikes.return_value = {'data': {'feed': [{'post': {'author': {'did': 'carol'}}}]}}
    feed = await client.app.bsky.feed.getActorLikes({'actor': 'bob'}, {'headers': 'headers_bob'})
    assert all(item['post']['author']['did'] != 'alice' for item in feed['data']['feed'])
    await client.app.bsky.graph.block.delete({'repo': 'bob', 'rkey': 'mock_uri'}, 'headers_bob')

# Test: Ensures correct handling when the author of a liked post has blocked the viewer
@pytest.mark.asyncio
async def test_liked_post_author_has_blocked_viewer(client):
    await client.app.bsky.graph.block.create({'repo': 'alice'}, {'subject': 'bob', 'createdAt': datetime.now().isoformat()}, 'headers_alice')
    client.app.bsky.feed.getActorLikes.return_value = {'data': {'feed': []}}
    feed = await client.app.bsky.feed.getActorLikes({'actor': 'bob'}, {'headers': 'headers_alice'})
    assert all(item['post']['author']['did'] != 'alice' for item in feed['data']['feed'])
    await client.app.bsky.graph.block.delete({'repo': 'alice', 'rkey': 'mock_uri'}, 'headers_alice')
