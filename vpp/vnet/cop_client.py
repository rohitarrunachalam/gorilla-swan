import logging
from command import VPPCommand

logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


class COPClient:
    def __init__(self):
        self.vpp_command = VPPCommand()  # Assuming VPPCommand is appropriately defined
        self.logger = logging.getLogger(__name__)

    def run_vpp_command(self, command):
        self.logger.debug(f"Running command: {command}")
        return self.vpp_command.run_vpp_command(command)

    def cop_interface(self, interface_name, *options):
        command = f'cop interface {interface_name}'
        if options:
            command += f' {" ".join(options)}'
        return self.run_vpp_command(command)

    def cop_whitelist(self, *options):
        command = 'cop whitelist'
        if options:
            command += f' {" ".join(options)}'
        return self.run_vpp_command(command)


# Example usage
if __name__ == "__main__":
    client = COPClient()

    # Example command execution
    print(client.cop_interface('GigabitEthernet0/8/0', 'input-acl', '1'))
    print(client.cop_whitelist('add', '10.0.0.1'))
