<div align="center">

# 🧪 Ren'Py Experiments

**Small experiments and tests while learning Ren'Py**

![Ren'Py](https://img.shields.io/badge/Ren'Py-FF7F7F?logo=renpy&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Learning](https://img.shields.io/badge/Type-Experiments-orange)

*Isolated mechanics, not full story scripts*

</div>

---

## 📖 About

This document contains **small experiments and tests** done while learning Ren'Py. These are isolated mechanics to understand engine behavior, not complete story scripts.

---

## 🧪 Experiment 1 — Indentation Sensitivity Test

### Goal
Understand how Ren'Py reacts to incorrect indentation.

### Observation
- Ren'Py is **strictly indentation-based** (Python-style)
- Even a **single misplaced space** can cause script errors
- The engine will not execute scripts with inconsistent indentation

### Example

**❌ Incorrect:**
```python
label start:
scene bg room
    "This will break"
```

**✅ Correct:**
```python
label start:
    scene bg room
    "This works correctly"
```

### Takeaway
**Indentation discipline is mandatory.**

---

## 👨‍💻 Author

**Sumit**

- GitHub: [@LegendarySumit](https://github.com/LegendarySumit)

---

<div align="center">

**🧪 Learning through experimentation**

*Breaking things to understand them*

</div>
