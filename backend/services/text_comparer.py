def compare(original: dict, modified: dict, template: dict = None) -> dict:
    deviations = {}
    for key, value in original.items():
        modified_value = modified.get(key)
        template_value = template.get(key) if template else None
        if modified_value != value:
            deviations[key] = {
                "original": value,
                "modified": modified_value,
                "template": template_value,
            }
    return deviations
