import json
import toml
import time
import sys
import os, subprocess
from multiprocessing import Pool
import pandas as pd

# Configs
def parse_config(config_file):
    with open(config_file, 'rt') as f:
        # config = tomllib.load(f)
        config = toml.load(f)
    return config

# Decorator for time check
def time_check(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        return (res, end - start)
    return wrapper

# Multiprocessing
def subprocs(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True)
@time_check
def execute_command(cmds, pool_num):
    with Pool(pool_num) as p:
        output = p.map(subprocs, cmds)
    return output
@time_check
def execute_command_with_env(cmds, env, pool_num):
    env_wrapper_func = lambda cmd: f"conda run -n {env} /bin/bash -c '{cmd}'"
    cmds = [env_wrapper_func(cmd) for cmd in cmds]
    with Pool(pool_num) as p:
        output = p.map(subprocs, cmds)
    return output
@time_check
def execute_function_pool(function, arg_list, pool_num):
    with Pool(pool_num) as p:
        output = p.map(function, arg_list)
    return output
@time_check
def execute_function_pool_args(function, args_list, pool_num):
    with Pool(pool_num) as p:
        output = p.starmap(function, args_list)
    return output
