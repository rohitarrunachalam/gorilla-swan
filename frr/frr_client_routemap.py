import subprocess
import logging
from command import FRRCommand

# Configure logging
logging.basicConfig(filename='logs/frrpy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class FRRClientRouteMap:
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

    # Route Map Commands
    def add_route_map(self, name, action, order):
        command = f"route-map {name} {action} {order}"
        return self.execute_command(command)

    def remove_route_map(self, name):
        command = f"no route-map {name}"
        return self.execute_command(command)
