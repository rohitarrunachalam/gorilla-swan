import logging
from command import VPPCommand  # Ensure VPPCommand is imported from the command module

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VPPClientPG:
    def __init__(self):
        self.vpp_command = VPPCommand()  # Initialize VPPCommand

    def execute_command(self, command):
        full_command = f'vppctl {command}'
        return self.vpp_command.run_vppctl_command(full_command)

    # VPP VNET/PG Commands
    def create_packet_generator(self):
        return self.execute_command("create packet-generator")

    def packet_generator(self):
        return self.execute_command("packet-generator")

    def packet_generator_capture(self):
        return self.execute_command("packet-generator capture")

    def packet_generator_configure(self):
        return self.execute_command("packet-generator configure")

    def packet_generator_delete(self):
        return self.execute_command("packet-generator delete")

    def packet_generator_disable_stream(self):
        return self.execute_command("packet-generator disable-stream")

    def packet_generator_enable_stream(self):
        return self.execute_command("packet-generator enable-stream")

    def packet_generator_new(self):
        return self.execute_command("packet-generator new")

    def show_packet_generator(self):
        return self.execute_command("show packet-generator")

# Example usage
if __name__ == "__main__":
    vpp_client_pg = VPPClientPG()

    # Example: Show Packet Generator
    stdout, stderr = vpp_client_pg.show_packet_generator()
    print("Show Packet Generator Output:", stdout)
    print("Show Packet Generator Error:", stderr)

    # Add additional example usages as needed for other commands
