import os

stage = os.getenv('STAGE', 'DEV').upper()
if stage.startswith('PROD'):
    print(f'Running in production environment: {stage}')
else:
    print(f'{stage}: Running in developement environment')