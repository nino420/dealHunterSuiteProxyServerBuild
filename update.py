from lib import ehook
from lib.log import log
from colorama import init, Fore

import os
log("OKAY", "Imported: os")

import sys
log("OKAY", "Imported: sys")

import shutil
log("OKAY", "Imported: shutil")

from git.repo.base import Repo
log("OKAY", "Imported: git.repo.base.Repo")

from urllib.request import urlopen
log("OKAY", "Imported: urllib.request.urlopen")

init(autoreset=True)

REMOTE_GIT = "https://github.com/belivipro9x99/dealHunterSuiteProxyServerBuild.git"
REMOTE_VERSION_FILE = "https://raw.githubusercontent.com/belivipro9x99/dealHunterSuiteProxyServerBuild/master/version"
REMOTE_VERSION = None
VERSION = None

UPDATE_TMP = "./__update"

def logStatus(text, status, overWrite = False):
	statusText = [f"{Fore.RED}✗ ERRR", f"{Fore.YELLOW}● WAIT", f"{Fore.GREEN}✓ OKAY"]
	log("INFO", "{:48}{}{}".format(text, statusText[status + 1], Fore.RESET), resetCursor = (not overWrite))

if (os.path.isfile("version")):
	with open("version", "r") as f:
		VERSION = int(f.read())
else:
	log("ERRR", "Version file Not Found! Assuming VERSION = 0")
	VERSION = 0

log("OKAY", f"Current Version: {VERSION}")

remoteVersion = urlopen(REMOTE_VERSION_FILE).read(2)
REMOTE_VERSION = int(remoteVersion)
log("OKAY", f"Remote Version: {REMOTE_VERSION}")

if (REMOTE_VERSION > VERSION):
	log("INFO", "An update is available! Updating...")

	logStatus("Removing Old Update", 0)
	shutil.rmtree(UPDATE_TMP)
	logStatus("Removing Old Update", 1, True)

	logStatus("Cloning From Remote", 0)
	Repo.clone_from(REMOTE_GIT, UPDATE_TMP)
	logStatus("Cloning From Remote", 1, True)

	logStatus("Copying Files", 0)
	uFiles = os.listdir(UPDATE_TMP)

	for uFile in uFiles:
		if (uFile in [".git"]):
			continue

		target = f"{UPDATE_TMP}/{uFile}"
		dest = f"../{uFile}"
		logStatus(f"Copying Files: {target} -> {dest}", 0, True)

		if (os.path.isfile(target)):
			shutil.copy2(target, dest)
		else:
			shutil.copytree(target, dest)

	logStatus("Copying Files", 1, True)

	log("INFO", "Updated Successfully! Restarting...")

	args = sys.argv[:]
	log("DEBG", 'Re-spawning %s' % ' '.join(args))

	args.insert(0, sys.executable)
	if sys.platform == 'win32':
		args = ['"%s"' % arg for arg in args]

	os.execv(sys.executable, args)
else:
	log("OKAY", "Proxy Server is Up To Date! Starting Server...")

	tSize = os.get_terminal_size()
	print("*" * tSize.columns)

	import proxy