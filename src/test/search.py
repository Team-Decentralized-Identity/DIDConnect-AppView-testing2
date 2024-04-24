# actor_search_service.py
class ActorSearchService:
    def __init__(self):
        self.actors = [
            {'handle': 'cara-wiegand69.test', 'name': 'Cara Wiegand'},
            {'handle': 'eudora-dietrich4.test', 'name': 'Eudora Dietrich'},
            {'handle': 'shane-torphy52.test', 'name': 'Shane Torphy'},
            {'handle': 'aliya-hodkiewicz.test', 'name': 'Aliya Hodkiewicz'},
            {'handle': 'carlos6.test', 'name': 'Carlos'},
            {'handle': 'carolina-mcderm77.test', 'name': 'Carolina McDermott'}
        ]

    async def search_actors_typeahead(self, term):
        if term == '':
            return []
        return [actor for actor in self.actors if term.lower() in actor['handle'].lower()]
