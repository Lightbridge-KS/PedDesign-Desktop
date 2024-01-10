import math
from ._child import *
from ._designTemp import design_template


# CT Chest (Old version) TODO Deprecate
def design_chest(age_group, weight_kg):
    assert age_group in [
        "younger_child",
        "older_child",
    ], "Invalid `age_group`, Please choose: 'younger_child' or 'older_child'"

    print("-- Design CT --", "\n")
    print("CT chest, venous only")
    # Weight
    print("Body weight:", weight_kg, "kg")

    # kV
    kV = get_kV(weight_kg)
    print("kV:", kV)
    # mA
    print("mA: auto")
    # Noise
    noise_index = 17 if age_group == "younger_child" else 20
    print("Noise index:", noise_index)
    # Delay
    print("Delay: 45 sec")
    # Contrast
    ml_kg = 1  # Chest
    print_contrast(ml_kg=ml_kg, weight_kg=weight_kg)
    # Rate
    print_rate_ml_sec(
        contrast_ml=get_contrast_ml(ml_kg=ml_kg, weight_kg=weight_kg),
        rate_formula="no_delay",
    )
    print("\n---")


# Whole Abdomen (Old version) TODO Deprecate
def design_whole_abd(age_group, weight_kg, rate_formula="no_delay", delay_sec=None):
    assert age_group in [
        "younger_child",
        "older_child",
    ], "Invalid `age_group`, Please choose: 'younger_child' or 'older_child'"
    assert rate_formula in [
        "no_delay",
        "delay",
    ], "Invalid rate_formula argument. Please choose 'no_delay' or 'delay'."

    print("-- Design CT --", "\n")
    print("CT whole abdomen, venous only")
    # Weight
    print("Body weight:", weight_kg, "kg")

    # kV
    kV = get_kV(weight_kg)
    print("kV:", kV)
    # mA
    print("mA: auto")
    # Noise
    noise_index = 15 if age_group == "younger_child" else 17
    print("Noise index:", noise_index)
    # Delay
    if rate_formula == "no_delay":
        print("Delay: 60 or 65 or 70 sec")
    else:
        print("Delay:", delay_sec)

    # Contrast
    ml_kg = 2  # WA
    print_contrast(ml_kg=ml_kg, weight_kg=weight_kg)
    # Rate
    print_rate_ml_sec(
        contrast_ml=get_contrast_ml(ml_kg=ml_kg, weight_kg=weight_kg),
        rate_formula=rate_formula,
        delay_sec=delay_sec,
    )
    print("\n---")


# Chest + WA


def design_chest_whole_abd(
    age_group, weight_kg, rate_formula="no_delay", delay_sec=None
):
    assert age_group in [
        "younger_child",
        "older_child",
    ], "Invalid `age_group`, Please choose: 'younger_child' or 'older_child'"
    assert rate_formula in [
        "no_delay",
        "delay",
    ], "Invalid rate_formula argument. Please choose 'no_delay' or 'delay'."

    print("-- Design CT --", "\n")
    print("Venous chest + whole abdomen")
    # Weight
    print("Body weight:", weight_kg, "kg")

    # kV
    kV = get_kV(weight_kg)
    print("kV:", kV)
    # mA
    print("mA: auto")
    # Noise
    noise_index = 15 if age_group == "younger_child" else 17
    print("Noise index:", noise_index)
    # Delay
    if rate_formula == "no_delay":
        print("Delay: 60 or 65 or 70 sec")
    else:
        print("Delay:", delay_sec, "sec")

    # Contrast
    ml_kg = 2  # WA
    print_contrast(ml_kg=ml_kg, weight_kg=weight_kg)
    # Rate
    print_rate_ml_sec(
        contrast_ml=get_contrast_ml(ml_kg=ml_kg, weight_kg=weight_kg),
        rate_formula=rate_formula,
        delay_sec=delay_sec,
    )
    print("\n---")


# CTA Liver
def design_cta_liver(age_group, weight_kg):
    assert age_group in [
        "younger_child",
        "older_child",
    ], "Invalid `age_group`, Please choose: 'younger_child' or 'older_child'"

    print("-- Design CT --", "\n")
    print("CTA liver")
    # Weight
    print("Body weight:", weight_kg, "kg")

    # kV
    kV = get_kV(weight_kg)
    print("kV:", kV)
    # mA
    print("mA: auto")
    # Noise
    noise_index = 15 if age_group == "younger_child" else 17
    print("Noise index:", noise_index)
    # Delay
    print("Delay: 20 sec (CTA); 70 sec (Venous)")

    # Contrast
    ml_kg = 2.5  # Liver
    print_contrast(ml_kg=ml_kg, weight_kg=weight_kg)
    ml = get_contrast_ml(ml_kg=ml_kg, weight_kg=weight_kg)

    # Rate
    rate = (ml + 15) / 20
    rate_adj = math.ceil(rate * 10) / 10  # Round up to 1 decimal place
    print(f"Rate: {rate_adj} ml/sec ({ml} + 15) / 20 = {round(rate, 3)}")

    print("\n---")


# For Testing
if __name__ == "__main__":
    # Chest
    design_chest("younger_child", 12)
    design_chest_2(12, is_first_study=True)
    # WA
    design_whole_abd("younger_child", 12)
    design_whole_abd("younger_child", 12, "delay", 70)
    # Chest + WA
    design_chest_whole_abd("younger_child", 12)
    # Liver
    design_cta_liver("younger_child", 20.5)
