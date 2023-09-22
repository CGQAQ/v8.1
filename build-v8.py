#!/usr/bin/env python3

import os
import sys
import subprocess

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'depot_tools'))
os.environ["PATH"] = (os.path.join(os.path.dirname(__file__), 'depot_tools')) + os.pathsep + os.environ["PATH"]

subprocess.check_call(['vpython3.bat', './depot_tools/update_depot_tools_toggle.py', '--disable'])

subprocess.check_call(['vpython3.bat', './depot_tools/gclient.py', 'config', 
"--spec=solutions = ["
"{"
'  "name": "v8",'
'  "url": "https://chromium.googlesource.com/v8/v8.git", '
'  "deps_file": "DEPS", '
'  "managed": False, '
'  "custom_deps": {}, '
'},'
"]"
])
subprocess.check_call(['gclient.bat', 'sync', '--with_branch_heads'])

subprocess.check_call(['gn.bat', 'gen', 'out/Default', 'v8'])