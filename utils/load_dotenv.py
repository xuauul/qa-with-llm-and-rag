class DictToAttr:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

def load_dotenv():
  env = dict()

  with open('.env', 'r') as file:
    for line in file:
      line = line.strip()

      if line and not line.startswith('#'):
        key, value = line.split('=', 1)
        env[key.strip()] = value.strip()

  return DictToAttr(**env)