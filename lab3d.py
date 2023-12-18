#!/usr/bin/env python3
# Author ID: cfederici

import subprocess

space = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
output = space.communicate()
stdout = output[0].decode('utf-8').strip()
def free_space():
    stdout = output[0].decode('utf-8').strip()
    return (stdout)
print(stdout)

