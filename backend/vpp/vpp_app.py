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

# Example usage
if __name__ == "__main__":
    vpp_app = VPPAppCommands()

    # Example: IP Sticky Classify
    stdout, stderr = vpp_app.ip_sticky_classify()
    print("IP Sticky Classify Output:", stdout)
    print("IP Sticky Classify Error:", stderr)

    # Example: Show Sticky Classify
    stdout, stderr = vpp_app.show_sticky_classify()
    print("Show Sticky Classify Output:", stdout)
    print("Show Sticky Classify Error:", stderr)

    # Example: Show Version
    stdout, stderr = vpp_app.show_version()
    print("Show Version Output:", stdout)
    print("Show Version Error:", stderr)

    # Example: IP Virtual
    stdout, stderr = vpp_app.ip_virtual()
    print("IP Virtual Output:", stdout)
    print("IP Virtual Error:", stderr)

    # Add additional example usages as needed for other commands
