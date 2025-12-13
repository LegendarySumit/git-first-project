# Ren’Py Experiments

This document contains small experiments and tests done while learning Ren’Py.
These are isolated mechanics, not full story scripts.

## Experiment 1 — Indentation Sensitivity Test

Goal
-

Understand how Ren’Py reacts to incorrect indentation.

Observation
-

Ren’Py is strictly indentation-based (Python-style).
Even a single misplaced space can cause script errors.

Example

❌ Incorrect:

label start:
scene bg room
    "This will break"


✅ Correct:

label start:
    scene bg room
    "This works correctly"

## Takeaway

Indentation discipline is mandatory.