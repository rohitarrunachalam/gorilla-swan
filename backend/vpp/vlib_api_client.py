import logging
from command import VPPCommand

logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VlibApiClient:
    def __init__(self):
        self.vpp_command = VPPCommand()
        self.logger = logging.getLogger(__name__)

    def api_trace(self, action=None, file=None):
        command = 'api trace'
        if action:
            command += f' {action}'
            if action in ['save', 'replay'] and file:
                command += f' {file}'
        return self.vpp_command.run_vpp_command(command)

    def test_node_serialize(self, max_threads=None):
        command = 'test node serialize'
        if max_threads:
            command += f' max-threads {max_threads}'
        command += ' nexts stats'
        return self.vpp_command.run_vpp_command(command)

    def clear_api_histogram(self):
        command = 'clear api histogram'
        return self.vpp_command.run_vpp_command(command)

    def set_api_trace(self):
        command = 'set api-trace'
        return self.vpp_command.run_vpp_command(command)

    def show_api(self):
        command = 'show api'
        return self.vpp_command.run_vpp_command(command)

    def show_api_clients(self):
        command = 'show api clients'
        return self.vpp_command.run_vpp_command(command)

    def show_api_histogram(self):
        command = 'show api histogram'
        return self.vpp_command.run_vpp_command(command)

    def show_api_message_table(self):
        command = 'show api message-table'
        return self.vpp_command.run_vpp_command(command)

    def show_api_plugin(self):
        command = 'show api plugin'
        return self.vpp_command.run_vpp_command(command)

    def show_api_ring_stats(self):
        command = 'show api ring-stats'
        return self.vpp_command.run_vpp_command(command)

    def show_pci(self, show_all=False):
        command = 'show pci'
        if show_all:
            command += ' all'
        return self.vpp_command.run_vpp_command(command)
