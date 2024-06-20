import logging
from command import VPPCommand

logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


class CdpClient:
    def __init__(self):
        self.vpp_command = VPPCommand()  # Assuming VPPCommand is appropriately defined
        self.logger = logging.getLogger(__name__)

    def run_vpp_command(self, command):
        self.logger.debug(f"Running command: {command}")
        return self.vpp_command.run_vpp_command(command)

    def show_cdp(self):
        """
        Summary/usage:
        Show cdp command.

        Declaration:
        show_cdp_command (vnet/vnet/cdp/cdp_input.c:448)

        Implementation:
        show_cdp.
        """
        command = 'show cdp'
        return self.run_vpp_command(command)
