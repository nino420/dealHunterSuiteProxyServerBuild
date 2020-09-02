#? |-----------------------------------------------------------------------------------------------|
#? |  build/build.py                                                                               |
#? |                                                                                               |
#? |  Copyright (c) 2020 Belikhun. All right reserved                                              |
#? |  Licensed under the MIT License. See LICENSE in the project root for license information.     |
#? |-----------------------------------------------------------------------------------------------|

from lib import ehook
from lib.log import log

import os
log("OKAY", "Imported: os")

import py_compile
log("OKAY", "Imported: py_compile")

# =============== COMPILE ===============
CINPUT = "proxy.py"
CTARGET = "proxy.pyc"
log("INFO", f"Compiling {CINPUT}")

if (not os.path.isfile(CINPUT)):
	raise FileNotFoundError(f"File {CINPUT} does not exist!")

py_compile.compile(CINPUT, cfile = CTARGET)
log("OKAY", f"Compiled {CINPUT} -> {CTARGET}")