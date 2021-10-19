import yaml
from yaml.loader import SafeLoader

f = open("Rasa_Bot/config.yml")
a = yaml.load(f, Loader=SafeLoader)
hist = max([a['policies'][i]['max_history'] for i in range(len(a['policies'])) if not a['policies'][i]['name'] == 'RulePolicy'])

print(hist)