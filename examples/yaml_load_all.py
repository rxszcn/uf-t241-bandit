import yaml

# load_all family via module attribute (should trigger B506)
docs = list(yaml.load_all("{}"))

# safe Loader exclusion path (should NOT trigger B506)
yaml.load_all("{}", Loader=yaml.SafeLoader)
yaml.load_all("{}", Loader=yaml.CSafeLoader)
