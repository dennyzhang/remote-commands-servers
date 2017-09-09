Travis CI Status: [![Build Status](https://travis-ci.org/DennyZhang/remote-commands-servers.svg?branch=master)](https://travis-ci.org/DennyZhang/remote-commands-servers)

# remote-commands-servers
Run remote ssh commands on multiple servers

You can:
1. Choose whether to run sequentially or in parallel. By default, it's sequential.
2. When sequentially, it will abort immediately if any node has failed. Customize by **--avoid_abort**.

Assumptions:
- All ssh servers accept the same username
- All ssh servers accept the same ssh private key

# Online Usage
```
Denny: mac$ python ./remote-commands-servers.py --help
usage: remote-commands-servers.py [-h] --server_list SERVER_LIST [--command_list COMMAND_LIST] [--command_file COMMAND_FILE]
                                  [--ssh_username SSH_USERNAME] --ssh_key_file SSH_KEY_FILE [--key_passphrase KEY_PASSPHRASE]
                                  [--enable_parallel] [--avoid_abort]

optional arguments:
  -h, --help            show this help message and exit
  --server_list SERVER_LIST
                        A list of ip-port. Separated by comma
  --command_list COMMAND_LIST
                        A list of commands to run
  --command_file COMMAND_FILE
                        File to host bash command. If --command_list no given, use this one
  --ssh_username SSH_USERNAME
                        SSH username
  --ssh_key_file SSH_KEY_FILE
                        SSH private key file. Here we assume the same key file works for all servers
  --key_passphrase KEY_PASSPHRASE
                        Key passphrase for SSH private key file. If not given, key file is in plain text
  --enable_parallel     By default, it's sequential. If enabled, we will run commands in all nodes simultaneously
  --avoid_abort         When sequentially, whether to keep going if some nodes have failed
```

# Different Scenarios
- Paralell
```
python ./remote-commands-servers.py \
    --server_list "45.33.88.175:2702, www.dennyzhang.com:23, test.dennyzhang.com:2703" \
    --command_list "date && hostname" --ssh_username "root" \
    --enable_parallel \
    --ssh_key_file "/Users/mac/.ssh/id_rsa" --key_passphrase "mykeypass"
```

- Sequential
```
python ./remote-commands-servers.py \
    --server_list "45.33.88.175:2702, www.dennyzhang.com:23, test.dennyzhang.com:2703" \
    --command_list "date && hostname" --ssh_username "root" \
    --ssh_key_file "/Users/mac/.ssh/id_rsa" --key_passphrase "mykeypass"
```

- Sequential, abort if any errors
```
python ./remote-commands-servers.py \
    --server_list "45.33.88.175:2702, www.dennyzhang.com:23, test.dennyzhang.com:2703" \
    --command_list "date; false && hostname" --ssh_username "root" \
    --ssh_key_file "/Users/mac/.ssh/id_rsa" --key_passphrase "mykeypass"
```

- Sequential, avoid fast fail
```
python ./remote-commands-servers.py \
    --server_list "45.33.88.175:2702, www.dennyzhang.com:23, test.dennyzhang.com:2703" \
    --command_list "date; false && hostname" --ssh_username "root" \
    --avoid_abort \
    --ssh_key_file "/Users/mac/.ssh/id_rsa" --key_passphrase "mykeypass"
```

Code is licensed under [MIT License](https://www.dennyzhang.com/wp-content/mit_license.txt).
