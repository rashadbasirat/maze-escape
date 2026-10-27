# Maze Escape

A Python desktop puzzle game by **Rashad Basirat** for CIS 1051.
Solo project. Developed with AI coding assistance; see [Acknowledgments](#acknowledgments).

Collect the golden key, find the exit, and escape a new maze every time you play.

## Run the game

Requires **Python 3.10 or newer with Tkinter**. No pip packages are required.
Tkinter is included with the normal Windows Python installer. On other systems,
install your operating system's Tkinter package if `import tkinter` fails.

On Windows, double-click **Play Maze Escape.bat**. Alternatively, open a terminal
in this folder and run:

```sh
python maze_escape.py
```

If your system calls Python `python3`, use that command instead.

## How to play

1. Choose one of three levels: The Courtyard, The Catacombs, or The Labyrinth.
2. Move the mint-colored player with the arrow keys or WASD.
3. Collect the gold diamond key. The exit stays locked until the key is collected.
4. Reach the mint-colored exit gate to win.
5. Press Enter on the victory screen for the next level or a fresh final-level maze.

| Control | Action |
| --- | --- |
| Arrow keys / WASD | Move one tile |
| H / Hint button | Show up to six upcoming steps for three seconds; add 10 seconds |
| P / Escape | Pause or resume |
| N / New maze button | Start a new randomly generated maze |
| Show trail | Toggle dots marking visited cells |
| Enter / Space after winning | Continue |

The clock starts on the first successful move, or when requesting a hint.
Switching to another app pauses an active run. A run with hints cannot set a
personal best. Best times are stored separately for each difficulty at
`%LOCALAPPDATA%\MazeEscape\best_times.json` on Windows. When `LOCALAPPDATA`
is unavailable, the program uses a `MazeEscape` folder in your home directory.
Different random layouts have different solution lengths, so these records
are casual personal bests, not times on an identical competitive course.

## Features

- Randomly generated, connected mazes at three sizes.
- Key collection and a locked exit.
- Elapsed time, move count, optional trail, and temporary hints.
- Pause/resume, including automatic pause when the application loses focus.
- A victory screen and level progression.
- Local JSON storage for the best unassisted time in each level.
- No internet connection, game assets, or third-party packages needed to play.

## How the code works

`maze_logic.py` contains the rules without any graphical code. `Maze` uses
randomized depth-first search with a stack to carve paths through a wall grid.
Breadth-first search finds distances and routes. The exit is a far-away endpoint;
the key is placed on a reachable floor tile distinct from the entrance and exit.
`Game.move()` checks walls, the locked gate, key collection, and the win condition.

`maze_escape.py` builds the Tkinter window. It uses a Canvas to draw the grid and
player. Keyboard events call the game rules, `after()` updates the clock without
blocking input, and JSON stores records. Timing uses a monotonic clock so normal
system-clock adjustments do not change a run's duration.

## Tests

Run from this directory:

```sh
python -m unittest -v
```

The checks cover 300 seeded mazes across all three difficulties, connectivity,
reachable keys and exits, wall collisions, locked gates, completed-game behavior,
timing, hints, pause/resume, and record-file handling. Tkinter interface tests
require a graphical desktop environment.

## Development challenges and solutions

- **Solvable random mazes:** generating walls arbitrarily can trap the player.
  Carving a connected maze with a backtracking algorithm avoids disconnected areas.
- **Finding useful key and exit positions:** breadth-first distances let the game
  select distant locations instead of placing both next to the entrance.
- **Keeping the UI responsive:** timer updates use Tkinter's scheduled callbacks
  instead of a blocking game loop.
- **Fairer timing:** paused time is excluded, hints receive a visible penalty, and
  assisted runs do not update best-time records.
- **Reliable rendering:** the grid scales to its available canvas area, and the
  readonly level selector explicitly maps its colors for the selected Tk theme.
- **Robust saved data:** malformed, negative, or non-finite record values are ignored;
  write failures leave the game playable and display a message.

These notes describe the implementation work in this version. Rashad should add
his own reflections on what he learned, enjoyed, and changed after reviewing and
playing the game; no personal experiences have been invented here.

## Demo video

**Pending: record the required 1-3 minute video later.** Include the project title,
Rashad's name and year, and a short demonstration of the final game. Replace this
paragraph with the accessible video URL. If using YouTube, use Public or Unlisted.
Put the same URL in the Canvas final submission.

## Acknowledgments

This initial implementation, tests, and document drafts were generated with
OpenAI Codex assistance in this chat. There is no copied Pong/Mario starter code
or third-party artwork. Rashad should understand and review the code, make his
own revisions, and follow the course's assistance and attribution requirements.

## Project paperwork

- `preposal.md`: idea and collaboration details.
- `proposal.md`: planned scope, outcomes, and next steps.
- `status.md`: dated progress-report draft; update before its deadline.
- `ASSIGNMENT_CHECKLIST.md`: readiness, deadlines, and remaining actions.

Repository: https://github.com/rashadbasirat/maze-escape

No work has been submitted to Canvas by this workflow. The project documents are
drafts for Rashad to review before submitting their links.
