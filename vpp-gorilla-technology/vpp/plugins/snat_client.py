

import logging
from command import VPPCommand
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')



class SnatClient:
    def __init__(self):
        self.vpp_command = VPPCommand()
        self.logger = logging.getLogger(__name__)

    def run_vpp_command(self, command):
        return self.vpp_command.run_vpp_command(command)

    def set_interface_snat(self, in_intfc, out_intfc, delete=False):
        command = f'set interface snat in {in_intfc} out {out_intfc}'
        if delete:
            command += ' del'
        return self.run_vpp_command(command)

    def show_snat(self):
        command = 'show snat'
        return self.run_vpp_command(command)

    def snat_add_address(self, ip4_range_start, ip4_range_end=None):
        command = f'snat add addresses {ip4_range_start}'
        if ip4_range_end:
            command += f' - {ip4_range_end}'
        return self.run_vpp_command(command)
