import os
from website import app

USER_PATH='/Users/hq/PycharmProjects/Object Detection Web App based Flask'

if __name__=="__main__":
  app.secret_key = "super secret key"
  app.run(port=5011)