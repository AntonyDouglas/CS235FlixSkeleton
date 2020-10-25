class Actor:
    def __init__(self, actor: str):
        self.colleagues = []
        if actor == "" or type(actor) is not str:
            self.__actor = None
        else:
            self.__actor = actor.strip()

    def actor(self) -> str:
        return self.__actor

    def __repr__(self):
        return f"<Actor {self.__actor}>"

    def __eq__(self, other):
        return self.__actor == other.__actor

    def __lt__(self, other):
        if self.__actor is not None and other.__actor is not None:
            return self.__actor < other.__actor
        else:
            return False

    def __hash__(self):
        return hash(self.__actor)

    def add_actor_colleague(self, other):
        if other.__actor not in self.colleagues:
            self.colleagues.append(other.__actor)

    def check_if_this_actor_worked_with(self, other):
        if other.__actor in self.colleagues:
            return True
        else:
            return False