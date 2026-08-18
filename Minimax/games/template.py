
# This is a template for a State class
class State:
    def __init__(self):
        self.evaluation = None
        self.branches = []
        self.turn = None

    # ======== REQUIRED METHODS ======== #

    def __repr__(self) -> str:
        # ...
        return f"State()"

    def get_moves(self) -> list[State]:
        # ...
        return self.branches

    def get_evaluation(self) -> float:
        # ...
        return self.evaluation