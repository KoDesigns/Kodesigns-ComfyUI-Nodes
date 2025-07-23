class PromptVariable:
    """
    Defines a single variable: name + value
    Output: dict {name: value}
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "var_name": ("STRING", {"multiline": False, "default": "subject"}),
                "var_value": ("STRING", {"multiline": True, "default": "dog"})
            }
        }

    RETURN_TYPES = ("DICT",)
    FUNCTION = "output_var"
    CATEGORY = "Kodesign Tools 🔥"

    def output_var(self, var_name, var_value):
        return ({var_name: var_value},)


NODE_CLASS_MAPPINGS = {
    "PromptVariable": PromptVariable
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptVariable": "PromptVariable"
}
