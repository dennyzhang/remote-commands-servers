Travis CI Status: [![Build Status](https://travis-ci.org/DennyZhang/remote-commands-servers.svg?branch=master)](https://travis-ci.org/DennyZhang/remote-commands-servers)

# remote-commands-servers
Run remote ssh commands on multiple servers

People can:
1. People can choose how many concurrent executors to run. By default, it's 1.
2. If executors count is 1, we run remote ssh commands sequentially.
3. By default, it will abort immediately, if previous batch has any errors. People can customize by providing --avoid_abort option.

# Usage
```
Denny: mac$ python ./remote-commands-servers.py --help
usage: remote-commands-servers.py [-h] --server_list SERVER_LIST [--executor_count EXECUTOR_COUNT]
                                  [--ssh_username SSH_USERNAME] --ssh_key_file SSH_KEY_FILE [--key_passphrase KEY_PASSPHRASE]
                                  [--avoid_abort]

optional arguments:
  -h, --help            show this help message and exit
  --server_list SERVER_LIST
                        A list of servers to run the remote ssh commands
  --executor_count EXECUTOR_COUNT
                        How many concurrent executors to run. Default value is 1.
  --ssh_username SSH_USERNAME
                        SSH username
  --ssh_key_file SSH_KEY_FILE
                        SSH private key file. Here we assume the same key file works for all servers.
  --key_passphrase KEY_PASSPHRASE
                        Key passphrase for SSH private key file. If not given, key file is assumed unencrypted.
  --avoid_abort         Whether to avoid abort. By default, any node failure will abort the whole process
```

Notice:
- Here we assume all remote servers can accept ssh by the same ssh private key file.
