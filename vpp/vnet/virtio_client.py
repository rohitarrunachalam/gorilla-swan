import logging
from command import VPPCommand

logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


class VirtioClient:
    def __init__(self):
        self.vpp_command = VPPCommand()  # Assuming VPPCommand is appropriately defined
        self.logger = logging.getLogger(__name__)

    def run_vpp_command(self, command):
        self.logger.debug(f"Running command: {command}")
        return self.vpp_command.run_vpp_command(command)

    def create_vhost_user(self, socket_path, *options):
        command = f'create vhost-user {socket_path}'
        if options:
            command += f' {" ".join(options)}'
        return self.run_vpp_command(command)

    def delete_vhost_user(self, socket_path):
        command = f'delete vhost-user {socket_path}'
        return self.run_vpp_command(command)

    def show_vhost_user(self, socket_path=None):
        command = 'show vhost-user'
        if socket_path:
            command += f' {socket_path}'
        return self.run_vpp_command(command)
