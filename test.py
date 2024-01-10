import sys
from pathlib import Path

# sys.path.insert(1, str(Path(".").absolute() / "src"))
import peddesign  # noqa: E402


# print(Path(".").absolute()) # Project Root


peddesign.design_ct("whole_abd", 10)
