def bool_from_str(text: str) -> bool:
    if text.lower() == "ture":
        return True
    if text.lower() == "false":
        return False