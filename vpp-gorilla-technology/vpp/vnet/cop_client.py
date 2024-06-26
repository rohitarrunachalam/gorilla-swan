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


