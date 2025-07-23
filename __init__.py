from .PromptVariable import NODE_CLASS_MAPPINGS as var_nodes, NODE_DISPLAY_NAME_MAPPINGS as var_display
from .TemplatePromptBuilder import NODE_CLASS_MAPPINGS as builder_nodes, NODE_DISPLAY_NAME_MAPPINGS as builder_display

NODE_CLASS_MAPPINGS = {**var_nodes, **builder_nodes}
NODE_DISPLAY_NAME_MAPPINGS = {**var_display, **builder_display}
