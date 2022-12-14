import logging
import paramiko

logger = logging.getLogger(__name__)

class SFTP(object):
    def __init__(self, host, username, key):
        self.host = host
        self.username = username
        self.key = key
        
        self.ssh_obj, self.sftp_obj = self.get_sftp()
        
    def get_sftp(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.host, username=self.username, key_filename = self.key)
        assert self.ssh.get_transport().is_active(), 'Failed to connect to server'
        return self.ssh, self.ssh.open_sftp()
        
    def check_connection(function):
        def deco(self, *args, **kwargs):
            if self.sftp_obj is None:
                self.ssh_obj, self.sftp_obj = self.get_sftp()
            else:
                ret = getattr(self.ssh.get_transport(), 'is_active', None)
                if ret is None or (ret is not None and not ret()):
                    self.ssh_obj, self.sftp_obj = self.get_sftp()
            return function(self, *args, **kwargs)
        return deco
        
    @check_connection
    def command(self, input):
        stdin, stdout, stderr = self.ssh.exec_command(input)
        stdin.flush()
        stdin.channel.shutdown_write()
        ret = stdout.read()
        err = stderr.read()
        if ret:
            return ret
        elif err:
            return err
        else:
            return None
            
            