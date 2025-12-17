<div align="center">

# 🧪 Ren'Py Script Flow Experiment

**Testing variables, conditional logic, and branching flow**

![Ren'Py](https://img.shields.io/badge/Ren'Py-FF7F7F?logo=renpy&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)

*Learning branching mechanics through experimentation*

</div>

---

## 📖 Purpose

This experiment tests:
- Variable declaration and modification
- Conditional logic (`if` statements)
- Menu-based branching
- Label jumping
- Dynamic text interpolation

---

## 📝 Script
```python
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
```

---

## 🎯 What This Tests

### Variables
- ✅ Declaring character definitions (`define`)
- ✅ Setting default variable values (`default`)
- ✅ Modifying variables with Python code (`$ courage += 1`)
- ✅ Displaying variable values in dialogue (`[courage]`)

### Branching
- ✅ Menu creation with multiple choices
- ✅ Label jumping based on user selection
- ✅ Conditional logic affecting dialogue

### Flow Control
- ✅ Scene transitions (`scene bg room`)
- ✅ Fade effects (`with fade`)
- ✅ Label organization
- ✅ Script termination (`return`)

---

## 📚 Key Learnings

**Variable Management:**
- Variables can be modified mid-script using Python syntax
- Variables persist across labels within the same session
- Dynamic text interpolation uses `[variable_name]` syntax

**Branching Logic:**
- Menus create decision points
- `jump` moves execution to different labels
- Conditional statements can alter narrative flow

**Script Structure:**
- Labels organize different story paths
- `return` ends script execution
- Clean label naming improves readability

---

## 🧠 Observations

- Ren'Py seamlessly blends narrative scripting with Python logic
- Variable-based branching enables dynamic storytelling
- Menu systems provide clear player agency
- Script flow is predictable and easy to trace

---

## 👨‍💻 Author

**Sumit**

- GitHub: [@LegendarySumit](https://github.com/LegendarySumit)

---
