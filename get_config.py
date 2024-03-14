import logging
from requests import get as rget
import os
import subprocess

def set_permissions(directory):
    os.chmod(directory, 0o777)

CLONE_DIR = '/VJ-FILTER-BOT'

UPSTREAM_REPO = os.environ.get('UPSTREAM_REPO')
if not UPSTREAM_REPO:
    print("Cloning main Repository")
    subprocess.run(['git', 'clone', 'https://github.com/Tamilupdates/VJ-FILTER-BOT.git', CLONE_DIR])
else:
    print(f"Cloning Custom Repo from {UPSTREAM_REPO}")
    subprocess.run(['git', 'clone', UPSTREAM_REPO, CLONE_DIR])

set_permissions(CLONE_DIR)

os.chdir(CLONE_DIR)

subprocess.run(['pip3', 'install', '-U', '-r', 'requirements.txt'])
print("Starting Bot....")
subprocess.run(['python3', 'bot.py'])

logging.basicConfig(level=logging.ERROR)
LOGGER = logging.getLogger(__name__)

CONFIG_FILE_URL = os.environ.get('CONFIG_FILE_URL')
try:
    if not CONFIG_FILE_URL:
        raise ValueError("CONFIG_FILE_URL is missing or empty")

    res = rget(CONFIG_FILE_URL)

    if res.status_code == 200:
        # Write the content to info.py file
        with open('info.py', 'wb+') as f:
            f.write(res.content)
        LOGGER.info("info.py downloaded successfully!")
    else:
        LOGGER.error(f"Failed to download info.py: {res.status_code}")
except Exception as e:
    LOGGER.error(f"Error downloading CONFIG_FILE_URL: {e}")