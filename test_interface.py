"""Tkinter integration checks; use a temporary record file, never personal scores."""

import json
from pathlib import Path
import tempfile
import tkinter as tk
import unittest
from unittest.mock import patch

import maze_escape
from maze_logic import Game


class InterfaceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.record_path = Path(self.temp.name) / 'scores.json'
        self.root = tk.Tk()
        self.root.withdraw()
        self.app = maze_escape.MazeEscape(self.root)
        self.app.records = {}

    def tearDown(self):
        # Cancel scheduled callbacks before destroying the test-only window.
        for callback in self.root.tk.splitlist(self.root.tk.call('after', 'info')):
            self.root.after_cancel(callback)
        self.root.destroy()
        self.temp.cleanup()

    def follow(self, goal):
        for target in self.app.game.maze.path(self.app.game.position, goal)[1:]:
            x, y = self.app.game.position
            self.app.move(target[0] - x, target[1] - y)

    def test_pause_excludes_time_and_blocks_movement(self):
        app = self.app
        with patch('maze_escape.time.monotonic', return_value=100):
            app.started = 90
            app.toggle_pause()
        old = app.game.position
        app.move(1, 0)
        self.assertEqual(app.game.position, old)
        self.assertEqual(app.current_time(), 10)
        with patch('maze_escape.time.monotonic', return_value=120):
            app.toggle_pause()
            self.assertEqual(app.current_time(), 10)
        with patch('maze_escape.time.monotonic', return_value=125):
            self.assertEqual(app.current_time(), 15)

    def test_hint_penalty_and_new_game_reset(self):
        app = self.app
        with patch('maze_escape.time.monotonic', return_value=50):
            app.show_hint()
            self.assertEqual(app.current_time(), 10)
        self.assertEqual(app.hints, 1)
        self.assertTrue(app.hint_route)
        generation = app.hint_generation
        app.new_game()
        self.assertEqual(app.current_time(), 0)
        self.assertEqual(app.hints, 0)
        app.clear_hint(generation)  # An old callback cannot affect a later game.
        self.assertFalse(app.hint_route)

    def test_all_levels_can_win_and_save(self):
        app = self.app
        for level in (1, 2, 3):
            app.level.set(f'{level} test')
            app.new_game()
            app.game = Game(level, seed=15)
            with patch('maze_escape.SCORE_FILE', self.record_path):
                self.follow(app.game.maze.key)
                self.follow(app.game.maze.exit)
            self.assertTrue(app.game.won)
            self.assertIn(str(level), json.loads(self.record_path.read_text()))
            app.draw()

    def test_assisted_run_does_not_save_best(self):
        app = self.app
        app.show_hint()
        with patch('maze_escape.SCORE_FILE', self.record_path):
            self.follow(app.game.maze.key)
            self.follow(app.game.maze.exit)
        self.assertTrue(app.game.won)
        self.assertFalse(self.record_path.exists())

    def test_record_loader_handles_bad_data(self):
        for content in ('not json', '[]', 'null'):
            self.record_path.write_text(content)
            self.assertEqual(maze_escape.load_records(self.record_path), {})
        self.record_path.write_text('{"1": 12, "2": -1, "3": Infinity}')
        self.assertEqual(maze_escape.load_records(self.record_path), {'1': 12})


if __name__ == '__main__':
    unittest.main()
