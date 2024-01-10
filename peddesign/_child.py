import math

# kV


def get_kV(weight_kg: float) -> str:
    """Get kV according to weight in kg

    Args:
        weight_kg (float): patient's weight in kg

    Returns:
        str: string of weight
    """

    assert isinstance(weight_kg, (int, float)) and weight_kg > 0

    if weight_kg < 20:
        kV = "80"
    elif weight_kg == 20:
        kV = "80 or 100"
    elif weight_kg < 45:
        kV = "100"
    elif weight_kg == 45:
        kV = "100 or 120"
    elif weight_kg <= 60:
        kV = "120"
    else:
        # weight_kg ≥ 60
        kV = "120 ?"

    return kV


# Contrast (ml)


def get_contrast_ml(ml_kg: float, weight_kg: float) -> float:
    """Get contrast volume in ml from ml/kg and weight (kg)

    Args:
        ml_kg (float): Contrast ml/kg
        weight_kg (float): Patient's weight (kg)

    Returns:
        float: ml of contrast
    """
    assert isinstance(weight_kg, (int, float)) and weight_kg > 0

    ml = ml_kg * weight_kg

    # Maximum contrast = 80 ml
    return round(ml, 1) if ml < 80 else 80


def print_contrast(ml_kg: float, weight_kg: float) -> None:
    """Print contrast calculation to STD out

    Args:
        ml_kg (float): Contrast ml/kg
        weight_kg (float): Patient's weight (kg)
    """
    ml = ml_kg * weight_kg
    if ml >= 80:
        ml_adj_txt = "80 ml [maximum]"
    else:
        ml_adj_txt = f"{round(ml, 1)} ml"

    print(f"Contrast: {ml_adj_txt} ({ml_kg} ml/kg * {weight_kg} kg = {ml}) ")


def get_contrast_str(ml_kg: float, weight_kg: float) -> str:
    """Get contrast calculation as string

    Args:
        ml_kg (float): Contrast ml/kg
        weight_kg (float): Patient's weight (kg)
    """
    ml = ml_kg * weight_kg
    if ml >= 80:
        ml_adj_txt = "80 ml [maximum]"
    else:
        ml_adj_txt = f"{round(ml, 1)} ml"

    contrast_calc = f"{ml_adj_txt} ({ml_kg} ml/kg * {weight_kg} kg = {ml})"
    return contrast_calc


# Rate (ml/sec)

# TODO: Deprecate this
# def print_rate_ml_sec(contrast_ml, rate_formula="no_delay", delay_sec=None):
#     rate_formula = rate_formula.lower()
#     assert isinstance(contrast_ml, (int, float)) and contrast_ml > 0

#     if rate_formula == "no_delay":
#         rate = (contrast_ml + 15) / 45
#         rate_adj = math.ceil(rate * 10) / 10  # Round up to 1 decimal place

#         show_calc = f"({contrast_ml} + 15) / 45 = {round(rate, 3)}"

#     elif rate_formula == "delay":
#         assert isinstance(delay_sec, (int, float))

#         rate = (contrast_ml + 15) / (delay_sec - 15)
#         rate_adj = math.ceil(rate * 10) / 10  # Round up to 1 decimal place

#         show_calc = f"({contrast_ml} + 15) / ({delay_sec} - 15) = {round(rate, 3)}"

#     else:
#         raise ValueError(
#             "Invalid rate_formula value. Please choose 'no_delay' or 'delay'.")

#     print(f"Rate: {rate_adj} ml/sec {show_calc}")
