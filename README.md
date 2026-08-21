
# My Game Theory Projects


Implementing algorithms for game-theory situations is fun. This repository will be my collection for them. Humble beginnings!

<hr style="border: none; border-top: 10px double #333; color: #333; overflow: visible; text-align: center; height: 5px;">


## The Minimax Algorithm

This **Minimax** project will apply the *minimax* algorithm along with common optimizations such as *alpha-beta pruning* for some arbitrary *game*. 

A *game* must include a *State* object, a *Branch* function that acts on a state, and an *Evaluation* function to evaluate a state. 

To run the *minimax* algorithm, simply create an *initial state* and *reference the game file*. An example of a proper game file is given in the `games/` folder. Use the `template.py` file to make a game state that is compatible with the minimax class
