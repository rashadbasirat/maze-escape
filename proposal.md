# Proposal

## What will (likely) be the title of your project?

Maze Escape

## In just a sentence or two, summarize your project.

A Python desktop game in which the player explores a maze, collects a key, and
unlocks an exit. Random layouts and increasing difficulty will make it replayable.

## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?

Maze Escape will use Python and Tkinter to display a top-down maze and accept arrow
key or WASD movement. Walls will prevent movement, a collectible key will unlock
the exit, and reaching the unlocked exit will show a victory screen. The planned
extensions are three difficulty levels, randomized connected layouts, a timer,
move counter, optional visited-cell trail, pause/resume, temporary hints with a
time penalty, and persistent best unassisted times. The player will run
`python maze_escape.py` or use the included Windows launcher. The game will run
locally without a network connection or additional Python packages.

## If planning to combine 1051's final project with another course's final project, with which other course? And which aspect(s) relate to each course?

Not currently planned. Confirm this statement before submitting.

## If planning to collaborate with 1 or 2 classmates, list their names, email addresses, and assigned TAs.

Not applicable. I am working alone.

## GOOD outcome: what WILL you accomplish no matter what?

A playable maze with keyboard movement, wall collisions, a key, a locked exit,
and a clear win condition. The code will run locally and include instructions.

## BETTER outcome: what do you THINK you can accomplish before the deadline?

Three difficulty levels, random mazes, elapsed time and move tracking,
pause/resume, and best-time records saved to a JSON file.

## BEST outcome: what do you HOPE to accomplish before the deadline?

A polished interface, temporary hints with a time penalty, an optional trail,
automatic pause on focus loss, automated solvability checks, and a clear demo video.

## In a paragraph or more, outline your next steps. What skills or topics require research? Who will do what?

As the sole project member, I am responsible for reviewing the code, testing the
game, refining its features, maintaining the repository, and preparing the
documentation and demonstration. I will review Tkinter Canvas drawing and event
handling, depth-first maze generation, breadth-first path finding, and JSON file
storage. I will test that every difficulty can be completed, the gate cannot be
used before finding the key, paused time is excluded, and hints do not produce a
best-time record. I will then collect feedback, improve unclear controls, update
the README, and record the final 1-3 minute video. The initial version was built
with Codex assistance, which will be disclosed in the documentation.

---
Draft scope for Rashad Basirat to review. The local implementation already exists;
the proposal is not a claim of instructor approval. Not submitted.
