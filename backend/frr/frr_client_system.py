import subprocess
import logging
import command

# Configure logging
logging.basicConfig(filename='logs/frrpy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class FRRClientSystem:
    def __init__(self):
        pass

    def execute_command(self, command):
        frr_command = frr_command()
        full_command = f'vtysh -c "{command}"'
        return frr_command.run_vtysh_command(full_command)

    # General Commands
    def get_version(self):
        return self.execute_command("show version")

    def get_interfaces(self):
        return self.execute_command("show ip interface brief")

    # Additional commands can be added as needed
