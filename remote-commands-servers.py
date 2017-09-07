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
## Updated: Time-stamp: <2017-09-07 17:22:18>
##-------------------------------------------------------------------
import sys
import paramiko
import argparse

def remote_commands_servers(server_list, executor_count, avoid_abort, command_list, ssh_parameter_list):
    failed_server_list = []
    print("Run remote commands: %s" % (command_list))
    # TODO: avoid_abort
    # TODO: executor_count
    for server in server_list:
        [ip, port] = server
        (exit_code, detail) = run_remote_ssh(ip, port, command_list, ssh_parameter_list)
        if exit_code != 0:
            failed_server_list.append(ip)
        print("Exit code: %d, Detail: %s" % (exit_code, detail))
    return failed_server_list

################################################################################
def get_ssh_server_list(server_list):
    l = []
    for line in server_list.split(','):
        line = line.strip()
        if line == '' or line.startswith('#') is True:
            continue
        [ip, port] = line.split(':')
        port = int(port)
        l.append([ip, port])
    return l

def run_remote_ssh(ip, port, ssh_command, ssh_parameter_list):
    [ssh_username, ssh_key_file, key_passphrase] = ssh_parameter_list
    print("Run ssh command in %s:%d" % (ip, port))
    import logging
    logging.getLogger("paramiko").setLevel(logging.WARNING)
    output = ""
    info_dict = {}
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        key = paramiko.RSAKey.from_private_key_file(ssh_key_file, password=key_passphrase)
        ssh.connect(ip, username=ssh_username, port=port, pkey=key)
        stdin, stdout, stderr = ssh.exec_command(ssh_command)
        exit_code = stdout.channel.recv_exit_status()
        stdout_str = "\n".join(stdout.readlines())
        stderr_str = "\n".join(stderr.readlines())
        ssh.close()
        return (exit_code, "stdout: %s\nstderr: %s" % (stdout_str, stderr_str))
    except:
        return (1, "Unexpected on server: %s error: %s" % (ip, sys.exc_info()[0]))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--server_list', required=True, \
                        help="A list of ip-port. Separated by comma.", type=str)
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

    server_list = []
    try:
        server_list = get_ssh_server_list(l.server_list)
    except Exception as e:
        print("Unexpected error in parsing server_list: %s, %s" % (sys.exc_info()[0], e))
        sys.exit(1)

    ssh_parameter_list = [l.ssh_username, l.ssh_key_file, l.key_passphrase]
    failed_server_list = remote_commands_servers(server_list, l.executor_count, \
                                                 l.avoid_abort, l.command_list, ssh_parameter_list)
    if len(failed_server_list) == 0:
        print("OK: Actions succeed!")
        sys.exit(0)
    else:
        print("ERROR: Failed servers: %s" % (','.join(failed_server_list)))
        sys.exit(1)
## File : remote-commands-servers.py ends
