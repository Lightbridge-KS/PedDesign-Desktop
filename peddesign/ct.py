import math
from ._child import *
from ._designTemp import design_template

# Design CT Chest


class DesignCTchest:
    """Design CT Chest class
    """

    def __init__(self, weight_kg: float, is_first_study: bool = False) -> None:
        """Design a chest CT Protocol

        Args:
            weight_kg (float): Weight in kg
            is_first_study (bool, optional): `True` if this is the first study. Defaults to False.
        """
        # kV
        kV = get_kV(weight_kg)
        # Noise
        noise_index = 17 if is_first_study else 20
        # Contrast
        ml_kg = 1  # Chest
        contrast_calc = get_contrast_str(ml_kg=ml_kg, weight_kg=weight_kg)
        # Rate
        contrast_ml = get_contrast_ml(ml_kg, weight_kg)
        rate = (contrast_ml + 15) / (45 - 15)
        rate_adj = math.ceil(rate * 10) / 10  # Round up to 1 decimal place
        # Calc at the end
        show_calc = f"({contrast_ml} + 15) / 30 = {round(rate, 3)}"
        # Substitute Fmt String
        self.str_design = design_template["chest"].format(weight_kg=weight_kg,
                                                          kV=kV,
                                                          noise_index=noise_index,
                                                          contrast_calc=contrast_calc,
                                                          rate_adj=rate_adj,
                                                          show_calc=show_calc)

    def __str__(self):
        return self.str_design

    def __repr__(self) -> str:
        return self.str_design

# Design CT Whole Abd


class DesignCTwholeAbd:
    """Design CT whole abdomen class
    """
    def __init__(self, weight_kg: float, is_first_study: bool = False, rate_formula="no_delay", delay_sec=None) -> None:
        """Design a CT of the Whole Abdomen Protocol

        Args:
            weight_kg (float): Weight in kg
            is_first_study (bool, optional): `True` if this is the first study.. Defaults to False.
            rate_formula (str, optional): "delay" or "no_delay": choose "delay" if you want to provide a delay time (as `delay_sec`). Defaults to "no_delay".
            delay_sec (_type_, optional): If `rate_formula` = "delay", input the delay time.
        """
        # kV
        kV = get_kV(weight_kg)
        # Noise
        noise_index = 15 if is_first_study else 17
        # Delay
        if rate_formula == "no_delay":
            delay_sec_calc = "60 or 65 or 70 sec"
        else:
            delay_sec_calc = f"{delay_sec} sec"
        # Contrast
        ml_kg = 2  # WA
        contrast_calc = get_contrast_str(ml_kg=ml_kg, weight_kg=weight_kg)
        # Rate
        contrast_ml = get_contrast_ml(ml_kg=ml_kg, weight_kg=weight_kg)
        # No delay
        if rate_formula == "no_delay":
            rate = (contrast_ml + 15) / 45
            rate_adj = math.ceil(rate * 10) / 10  # Round up to 1 decimal place
            show_calc = f"({contrast_ml} + 15) / 45 = {round(rate, 3)}"
        # Delay
        else:
            assert isinstance(delay_sec, (int, float)
                              ), "`delay_sec` must be a number"
            rate = (contrast_ml + 15) / (delay_sec - 20)
            rate_adj = math.ceil(rate * 10) / 10  # Round up to 1 decimal place
            show_calc = f"({contrast_ml} + 15) / ({delay_sec} - 20) = {round(rate, 3)}"


        # Substitute Fmt String
        self.str_design = design_template["whole_abd"].format(weight_kg=weight_kg,
                                                              kV=kV,
                                                              noise_index=noise_index,
                                                              delay_sec_calc=delay_sec_calc,
                                                              contrast_calc=contrast_calc,
                                                              rate_adj=rate_adj,
                                                              show_calc=show_calc)

    def __str__(self):
        return self.str_design

    def __repr__(self) -> str:
        return self.str_design

# CT Chest + WA


