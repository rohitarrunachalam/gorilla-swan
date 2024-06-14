import logging
from command import FRRCommand

# Configure logging
logging.basicConfig(filename='logs/frrpy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class FRRClientFiltering:
    def __init__(self):
        self.frr_command = FRRCommand()

    def run_vtysh_command(self, command):
        return self.frr_command.run_vtysh_command(command)

    # Access List Commands
    def create_access_list(self, name, seq, action, network):
        if seq:
            command = f'configure terminal ; ip access-list {name} seq {seq} {action} {network}'
        else:
            command = f'configure terminal ; ip access-list {name} {action} {network}'
        return self.run_vtysh_command(command)

    def show_access_lists(self, name=None, json_output=False):
        if name:
            command = f'show ip access-list {name}'
        else:
            command = f'show ip access-list'
        if json_output:
            command += ' json'
        return self.run_vtysh_command(command)

    # IP Prefix List Commands
    def create_prefix_list(self, name, seq, action, prefix, le=None, ge=None):
        if seq:
            command = f'configure terminal ; ip prefix-list {name} seq {seq} {action} {prefix}'
        else:
            command = f'configure terminal ; ip prefix-list {name} {action} {prefix}'
        
        if le:
            command += f' le {le}'
        if ge:
            command += f' ge {ge}'
        
        return self.run_vtysh_command(command)

    def add_prefix_list_description(self, name, description):
        command = f'configure terminal ; ip prefix-list {name} description {description}'
        return self.run_vtysh_command(command)

    def show_prefix_lists(self, name=None, seq=None, prefix=None, summary=False, detail=False, json_output=False):
        if summary:
            command = 'show ip prefix-list summary'
        elif detail:
            if name:
                command = f'show ip prefix-list {name} detail'
            else:
                command = 'show ip prefix-list detail'
        else:
            if name and seq:
                command = f'show ip prefix-list {name} seq {seq}'
            elif name and prefix:
                command = f'show ip prefix-list {name} {prefix}'
            elif name:
                command = f'show ip prefix-list {name}'
            else:
                command = 'show ip prefix-list'
        
        if json_output:
            command += ' json'
        
        return self.run_vtysh_command(command)

    def debug_prefix_list_match(self, name, prefix, address_mode=None):
        if address_mode:
            command = f'debug prefix-list {name} match {prefix} {address_mode}'
        else:
            command = f'debug prefix-list {name} match {prefix}'
        return self.run_vtysh_command(command)

    def clear_prefix_list_counters(self, name=None, prefix=None):
        if name and prefix:
            command = f'clear ip prefix-list {name} {prefix}'
        elif name:
            command = f'clear ip prefix-list {name}'
        else:
            command = 'clear ip prefix-list'
        return self.run_vtysh_command(command)
