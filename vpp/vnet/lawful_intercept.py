import logging
from command import VPPCommand  # Ensure VPPCommand is imported from the command module

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VPPClientLawfulIntercept:
    def __init__(self):
        self.vpp_command = VPPCommand()  # Initialize VPPCommand

    def execute_command(self, command):
        full_command = f'vppctl {command}'
        return self.vpp_command.run_vppctl_command(full_command)

    # VPP VNET/Lawful Intercept Commands
    def set_lawful_intercept(self, interface, direction, port):
        return self.execute_command(f"set li interface {interface} direction {direction} port {port}")

# Example usage
if __name__ == "__main__":
    vpp_client_li = VPPClientLawfulIntercept()

    # Example: Set Lawful Intercept
    stdout, stderr = vpp_client_li.set_lawful_intercept("eth0", "ingress", 1234)
    print("Set Lawful Intercept Output:", stdout)
    print("Set Lawful Intercept Error:", stderr)

    # Add additional example usages as needed for other commands
