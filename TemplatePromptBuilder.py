class TemplatePromptBuilder:
    """
    Combines variables from multiple PromptVariable nodes
    and applies them to a template string with {placeholders}.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "template": ("STRING", {
                    "multiline": True,
                    "default": "{subject} captured with {camera} during {time}"
                }),
            },
            "optional": {
                "var_1": ("DICT",),
                "var_2": ("DICT",),
                "var_3": ("DICT",),
                "var_4": ("DICT",),
                "var_5": ("DICT",),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "build_prompt"
    CATEGORY = "Kodesign Tools 🔥"

    def build_prompt(self, template, var_1=None, var_2=None, var_3=None, var_4=None, var_5=None):
        merged = {}
        for var in [var_1, var_2, var_3, var_4, var_5]:
            if isinstance(var, dict):
                merged.update(var)

        try:
            result = template.format(**merged)
        except KeyError as e:
            raise ValueError(f"Missing variable in template: {e}")

        return (result,)


# Only register THIS node here
NODE_CLASS_MAPPINGS = {
    "TemplatePromptBuilder": TemplatePromptBuilder
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TemplatePromptBuilder": "Template Prompt Builder"
}
