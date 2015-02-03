import os

os.environ['APP_SETTINGS'] = "config.DevelopmentConfig"

import seed


from Todo import app


if __name__ == '__main__':

    app.run()