from typing import Optional, Dict

def compare(original_text: str, modified_text: str, template_text: Optional[str] = None) -> Dict:
    deviations = {}

    original_lines = original_text.splitlines()
    modified_lines = modified_text.splitlines()
    template_lines = template_text.splitlines() if template_text else None

    max_lines = max(len(original_lines), len(modified_lines), len(template_lines) if template_lines else 0)

    for i in range(max_lines):
        orig_line = original_lines[i] if i < len(original_lines) else ""
        mod_line = modified_lines[i] if i < len(modified_lines) else ""
        temp_line = template_lines[i] if template_lines and i < len(template_lines) else None

        if orig_line != mod_line:
            deviation = {
                "original": orig_line,
                "modified": mod_line,
            }
            if temp_line is not None:
                deviation["template"] = temp_line

            deviations[i] = deviation

    return deviations