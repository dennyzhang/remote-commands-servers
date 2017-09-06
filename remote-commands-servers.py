#!/usr/bin/python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://raw.githubusercontent.com/DennyZhang/devops_public/master/LICENSE
##
## File : remote-commands-servers.py
## Author : Denny <contact@dennyzhang.com>
## Description :
## --
## Created : <2017-09-05>
## Updated: Time-stamp: <2017-09-05 19:20:22>
##-------------------------------------------------------------------
import sys
import paramiko
import argparse

def run_remote_ssh(server, username, ssh_port, ssh_key_file, key_passphrase, ssh_command):
    import logging
    logging.getLogger("paramiko").setLevel(logging.WARNING)
    output = ""
    info_dict = {}
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        key = paramiko.RSAKey.from_private_key_file(ssh_key_file, password=key_passphrase)
        ssh.connect(server, username=username, port=ssh_port, pkey=key)
        stdin, stdout, stderr = ssh.exec_command(ssh_command)
        output = "\n".join(stdout.readlines())
        ssh.close()
        output = (stdin, stdout, stderr)
        # info_dict = json.loads(output)
        return (server, output, None)
    except:
        return (server, (), "Unexpected on server: %s error: %s" % (server, sys.exc_info()[0]))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--server_list', required=True, \
                        help="A list of servers to run the remote ssh commands", type=str)
    parser.add_argument('--command_list', required=True, \
                        help="A list of commands to run", type=str)
    parser.add_argument('--executor_count', default=1, \
                        help="How many concurrent executors to run. Default value is 1.", type=int)
    parser.add_argument('--ssh_username', default="root", \
                        help="SSH username", type=str)
    parser.add_argument('--ssh_key_file', required=True, \
                        help="SSH private key file. Here we assume the same key file works for all servers.", type=str)
    parser.add_argument('--key_passphrase', default="", \
                        help="Key passphrase for SSH private key file. If not given, key file is assumed unencrypted.", \
                        type=str)
    parser.add_argument('--avoid_abort', dest='avoid_abort', action='store_true', default=False, \
                        help="Whether to avoid abort. By default, any node failure will abort the whole process")
    l = parser.parse_args()
## File : remote-commands-servers.py ends
