

class State:
    def __init__(self, evaluation=None, branches=None):
        self.evaluation = evaluation
        self.branches = branches
        self.turn = None

    def __repr__(self):
        return f"{self.evaluation}"

    def get_moves(self):
        return self.branches

    def get_evaluation(self):
        return self.evaluation if self.evaluation is not None else 0



if __name__ == "__main__":

    test = State(
        branches=[
            State(branches=[
                State(branches=[
                    State(branches=[
                        State(evaluation=8),
                        State(evaluation=7)
                    ]),
                    State(branches=[
                        State(evaluation=3),
                        State(evaluation=9)
                    ])
                ]),
                State(branches=[
                    State(branches=[
                        State(evaluation=9),
                        State(evaluation=8)
                    ]),
                    State(branches=[
                        State(evaluation=2),
                        State(evaluation=4)
                    ])
                ])
            ]),
            State(branches=[
                State(branches=[
                    State(branches=[
                        State(evaluation=1),
                        State(evaluation=8)
                    ]),
                    State(branches=[
                        State(evaluation=8),
                        State(evaluation=9)
                    ])
                ]),
                State(branches=[
                    State(branches=[
                        State(evaluation=9),
                        State(evaluation=9)
                    ]),
                    State(branches=[
                        State(evaluation=3),
                        State(evaluation=4)
                    ])
                ])
            ])
        ]
    )
