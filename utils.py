import json
# import tomllib
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


# Decorator for logging
def with_logging(log_file):
    def decorator(func):
        def wrapper(*args, **kwargs):
            org_stdout = sys.stdout
            org_stderr = sys.stderr
            # redirect stdout & err to log file
            with open(log_file, 'w') as f:
                sys.stdout = f
                sys.stderr = f
                try:
                    result = func(*args, **kwargs)
                except Exception as e:
                    print(e)
                finally:
                    sys.stdout = org_stdout
                    sys.stderr = org_stderr

            return result
        return wrapper
    return decorator


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

# Get stat of fasta file
def get_fasta_stat(fasta):
    cmd = f"seqkit stat {fasta}"
    output = subprocs(cmd)
    data = [line.split() for line in output.stdout.decode().strip().split('\n')]
    if len(data[1]) == 6:
        v = [data[1][0], data[1][1], data[1][2], '0', '0', '0', '0', '0']
        data[1] = v
    stat_ser = pd.Series(data[1], index=data[0])
    for col in ['num_seqs', 'sum_len', 'min_len', 'avg_len', 'max_len']:
        stat_ser[col] = stat_ser[col].replace(',','')
    return stat_ser
