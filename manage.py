__author__ = 'LMai'
import os
from app import create_app

config_file = os.path.abspath('config.py')
app = create_app(config_file)

if __name__ == '__main__':
    app.run(debug=True)
