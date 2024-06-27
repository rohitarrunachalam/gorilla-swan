import logging
from vpp_papi import VPPApiClient  # Replace with the actual import statement for VPP PAPI

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class DebugClient:
    def __init__(self):
        self.vpp_api = VPPApiClient()  # Initialize VPP PAPI client
        self.logger = logging.getLogger(__name__)

    def run_vpp_command(self, command):
        self.logger.debug(f"Running command: {command}")
        # Example assuming VPPApiClient.execute_command exists
        return self.vpp_api.execute_command(command)

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

# Example usage
if __name__ == "__main__":
    debug_client = DebugClient()

    # Example: Execute commands from file
    file_path = "/path/to/commands.txt"
    stdout, stderr = debug_client.execute_commands_from_file(file_path)
    print("Execute Commands from File Output:", stdout)
    print("Execute Commands from File Error:", stderr)

    # Example: Show CLI history
    stdout, stderr = debug_client.show_cli_history()
    print("Show CLI History Output:", stdout)
    print("Show CLI History Error:", stderr)

    # Add additional example usages as needed for other commands
