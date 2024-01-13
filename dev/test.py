import sys
from pathlib import Path

sys.path.insert(1, str(Path.cwd()))
# print(sys.path)
import peddesign  # noqa: E402

peddesign.design_ct("whole_abd", 10)
