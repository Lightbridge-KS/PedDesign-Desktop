from . import ct
from . import ct_old


def design_ct(
    study_type: str,
    weight_kg: float,
    is_first_study: bool = False,
    rate_formula: str = "no_delay",
    delay_sec: float = None,
) -> None:
    string = design_ct_str(
        study_type=study_type,
        weight_kg=weight_kg,
        is_first_study=is_first_study,
        rate_formula=rate_formula,
        delay_sec=delay_sec,
    )
    print(string)


def design_ct_str(
    study_type: str,
    weight_kg: float,
    is_first_study: bool = False,
    rate_formula: str = "no_delay",
    delay_sec: float = None,
) -> None:
    assert isinstance(is_first_study, bool), "`is_first_study` must be True of False"
    assert rate_formula in [
        "no_delay",
        "delay",
    ], "Invalid rate_formula argument. Please choose 'no_delay' or 'delay'."
    
    match study_type:
        case "chest":
            design = ct.DesignCTchest(weight_kg=weight_kg, is_first_study=is_first_study)
        case "whole_abd":
            design = ct.DesignCTwholeAbd(
                weight_kg=weight_kg,
                is_first_study=is_first_study,
                rate_formula=rate_formula,
                delay_sec=delay_sec
                )
        case "chest_whole_abd":
            design = ct.DesignCTchestWholeAbd(
                weight_kg=weight_kg,
                is_first_study=is_first_study,
                rate_formula=rate_formula,
                delay_sec=delay_sec
                )
        case "cta_liver":
            design = ct.DesignCTAliver(weight_kg=weight_kg, is_first_study=is_first_study)
        case "hrct":
            design = ct.DesignHRCTchest(weight_kg=weight_kg, is_first_study=is_first_study)
        case _:
            raise "Invalid study_type argument, Please choose: 'chest', 'whole_abd', 'chest_whole_abd', 'cta_liver', or 'hrct'"

    return design.str_design


def design_ct_old(
    study_type, age_group, weight_kg, rate_formula="no_delay", delay_sec=None
):
    assert (
        study_type in ["chest", "whole_abd", "chest_whole_abd", "cta_liver"]
    ), "Invalid study_type argument, Please choose: 'chest', 'whole_abd', 'chest_whole_abd', 'cta_liver'"
    assert age_group in [
        "younger_child",
        "older_child",
    ], "Invalid `age_group`, Please choose: 'younger_child' or 'older_child'"
    assert rate_formula in [
        "no_delay",
        "delay",
    ], "Invalid rate_formula argument. Please choose 'no_delay' or 'delay'."

    # CT Chest
    if study_type == "chest":
        ct_old.design_chest(age_group=age_group, weight_kg=weight_kg)

    # CT Whole Abdomen
    if study_type == "whole_abd":
        ct_old.design_whole_abd(
            age_group=age_group,
            weight_kg=weight_kg,
            rate_formula=rate_formula,
            delay_sec=delay_sec,
        )

    # CT Chest + WA
    if study_type == "chest_whole_abd":
        ct_old.design_chest_whole_abd(
            age_group=age_group,
            weight_kg=weight_kg,
            rate_formula=rate_formula,
            delay_sec=delay_sec,
        )

    # CTA Liver
    if study_type == "cta_liver":
        ct_old.design_cta_liver(age_group=age_group, weight_kg=weight_kg)


# For Testing
if __name__ == "__main__":
    design_ct("chest", 10)
