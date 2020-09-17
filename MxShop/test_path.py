from pathlib import Path
import sys
BASE_DIR = Path(__file__).resolve().parent.parent

print(str(BASE_DIR))
print(str(BASE_DIR/'apps'))
print(str(BASE_DIR/'extra_apps'))

sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR/'apps'))
sys.path.insert(0, str(BASE_DIR/'extra_apps'))