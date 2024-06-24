import logging
from command import VPPCommand  # Ensure VPPCommand is imported from the command module

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VPPClientPolicer:
    def __init__(self):
        self.vpp_command = VPPCommand()  # Initialize VPPCommand

    def execute_command(self, command):
        full_command = f'vppctl {command}'
        return self.vpp_command.run_vppctl_command(full_command)

    # VPP VNET/Policer Commands
    def test_policer(self):
        return self.execute_command("test policer")

    def configure_policer(self, policer_index, policer_params):
        return self.execute_command(f"configure policer {policer_index} {policer_params}")

    def show_policer(self):
        return self.execute_command("show policer")

# Example usage
if __name__ == "__main__":
    vpp_client_policer = VPPClientPolicer()

    # Example: Show Policier
    stdout, stderr = vpp_client_policer.show_policer()
    print("Show Policier Output:", stdout)
    print("Show Policier Error:", stderr)

    # Add additional example usages as needed for other commands
