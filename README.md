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
