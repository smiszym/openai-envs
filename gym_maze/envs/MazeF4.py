from gym_maze.envs import AbstractMaze

import numpy as np


class MazeF4(AbstractMaze):
    def __init__(self):
        super().__init__(np.matrix([
            [1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 9, 1],
            [1, 0, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 1, 1],
            [1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
        ]))
        self.solution = np.matrix([
            [9, 9, 9, 9, 9, 9, 9],
            [9, 2, 2, 2, 2, 9, 9],
            [9, 1, 9, 9, 9, 9, 9],
            [9, 0, 7, 6, 6, 9, 9],
            [9, 0, 9, 9, 9, 9, 9],
            [9, 9, 9, 9, 9, 9, 9],
        ])

    def rate_action(self, action):
        return 1.0 if action == self.solution[self.pos_y, self.pos_x] else 0.0
