

def attempt_float(x: str):
    try:
        return float(x)
    except ValueError:
        if x == "":
            return None
        else:
            raise ValueError(f"x = `{x}` must be a number")