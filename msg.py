import sys
import os
import time
import inspect

def info(message):
    target_file = os.path.splitext(os.path.basename(inspect.stack()[1].filename))[0]
    sys.stdout.write(f"[{target_file}]\033[32m [INFO]\033[0m " + str(message) + "\n")

def dbg(message):
    target_file = os.path.splitext(os.path.basename(inspect.stack()[1].filename))[0]
    sys.stdout.write(f"[{target_file}]\033[90m [DEBUG] @{time.time()}\033[0m " + str(message) + "\n")

def error(message):
    target_file = os.path.splitext(os.path.basename(inspect.stack()[1].filename))[0]
    sys.stderr.write(f"[{target_file}]\033[31m [ERROR]" + str(message) + "\033[0m\n")

def fetal_error(message):
    sys.stderr.write("\n\033[31m=!=========FATAL ERROR=========!=\n")
    sys.stderr.write(message + "\n")
    sys.stderr.write("=================================\033[0m\n")
