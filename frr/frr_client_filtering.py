import subprocess
import logging
from command import FRRCommand

# Configure logging
logging.basicConfig(filename='logs/frrpy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class FRRClientFiltering:
    def __init__(self):
        pass

    def run_vtysh_command(self, command):
        try:
            logging.info(f"Running command: {command}")
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            stdout = result.stdout.decode('utf-8')
            stderr = result.stderr.decode('utf-8')
            if stderr:
                logging.error(f"Error executing command: {stderr}")
            return stdout, stderr
        except subprocess.CalledProcessError as e:
            logging.error(f"Command '{command}' failed with error: {e.stderr}")
            return "", str(e)
        except Exception as e:
            logging.exception(f"Unexpected error: {e}")
            return "", str(e)

    def execute_command(self, command):
        frr_command = FRRCommand()
        full_command = f'vtysh -c "{command}"'
        return frr_command.run_vtysh_command(full_command)

    # Access List Commands
    def add_access_list(self, name, action, network, seq=None):
        if seq:
            command = f"access-list {name} seq {seq} {action} {network}"
        else:
            command = f"access-list {name} {action} {network}"
        return self.execute_command(command)

    def remove_access_list(self, name, seq):
        command = f"no access-list {name} seq {seq}"
        return self.execute_command(command)

    # Prefix List Commands
    def add_prefix_list(self, name, action, prefix, seq=None, le=None, ge=None):
        command = f"ip prefix-list {name}"
        if seq:
            command += f" seq {seq}"
        command += f" {action} {prefix}"
        if le:
            command += f" le {le}"
        if ge:
            command += f" ge {ge}"
        return self.execute_command(command)

    def remove_prefix_list(self, name, seq):
        command = f"no ip prefix-list {name} seq {seq}"
        return self.execute_command(command)
