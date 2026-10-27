"""Maze generation and game rules, independent of the graphical interface."""

from collections import deque
import random


class Maze:
    def __init__(self, width=21, height=15, seed=None):
        if width < 7 or height < 7 or width % 2 == 0 or height % 2 == 0:
            raise ValueError("Maze dimensions must be odd and at least 7.")
        self.width, self.height = width, height
        self.start = (1, 1)
        self.floor = {self.start}
        rng = random.Random(seed)
        stack = [self.start]
        # Depth-first search carves passages through a grid of solid walls.
        while stack:
            x, y = stack[-1]
            options = [(x + dx, y + dy) for dx, dy in
                       ((2, 0), (-2, 0), (0, 2), (0, -2))
                       if 0 < x + dx < width - 1 and 0 < y + dy < height - 1
                       and (x + dx, y + dy) not in self.floor]
            if options:
                nx, ny = rng.choice(options)
                self.floor.update({((x + nx) // 2, (y + ny) // 2), (nx, ny)})
                stack.append((nx, ny))
            else:
                stack.pop()
        distances = self.distances(self.start)
        self.exit = max(distances, key=distances.get)
        # Put the key far from the entrance while keeping it separate from the exit.
        candidates = [p for p in self.floor if p not in (self.start, self.exit)]
        exit_distances = self.distances(self.exit)
        self.key = max(candidates, key=lambda p: distances[p] + exit_distances[p])

    def neighbors(self, position):
        x, y = position
        return [(x + dx, y + dy) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))
                if (x + dx, y + dy) in self.floor]

    def distances(self, start):
        result = {start: 0}
        queue = deque([start])
        while queue:
            position = queue.popleft()
            for neighbor in self.neighbors(position):
                if neighbor not in result:
                    result[neighbor] = result[position] + 1
                    queue.append(neighbor)
        return result

    def path(self, start, goal):
        parents = {start: None}
        queue = deque([start])
        while queue:
            position = queue.popleft()
            if position == goal:
                route = []
                while position is not None:
                    route.append(position)
                    position = parents[position]
                return route[::-1]
            for neighbor in self.neighbors(position):
                if neighbor not in parents:
                    parents[neighbor] = position
                    queue.append(neighbor)
        return []


class Game:
    def __init__(self, level=1, seed=None):
        if level not in (1, 2, 3):
            raise ValueError('Choose level 1, 2, or 3.')
        self.level = level
        self.maze = Maze(17 + 4 * (level - 1), 13 + 2 * (level - 1), seed)
        self.position = self.maze.start
        self.has_key = False
        self.won = False
        self.moves = 0
        self.visited = {self.position}

    def move(self, dx, dy):
        """Return 'wall', 'locked', 'key', 'win', or 'move'."""
        if self.won or (dx, dy) not in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            return 'wall'
        target = self.position[0] + dx, self.position[1] + dy
        if target not in self.maze.floor:
            return 'wall'
        if target == self.maze.exit and not self.has_key:
            return 'locked'
        self.position = target
        self.moves += 1
        self.visited.add(target)
        if target == self.maze.key and not self.has_key:
            self.has_key = True
            return 'key'
        if target == self.maze.exit:
            self.won = True
            return 'win'
        return 'move'
