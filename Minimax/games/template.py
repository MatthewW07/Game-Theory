
# This is a template for a State class
class State:
    def __init__(self):
        self.evaluation = None
        self.branches = None
        self.turn = None

    # ======== REQUIRED METHODS ======== #

    def __repr__(self) -> str:
        # ...
        return f"State()"

    def get_moves(self) -> list[State]:
        if self.branches is None:
            self.branches = []
        # ...
        return self.branches

    def get_evaluation(self) -> float:
        if self.evaluation is None:
            self.evaluation = 0.0
        # ...
        return self.evaluation