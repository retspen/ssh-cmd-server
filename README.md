# SSH cmd server

Simple SSH server for running commands on remote machines.

## Usage

Run script `ssh_server.py` on your server.
```bash
$ python ssh_server.py 0.0.0.0 2222
```

Run script `ssh_rcmd.py` on remote machine that you wnat to run commands.
```bash
$ python ssh_rcmd.py 1.1.1.1 2222
```
