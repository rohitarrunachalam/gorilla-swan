import logging
from command import FRRCommand

# Configure logging
logging.basicConfig(filename='logs/frrpy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class FRRClientRouteMap:
    def __init__(self):
        self.frr_command = FRRCommand()

    def run_vtysh_command(self, command):
        return self.frr_command.run_vtysh_command(command)

     # Route Map Commands
    def create_route_map_entry(self, name, action, order):
        command = f'configure terminal ; route-map {name} {action} {order}'
        return self.run_vtysh_command(command)

    def add_route_map_match(self, name, match_type, match_value):
        command = f'configure terminal ; route-map {name} match {match_type} {match_value}'
        return self.run_vtysh_command(command)

    def add_route_map_set(self, name, set_type, set_value):
        command = f'configure terminal ; route-map {name} set {set_type} {set_value}'
        return self.run_vtysh_command(command)

    def call_route_map(self, name, map_to_call):
        command = f'configure terminal ; route-map {name} call {map_to_call}'
        return self.run_vtysh_command(command)

    def set_route_map_exit_action(self, name, action):
        command = f'configure terminal ; route-map {name} {action}'
        return self.run_vtysh_command(command)

    def enable_route_map_optimization(self, name):
        command = f'configure terminal ; route-map {name} optimization'
        return self.run_vtysh_command(command)

    def show_route_map(self, name=None, json_format=False):
        command = 'show route-map'
        if name:
            command += f' {name}'
        if json_format:
            command += ' json'
        return self.run_vtysh_command(command)

    def clear_route_map_counters(self, name=None):
        command = 'clear route-map counter'
        if name:
            command += f' {name}'
        return self.run_vtysh_command(command)

    def debug_route_map_match(self, name, prefix, address_mode=None):
        command = f'debug route-map {name} match {prefix}'
        if address_mode:
            command += f' {address_mode}'
        return self.run_vtysh_command(command)
