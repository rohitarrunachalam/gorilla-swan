import subprocess
import logging

class FRRCommand:
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
        full_command = f'vtysh -c "{command}"'
        return self.run_vtysh_command(full_command)