class DesignCTchestWholeAbd:
    """Design CT chest and whole abdomen class
    """
    def __init__(self, weight_kg: float, is_first_study: bool = False, rate_formula="no_delay", delay_sec=None) -> None:
        """Design a CT of the Chest and Whole Abdomen Protocol

        Args:
            weight_kg (float): Weight in kg
            is_first_study (bool, optional): `True` if this is the first study. Defaults to False.
            rate_formula (str, optional): "delay" or "no_delay": choose "delay" if you want to provide a delay time (as `delay_sec`). Defaults to "no_delay".
            delay_sec (_type_, optional): If `rate_formula` = "delay", input the delay time.
        """
        # kV
        kV = get_kV(weight_kg)
        # Noise
        noise_index = 15 if is_first_study else 17
        # Delay
        if rate_formula == "no_delay":
            delay_sec_calc = "60 or 65 or 70 sec"
        else:
            delay_sec_calc = f"{delay_sec} sec"
        # Contrast
        ml_kg = 2  # WA
        contrast_calc = get_contrast_str(ml_kg=ml_kg, weight_kg=weight_kg)
        # Rate
        contrast_ml = get_contrast_ml(ml_kg=ml_kg, weight_kg=weight_kg)
        # No delay
        if rate_formula == "no_delay":
            rate = (contrast_ml + 15) / 45
            rate_adj = math.ceil(rate * 10) / 10  # Round up to 1 decimal place
            show_calc = f"({contrast_ml} + 15) / 45 = {round(rate, 3)}"
        # Delay
        else:
            assert isinstance(delay_sec, (int, float)
                              ), "`delay_sec` must be a number"
            rate = (contrast_ml + 15) / (delay_sec - 20)
            rate_adj = math.ceil(rate * 10) / 10  # Round up to 1 decimal place
            show_calc = f"({contrast_ml} + 15) / ({delay_sec} - 20) = {round(rate, 3)}"

        # Substitute Fmt String
        self.str_design = design_template["chest_whole_abd"].format(weight_kg=weight_kg,
                                                                    kV=kV,
                                                                    noise_index=noise_index,
                                                                    delay_sec_calc=delay_sec_calc,
                                                                    contrast_calc=contrast_calc,
                                                                    rate_adj=rate_adj,
                                                                    show_calc=show_calc)

    def __str__(self):
        return self.str_design

    def __repr__(self) -> str:
        return self.str_design

# CTA Liver


class DesignCTAliver:
    """Design CTA Liver Class
    """
    def __init__(self, weight_kg: float, is_first_study: bool = False) -> None:
        """Design a CTA of the liver

        Args:
            weight_kg (float): Weight in kg
            is_first_study (bool, optional): `True` if this is the first study. Defaults to False.
        """
        # kV
        kV = get_kV(weight_kg)
        # Noise
        noise_index = 15 if is_first_study else 17
        # Delay
        cta_time = 20
        # Contrast
        ml_kg = 2.5  # CTA liver
        contrast_calc = get_contrast_str(ml_kg=ml_kg, weight_kg=weight_kg)
        # Rate
        contrast_ml = get_contrast_ml(ml_kg=ml_kg, weight_kg=weight_kg)
        rate = (contrast_ml + 15) / cta_time
        rate_adj = math.ceil(rate * 10) / 10  # Round up to 1 decimal place
        # Calc at the end
        show_calc = f"({contrast_ml} + 15) / {cta_time} = {round(rate, 3)}"

        # Substitute Fmt String
        self.str_design = design_template["cta_liver"].format(weight_kg=weight_kg,
                                                              kV=kV,
                                                              noise_index=noise_index,
                                                              cta_time=cta_time,
                                                              contrast_calc=contrast_calc,
                                                              rate_adj=rate_adj,
                                                              show_calc=show_calc)

    def __str__(self):
        return self.str_design

    def __repr__(self) -> str:
        return self.str_design

# HRCT

class DesignHRCTchest:
    """docstring for DesignHRCTchest."""
    def __init__(self, weight_kg: float, is_first_study: bool = False):
        # kV
        kV = get_kV(weight_kg)
        # Noise
        noise_index = 17 if is_first_study else 20
        # Substitute Fmt String
        self.str_design = design_template["hrct"].format(kV=kV,
                                                         noise_index=noise_index)
    def __str__(self):
        return self.str_design

    def __repr__(self) -> str:
        return self.str_design