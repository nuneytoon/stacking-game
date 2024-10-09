# Stacking Game

The objective of this game is to construct stacks as tall as possible without
the stacks falling over. Discs will slowly fall from the top of the screen and
the user must try to catch them while avoiding the "evil" discs. If the stack
collapses or the player catches three "evil" discs, they lose. If the stack
remains in tact, the player manages to avoid catching three "evil" discs, and
they reach the points threshold, they win.

## Set up and dependencies

This game is built in Python v3.12.3 with TKinter for the UI.

### Installation (for development)

1. Install Python from [python.org](https://www.python.org)
2. Verify the correct Python version has been installed by running one of the
   following in your terminal or command prompt:

```bash
python --version
```

or

```bash
python3 --version
```

3. TKinter typically comes preinstalled with Python (particularly on Windows).
   If you are on Unix and do not have it, however, you can simply run the
   following in your terminal to install it:

```bash
pip3 install tk
```
