# Ren’Py — Basic Act Structure
---
```
label act_one:
    scene bg forest
    with fade

    "The world felt quiet."

    jump act_two


label act_two:
    scene bg clearing
    with dissolve

    "That silence was hiding something."
    return
```

## Ren’Py — Character & Narrator Usage

```
define j = Character("Jessy")
define jo = Character("Joshua")
define narrator = Character(None)

j "Welcome to this place."
jo "No one here is truly free."
narrator "The air felt heavy with regret."
```

## JavaScript — Event Listener (Basic)

```
document.getElementById("btn").addEventListener("click", () => {
  console.log("Button clicked");
});
```
### JavaScript — Simple Counter
```
JavaScript — Counter Logic
let count = 0;

incrementBtn.addEventListener("click", () => {
  count++;
  display.textContent = count;
});
```
### JavaScript — Dark/Light Mode Toggle
```
toggleBtn.addEventListener("click", () => {
  document.body.classList.toggle("dark");
});
```