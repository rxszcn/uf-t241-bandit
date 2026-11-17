from yaml import CSafeLoader
from yaml import Loader
from yaml import SafeLoader
from yaml import load
from yaml import load_all

# from-import form without a safe Loader (should trigger B506)
y = load("{}")

# load_all family via from-import (should trigger B506)
docs = list(load_all("{}"))

# explicit unsafe Loader via from-import (should trigger B506)
y2 = load("{}", Loader=Loader)

# safe Loader exclusion paths (should NOT trigger B506)
load("{}", Loader=SafeLoader)
load("{}", Loader=CSafeLoader)
load("{}", SafeLoader)
load("{}", CSafeLoader)
load_all("{}", Loader=SafeLoader)
load_all("{}", Loader=CSafeLoader)
