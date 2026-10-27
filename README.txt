MAZE ESCAPE
===========
A local desktop game written in Python and Tkinter. No extra packages or network
connection are needed. Requires Python 3.10+ with Tkinter (normally included in
the official Windows Python installation).

PLAY
Double-click "Play Maze Escape.bat" on Windows, or run:
    python maze_escape.py

Find the gold diamond key, then reach the mint-colored exit gate.
Use the arrow keys or WASD to move one tile at a time.
N: generate a new maze. P / Escape: pause or resume.
H: briefly reveal the next few steps, with a 10-second time penalty.
Enter after winning: next level, or another maze after level 3.
Choose any of three levels from the dropdown. Show trail toggles visited tiles.
The clock starts on your first successful move. Switching away pauses the game.
Only runs completed without hints qualify for a personal best. Best times are
per difficulty (random layouts vary, so they are not identical speedrun courses).
Records are saved at %LOCALAPPDATA%\MazeEscape\best_times.json on Windows.

PROJECT FILES
maze_logic.py: random depth-first maze generation, breadth-first path finding,
              and rules for movement, collecting the key, and unlocking the exit.
maze_escape.py: Tkinter interface, rendering, keyboard input, timing, pause,
               hints, and JSON personal-best storage.
test_maze.py: automated checks for connectivity, solvability, walls, and gates.
Run checks with: python -m unittest -v

HOW THE MAZE WORKS
1. Start with walls. Treat odd-numbered grid locations as possible rooms.
2. Randomly choose an unvisited neighboring room two tiles away.
3. Open that room and the wall between it and the current room.
4. Backtrack when there are no unvisited neighbors left.
5. Choose a distant exit and a reachable key. Every generated floor tile is
   connected, and the exit is an endpoint, so the key remains reachable while
   the exit is locked.
6. The game checks each requested move before changing the player's position.

PRESENTING THIS AS COURSEWORK
This version was generated with AI assistance in this chat. Review and understand
the implementation, customize it, and check your course's assistance policy before
using it for assessed work. No Canvas submission has been made.
GitHub repository: https://github.com/rashadbasirat/maze-escape
Your course still requires its preproposal, proposal, progress report, README,
GitHub repository, and 1-3 minute demonstration video. This document is a run guide,
not a claim that those deliverables or a final course submission are finished.

SUGGESTED PERSONAL EXTENSIONS
Add your own artwork or theme; introduce a limited vision mode; add coins;
design fixed challenge mazes; or add sound with an optional audio package.
