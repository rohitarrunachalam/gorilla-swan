import logging
from command import VPPCommand  # Ensure VPPCommand is imported from the command module

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VPPAppCommands:
    def __init__(self):
        self.vpp_command = VPPCommand()  # Initialize VPPCommand

    def execute_command(self, command):
        full_command = f'vppctl {command}'
        return self.vpp_command.run_vppctl_command(full_command)

    # VPP App Commands
    def ip_sticky_classify(self):
        return self.execute_command("ip sticky classify")

    def show_sticky_classify(self):
        return self.execute_command("show sticky classify")

    def show_version(self):
        return self.execute_command("show version")

    def ip_virtual(self):
        return self.execute_command("ip virtual")

