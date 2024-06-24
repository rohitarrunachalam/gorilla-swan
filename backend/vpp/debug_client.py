import logging
from command import VPPCommand

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class DebugClient:
    def __init__(self):
        self.vpp_command = VPPCommand()
        self.logger = logging.getLogger(__name__)

    def run_vpp_command(self, command):
        return self.vpp_command.run_vpp_command(command)

    ### Debug CLI Commands ###

    def execute_commands_from_file(self, file_path):
        command = f'exec {file_path}'
        return self.run_vpp_command(command)

    def show_cli_history(self):
        command = 'history'
        return self.run_vpp_command(command)

    def quit_cli(self):
        command = 'quit'
        return self.run_vpp_command(command)

    def set_terminal_ansi(self, enable=True):
        enable_str = 'on' if enable else 'off'
        command = f'set terminal ansi {enable_str}'
        return self.run_vpp_command(command)

    def set_terminal_history(self, enable=True, limit=None):
        enable_str = 'on' if enable else 'off'
        limit_str = f'limit {limit}' if limit is not None else ''
        command = f'set terminal history {enable_str} {limit_str}'
        return self.run_vpp_command(command)

    def set_terminal_pager(self, enable=True, limit=None):
        enable_str = 'on' if enable else 'off'
        limit_str = f'limit {limit}' if limit is not None else ''
        command = f'set terminal pager {enable_str} {limit_str}'
        return self.run_vpp_command(command)

    def show_terminal_settings(self):
        command = 'show terminal'
        return self.run_vpp_command(command)

    def show_unix_errors(self):
        command = 'show unix-errors'
        return self.run_vpp_command(command)

