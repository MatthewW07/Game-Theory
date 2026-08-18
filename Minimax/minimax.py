
from pprint import pprint
import math

"""
Here's what the State class looks like:
class State:
    def __init__(self, num=0):
        self.evaluation
        self.branches

    def branches(self) -> list[State]:
        ...
        return self.branches

    def evaluation(self) -> float:
        ...
        return self.evaluation
"""

class Minimax:
    def __init__(self, initial_state: State, is_max: bool=True, depth: int=10):
        self.tree = initial_state
        self.is_max = is_max
        self.depth = depth


    def __repr__(self):
        return (
            f"Minimax(is_max={self.is_max}, depth={self.depth})"
            f"{self.print_tree()}"
        )


    # The main minimax function
    def minimax(self):

        # ======== BRUTE FORCE IMPLEMENTATION ======== #

        # Create the state tree
    
        # self.create_tree()
        def brute_dfs(node: State, is_max: bool, depth: int) -> float:
            if depth == 0:
                return node.get_evaluation()

            # Maximizer
            if is_max:
                options = [brute_dfs(branch, 0, depth-1) for branch in node.branches]
                return max(options) if options else node.get_evaluation()

            # Minimizer
            else:
                options = [brute_dfs(branch, 1, depth-1) for branch in node.branches]
                return min(options) if options else node.get_evaluation()

            

        # ======== ALPHA-BETA IMPLEMENTATION ======== #

        def alpha_beta(node: State, is_max: bool, depth: int, alpha=-math.inf, beta=math.inf) -> float:
            if depth == 0 or not node.branches:
                return node.get_evaluation()

            # Maximizer
            if is_max:
                max_eval = -math.inf
                for move in node.branches:
                    max_eval = max(max_eval, alpha_beta(move, False, depth-1, alpha, beta))
                    alpha = max(alpha, max_eval)
                    if alpha >= beta:
                        break
                node.evaluation = max_eval
                return max_eval

            # Minimizer
            else:
                min_eval = math.inf
                for move in node.branches:
                    min_eval = min(min_eval, alpha_beta(move, True, depth-1, alpha, beta))
                    beta = min(beta, min_eval)
                    if alpha >= beta:
                        break
                node.evaluation = min_eval
                return min_eval


        return alpha_beta(self.tree, self.is_max, self.depth)
    

    # Utility function to recursively create the entire state tree
    def create_tree(self) -> None:

        def dfs(node: State, depth: int):
            if depth == 0:
                return node

            plain_moves = node.get_moves() 
            full_branches = []
            for branch in plain_moves:
                branch = dfs(branch, depth - 1) 
                full_branches.append(branch)

            node.branches = full_branches

            return node

        self.tree = dfs(self.tree, self.depth)


    # Utility function to recursively print the state tree
    def print_tree(self, node: State=None, prefix="", is_last=True) -> None:
        if node is None:
            node = self.tree

        connector = "└── " if is_last else "├── "

        print(
            f"{prefix}{connector}"
            f"{node}"
        )

        children = node.branches
        if not children:
            return
        for i, child in enumerate(children):
            is_last_child = i == len(children) - 1

            if is_last:
                child_prefix = prefix + "    "
            else:
                child_prefix = prefix + "│   "

            self.print_tree(child, child_prefix, is_last_child)



if __name__ == "__main__":

    # ======== TESTING ======== #

    # Should result in a Tie (3.0)
    from games.tic_tac_toe import State
    initial_state = State()
    minimax = Minimax(initial_state, depth=10)
    res = minimax.minimax()
    print(res)

