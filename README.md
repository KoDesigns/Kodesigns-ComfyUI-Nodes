
<img width="312" height="65" alt="logo" src="https://github.com/user-attachments/assets/7c06c67d-27b5-453c-9ba4-5dfde04eedae" />
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/KoDesigns/Kodesigns-ComfyUI-Nodes)](https://github.com/KoDesigns/Kodesigns-ComfyUI-Nodes/releases)
[![GitHub stars](https://img.shields.io/github/stars/KoDesigns/Kodesigns-ComfyUI-Nodes)](https://github.com/KoDesigns/Kodesigns-ComfyUI-Nodes/stargazers)
![ComfyUI](https://img.shields.io/badge/ComfyUI-Nodes-blue)
![GitHub last commit](https://img.shields.io/github/last-commit/KoDesigns/Kodesigns-ComfyUI-Nodes)

# Kodesigns-ComfyUI-Nodes

Custom nodes for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) focused on **variable‑driven prompt building**.
These nodes allow you to modularly define variables (e.g., subject, camera, time of day) and reuse them across prompts — making your workflows cleaner and easier to manage.

---

## Features

* **PromptVariable Node**

  * Define a single variable (`name` + `value`)
  * Output as a dictionary for downstream nodes

* **TemplatePromptBuilder Node**

  * Combine multiple variables into one prompt
  * Multiline template support with `{placeholders}`
  * Handles missing variables gracefully

---

## Example Workflow

**Template**

```
Hey {subject}, taken with a {camera}
```

**Variables**

* `subject = dog`
* `camera = Nikon 45D`

**Result**

```
Hey dog, taken with a Nikon 45D
```
<img width="3062" height="1042" alt="image" src="https://github.com/user-attachments/assets/a36d37da-132a-4adc-ae45-9f37f8c3f02c" />

---
## Nesting Variables

You can also nest variables inside of variables as seen in the example under, this way you can have more variables and make a even more dynamic setup. That you can split into different sections.

<img width="3616" height="1586" alt="image" src="https://github.com/user-attachments/assets/d90458bb-d9dc-4c68-93c4-398904e7ab8f" />

For nested workflow example, drag and drop the image under into your ComfyUI.

<img width="2752" height="1536" alt="ComfyUI_00011_" src="https://raw.githubusercontent.com/KoDesigns/Kodesigns-ComfyUI-Nodes/refs/heads/main/example/NestedWorkflowExample.png"/>


---

## Installation

1. Clone this repository into your ComfyUI `custom_nodes` folder:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/KoDesigns/Kodesigns-ComfyUI-Nodes.git
```

2. Restart ComfyUI.
3. New nodes will appear under "**Kodesign Tools 🔥"**.

---

## Usage

1. Add **Prompt Variable** nodes for each piece of data you want to inject.
2. Add a **Template Prompt Builder** node and reference variables with `{name}` in your prompt.
3. Connect variable nodes to builder node (`var_1`, `var_2`, etc.).
4. Send output to your text encoders, preview nodes, or prompt combiners.

---

## License

MIT — free to use and modify.
