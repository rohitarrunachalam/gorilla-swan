import logging
from command import VPPCommand

logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


class GreClient:
    def __init__(self):
        self.vpp_command = VPPCommand()  # Assuming VPPCommand is appropriately defined
        self.logger = logging.getLogger(__name__)

    def run_vpp_command(self, command):
        self.logger.debug(f"Running command: {command}")
        return self.vpp_command.run_vpp_command(command)

    def create_gre_tunnel(self, tunnel_name, src_address, dst_address, outer_fib_id=None, session_id=None):
        command = f'create gre tunnel {tunnel_name} src {src_address} dst {dst_address}'
        if outer_fib_id:
            command += f' outer-fib-id {outer_fib_id}'
        if session_id:
            command += f' session-id {session_id}'
        return self.run_vpp_command(command)

    def show_gre_tunnel(self):
        command = 'show gre tunnel'
        return self.run_vpp_command(command)

