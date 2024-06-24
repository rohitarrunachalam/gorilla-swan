import logging
from command import VPPCommand  # Ensure VPPCommand is imported from the command module

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VPPClientUnix:
    def __init__(self):
        self.vpp_command = VPPCommand()  # Initialize VPPCommand

    def execute_command(self, command):
        full_command = f'vppctl {command}'
        return self.vpp_command.run_vppctl_command(full_command)

    # VPP VNET/Unix Commands
    def show_gdb(self):
        return self.execute_command("show gdb")

    def tap_connect(self):
        return self.execute_command("tap connect")

    def tap_delete(self):
        return self.execute_command("tap delete")

    def tap_modify(self):
        return self.execute_command("tap modify")

# Example usage
if __name__ == "__main__":
    vpp_client_unix = VPPClientUnix()

    # Example: Show GDB
    stdout, stderr = vpp_client_unix.show_gdb()
    print("Show GDB Output:", stdout)
    print("Show GDB Error:", stderr)

    # Add additional example usages as needed for other commands
