import os
from dotenv import load_dotenv

env = os.getenv("ENV", "default") #ENV can be set to "staging", "dev" etc.
env_file = f".env.{env}" if env != "default" else ".env"

load_dotenv(dotenv_path=env_file)

class Config:
  BASE_URL = os.getenv("BASE_URL", "multi-step-form/index.html")
  DEFAULT_BROWSER = os.getenv("DEFAULT_BROWSER","chromium")
  HEADLESS =  os.getenv("HEADLESS", "true").lower() == "true"
  SLOW_MO = int(os.getenv("SLOW_MO", "0"))  # in milliseconds
  DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10000"))  # in milliseconds