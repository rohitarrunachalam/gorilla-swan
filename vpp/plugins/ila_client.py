import logging
from command import VPPCommand
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')



class IlaClient:
    def __init__(self):
        self.vpp_command = VPPCommand()
        self.logger = logging.getLogger(__name__)

    def run_vpp_command(self, command):
        return self.vpp_command.run_vpp_command(command)

    def ila_entry(self, type=None, sir_address=None, locator=None, vnid=None, adj_index=None, next_hop=None, direction=None, csum_mode=None, delete=False):
        command = 'ila entry'
        if type:
            command += f' type {type}'
        if sir_address:
            command += f' sir-address {sir_address}'
        if locator:
            command += f' locator {locator}'
        if vnid:
            command += f' vnid {vnid}'
        if adj_index:
            command += f' adj-index {adj_index}'
        if next_hop:
            command += f' next-hop {next_hop}'
        if direction:
            command += f' direction {direction}'
        if csum_mode:
            command += f' csum-mode {csum_mode}'
        if delete:
            command += ' del'
        return self.run_vpp_command(command)

    def ila_interface(self, interface_name, disable=False):
        command = f'ila interface {interface_name}'
        if disable:
            command += ' disable'
        return self.run_vpp_command(command)

    def show_ila_entries(self):
        command = 'show ila entries'
        return self.run_vpp_command(command)
