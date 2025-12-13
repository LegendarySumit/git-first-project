# Basic Game Start Script

```renpy
# This is a basic Ren'Py script to start a visual novel game.

label start:
    scene bg room
    show hero happy

    "This is my first Ren'Py visual novel."

    return
```

## Defining a Character

```
define h = Character("Hero")

Usage:

h "Hello! Welcome to my story."
```
## Common Commands

```
Playing Background Music
play music "audio/theme.mp3"


Stopping music:

stop music
```

## Showing and Hiding Characters

```
show hero happy
hide hero

Scene Change with Transition
scene bg room
with fade
```

## Simple Menu Choice
```
menu:
    "What should I do?"
    "Explore the room":
        jump explore
    "Go outside":
        jump outside

Label Jump
label explore:
    "You decided to explore the room."
    return
```