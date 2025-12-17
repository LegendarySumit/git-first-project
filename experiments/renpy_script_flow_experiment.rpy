# Ren'Py Script Flow Experiment
# Purpose: Testing variables, conditional logic, and branching flow
define p = Character("Player")
define n = Character(None)
default courage = 0
label start:
    scene bg room
    with fade
    n "This is an experiment to test Ren'Py script flow."
    p "I want to see how choices affect the story."
    menu:
        "What do you want to do?"
        "Stay calm":
            $ courage += 1
            jump calm_path
        "Panic":
            jump panic_path
label calm_path:
    p "I stayed calm."
    if courage > 0:
        n "Your calmness gives you confidence."
    jump end_experiment
label panic_path:
    p "I panicked and froze."
    n "Fear takes over your thoughts."
    jump end_experiment
label end_experiment:
    n "This concludes the script flow experiment."
    n "Variable value: [courage]"
    return
