import configparser

config = configparser.ConfigParser()
print(config.sections())

config.read('example.ini')
print(config.sections())

for k in config['database']:
    print(f'database.{k}: {config["database"][k]}')

print(config.get('database', 'username', fallback='sa'))
