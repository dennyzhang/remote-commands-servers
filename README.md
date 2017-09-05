Travis CI Status: [![Build Status](https://travis-ci.org/DennyZhang/remote-commands-servers.svg?branch=master)](https://travis-ci.org/DennyZhang/remote-commands-servers)

# remote-commands-servers
Run remote ssh commands on multiple servers

People can:
1. People can choose how many concurrent executors we support.
2. If the count of concurrent executors is 1, we run remote ssh commands sequentially.
3. People can specify whether to quit and abort following servers, if previous batch has any errors.
