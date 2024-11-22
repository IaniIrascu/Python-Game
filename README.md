# Pokemon Game with PyGame

## Description

A Pokémon-inspired game built with PyGame, featuring tile-based maps across diverse environments. It includes interactive characters with collision detection, seamless scene transitions, and a user-friendly main menu. The project offers rich graphics, animations, and sound effects, providing an immersive and dynamic gaming experience.

## Main Features

-   **Tile-based Mapping**
    -   Uses TMX files for creating and managing game maps.
    -   Supports multiple environments like plant, arena, house, and water.

-   **Game Entities and Characters**
    -   Defines characters with properties such as direction, graphic, and radius.
    -   Implements collision detection and interaction zones.

-   **Main Menu Interface**
    -   Features a  `MainMenu`  class for navigating game options.
    -   Includes buttons for settings and other functionalities.

-   **Scene Transitions**
    -   Manages transitions between different game areas seamlessly.
    -   Handles loading and unloading of map data.

-   **Collision Detection**
    -   Defines collision zones within TMX files to manage interactions.
    -   Ensures characters interact correctly with the environment.

-   **Graphics and Animations**
    -   Incorporates various graphics for characters and environments.
    -   Manages animations and visual effects for a dynamic experience.

-   **Sound Effects**
    -   Integrates sound assets for enhanced gameplay experience.


## Virtual Environment Setup

1. `pip install virtualenv`

2. `python3 -m venv virtual-environment-name` (you should name it env / venv)

3. source `virtual-environment-name/bin/activate` (in wsl)

	3.  `virtual-environment-name/Scripts/Activate.ps1` (in Powershell)

4. `pip install -r requirements.txt`

### If you install a new package, `pip freeze -> requirements.txt`

  

## Docs

1. [PyGame Docs](https://www.pygame.org/docs/#tutorials)

## Git Best Practices

1. Always `git pull` and `pip install -r requirements.txt` before working on something new.
1. Work on a separate branch.
2. Make a PR that closes and issue and request a review.