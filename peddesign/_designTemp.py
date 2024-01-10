
design_template = {
    "chest": """-- Design CT --
CT chest, venous only
Body weight: {weight_kg} kg
kV: {kV}
mA: auto
Noise index: {noise_index}
Delay: 45 sec
Contrast: {contrast_calc}
Rate: {rate_adj} ml/sec {show_calc}
---
""",
    "whole_abd": """-- Design CT --
CT whole abdomen, venous only
Body weight: {weight_kg} kg
kV: {kV}
mA: auto
Noise index: {noise_index}
Delay: {delay_sec_calc} 
Contrast: {contrast_calc}
Rate: {rate_adj} ml/sec {show_calc}
---
""",
    "chest_whole_abd": """-- Design CT --
Venous chest + whole abdomen
Body weight: {weight_kg} kg
kV: {kV}
mA: auto
Noise index: {noise_index}
Delay: {delay_sec_calc} 
Contrast: {contrast_calc}
Rate: {rate_adj} ml/sec {show_calc}
---
""",
    "cta_liver": """-- Design CT --
CTA liver
Body weight: {weight_kg} kg
kV: {kV}
mA: auto
Noise index: {noise_index}
Delay: {cta_time} sec (CTA); 70 sec (Venous)
Contrast: {contrast_calc}
Rate: {rate_adj} ml/sec {show_calc}
---
"""
}
