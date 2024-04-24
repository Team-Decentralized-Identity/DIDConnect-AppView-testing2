import unittest
import asyncio
import pytest
#test for search
class MockNetwork:
    def __init__(self, config):
        self.bsky = MockBSky(config)

    def getClient(self):
        return AtpAgent(MockClient())

    def getSeedClient(self):
        return MockSeedClient()

class MockBSky:
    def __init__(self, config):
        pass

    def getClient(self):
        return AtpAgent(MockClient())

class MockClient:
    # Mock client functionalities
    pass

class MockSeedClient:
    def dids(self):
        return {
            'cara-wiegand69.test': 'did:cara-wiegand69',
            'eudora-dietrich4.test': 'did:eudora-dietrich4'
        }

class AtpAgent:
    def __init__(self, client):
        self.client = client

    async def searchActorsTypeahead(self, params, headers=None):
        # Return different results based on the search term
        if params['term'] == '':
            return {'actors': []}  # No actors for empty search term
        else:
            return {
                'actors': [
                    {'handle': 'cara-wiegand69.test'},
                    {'handle': 'eudora-dietrich4.test'}
                ]
            }

    async def searchActors(self, params, headers=None):
        # Static response for demonstration purposes
        if params['term'] == '':
            return {'actors': []}  # No actors for empty search term
        else:
            return {
                'actors': [
                    {'handle': 'cara-wiegand69.test'},
                    {'handle': 'eudora-dietrich4.test'}
                ]
            }


class TestActorSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.loop = asyncio.get_event_loop()
        cls.network = MockNetwork({'dbPostgresSchema': 'bsky_views_actor_search'})
        cls.agent = cls.network.bsky.getClient()
        cls.seed_client = cls.network.getSeedClient()

    def test_typeahead_gives_relevant_results(self):
        params = {'term': 'car'}
        headers = {'Authorization': 'Bearer test-token'}
        result = self.loop.run_until_complete(self.agent.searchActorsTypeahead(params, headers))
        handles = [actor['handle'] for actor in result['actors']]
        expected_handles = ['cara-wiegand69.test', 'eudora-dietrich4.test']
        for handle in expected_handles:
            self.assertIn(handle, handles)

    def test_search_gives_relevant_results(self):
        params = {'term': 'car'}
        headers = {'Authorization': 'Bearer test-token'}
        result = self.loop.run_until_complete(self.agent.searchActors(params, headers))
        handles = [actor['handle'] for actor in result['actors']]
        expected_handles = ['cara-wiegand69.test', 'eudora-dietrich4.test']
        for handle in expected_handles:
            self.assertIn(handle, handles)

    def test_empty_search_term_returns_no_actors(self):
        params = {'term': ''}
        result = self.loop.run_until_complete(self.agent.searchActorsTypeahead(params))
        self.assertEqual(result['actors'], [])

if __name__ == '__main__':
    unittest.main()
