
# action-rpg-pygame

This is a skunkworks style sandbox repo to prove out some action RPG type gameplay ideas.

It uses [Python 3](https://www.python.org/) and [PyGame](https://www.pygame.org/news) for things like graphics, sound, and input. It borrows a few implementation ideas from [planarity-py](https://github.com/parappayo/planarity-py).

Genre-wise this project is inspired by [The Legend of Zelda](https://en.wikipedia.org/wiki/The_Legend_of_Zelda_(video_game)), [Diablo II](https://en.wikipedia.org/wiki/Diablo_II), [Secret of Mana](https://en.wikipedia.org/wiki/Secret_of_Mana), and [Vampire Survivors](https://en.wikipedia.org/wiki/Vampire_Survivors). Ideally this repo will provide a toolset for building games like these.

## Setup

[pipenv](https://pipenv.pypa.io/en/latest/) is recommended for creating a [Python virtual environment](https://docs.python.org/3/tutorial/venv.html) to manage dependency packages.

To launch the game,

* `pipenv run main.py`

## Project Structure

* `main.py` is the entry point with the main game loop
* `game/` is a package containing game-specific "engine" code
  * stuff like "draw player" and "get input events" goes here
  * depends on PyGame and sim
* `sim/` is a package containing abstract game world code
  * stuff like "update enemy positions" and "check attack collisions" goes here
  * should only depend on standard Python libs

 This project loosely attempts to follow the [PEP8 style conventions](https://peps.python.org/pep-0008/). To check for styling errors run `pep8 .`

## Goals

Accomplished so far,

* simple game loop

Yet to be accomplished,

* sprite rendering
* texture atlas support, maybe support for [TexturePacker](https://www.codeandweb.com/texturepacker)
* tile-based background layer
* integration with [Tiled](https://www.mapeditor.org/)
* two player same-screen gameplay
* simple enemy spawners
* radial hit detection logic
* procedural level generation
* a few character classes
* simple equipment system
* persist game state to file
* UI front-end flow (menu screen, load game)

## References

* [Beyond PCC: Using Sprite Sheets in Pygame](https://ehmatthes.github.io/pcc_2e/beyond_pcc/pygame_sprite_sheets/)
