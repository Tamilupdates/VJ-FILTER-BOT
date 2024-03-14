import logging
from requests import get as rget
import os
import subprocess

# Define the UPSTREAM_REPO variable here
UPSTREAM_REPO = os.environ.get('UPSTREAM_REPO')

if not UPSTREAM_REPO:
    print("Cloning main Repository")
    subprocess.run(['git', 'clone', 'https://github.com/Tamilupdates/VJ-FILTER-BOT.git', '/VJ-FILTER-BOT'])
else:
    print(f"Cloning Custom Repo from {UPSTREAM_REPO}")
    subprocess.run(['git', 'clone', UPSTREAM_REPO, '/VJ-FILTER-BOT'])

os.chdir('/VJ-FILTER-BOT')
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
        with open('info.py', 'wb+') as f:
            f.write(res.content)
    else:
        LOGGER.error(f"Failed to download info.py {res.status_code}")
except Exception as e:
    LOGGER.error(f"Error downloading CONFIG_FILE_URL: {e}")