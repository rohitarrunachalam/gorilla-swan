
import logging
from command import VPPCommand
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


class LbClient:
    def __init__(self):
        self.vpp_command = VPPCommand()
        self.logger = logging.getLogger(__name__)

    def run_vpp_command(self, command):
        return self.vpp_command.run_vpp_command(command)

    def lb_as(self, vip_prefix, addresses=None, delete=False):
        command = f'lb as {vip_prefix}'
        if addresses:
            for addr in addresses:
                command += f' {addr}'
        if delete:
            command += ' del'
        return self.run_vpp_command(command)

    def lb_bypass(self, prefix, address, disable=False):
        command = f'lb bypass {prefix} {address}'
        if disable:
            command += ' disable'
        return self.run_vpp_command(command)

    def lb_conf(self, ip4_src_address=None, ip6_src_address=None, buckets=None, timeout=None):
        command = 'lb conf'
        if ip4_src_address:
            command += f' ip4-src-address {ip4_src_address}'
        if ip6_src_address:
            command += f' ip6-src-address {ip6_src_address}'
        if buckets:
            command += f' buckets {buckets}'
        if timeout:
            command += f' timeout {timeout}'
        return self.run_vpp_command(command)

    def lb_vip(self, prefix, encap=None, new_len=None, delete=False):
        command = f'lb vip {prefix}'
        if encap:
            command += f' encap {encap}'
        if new_len:
            command += f' new_len {new_len}'
        if delete:
            command += ' del'
        return self.run_vpp_command(command)

    def show_lb(self):
        command = 'show lb'
        return self.run_vpp_command(command)

    def show_lb_vips(self, verbose=False):
        command = 'show lb vips'
        if verbose:
            command += ' verbose'
        return self.run_vpp_command(command)
