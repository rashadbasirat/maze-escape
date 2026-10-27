"""Check solvability, collisions, and the key/exit rules without opening a window."""
import unittest
from maze_logic import Game, Maze


class MazeTests(unittest.TestCase):
    def walk(self, game, goal):
        result = None
        for target in game.maze.path(game.position, goal)[1:]:
            x, y = game.position
            result = game.move(target[0] - x, target[1] - y)
        return result

    def test_all_generated_levels_are_connected(self):
        for level in (1, 2, 3):
            for seed in range(100):
                game = Game(level, seed)
                maze = game.maze
                self.assertEqual(set(maze.distances(maze.start)), maze.floor)
                self.assertEqual(len({maze.start, maze.key, maze.exit}), 3)
                self.assertEqual(self.walk(game, maze.key), 'key')
                self.assertEqual(self.walk(game, maze.exit), 'win')
                self.assertTrue(game.won)

    def test_wall_does_not_count_as_move(self):
        game = Game(seed=4)
        self.assertEqual(game.move(-1, 0), 'wall')
        self.assertEqual(game.moves, 0)
        self.assertEqual(game.position, (1, 1))

    def test_gate_requires_key(self):
        game = Game(seed=4)
        game.position = game.maze.neighbors(game.maze.exit)[0]
        x, y = game.position
        self.assertEqual(game.move(game.maze.exit[0]-x, game.maze.exit[1]-y), 'locked')
        self.assertFalse(game.won)
        self.assertEqual(game.moves, 0)

    def test_completed_game_is_frozen(self):
        game = Game(seed=8)
        self.walk(game, game.maze.key)
        self.walk(game, game.maze.exit)
        moves = game.moves
        game.move(1, 0)
        self.assertEqual(game.moves, moves)

    def test_seed_reproduces_layout(self):
        self.assertEqual(Maze(seed=42).floor, Maze(seed=42).floor)


if __name__ == '__main__':
    unittest.main()
