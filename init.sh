#!/bin/bash
#? |-----------------------------------------------------------------------------------------------|
#? |  init.sh                                                                                      |
#? |                                                                                               |
#? |  Copyright (c) 2020 Belikhun. All right reserved                                              |
#? |  Licensed under the MIT License. See LICENSE in the project root for license information.     |
#? |-----------------------------------------------------------------------------------------------|

set -e

apt install curl
apt install python3
apt install python3-pip

pip3 install -r requirements.txt

echo -e "\033[1;32m✓\033[0m Cài Đặt Thành Công!"