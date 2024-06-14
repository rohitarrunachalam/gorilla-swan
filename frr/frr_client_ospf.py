import logging
from command import FRRCommand

# Configure logging
logging.basicConfig(filename='logs/frrpy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


class FRRClientOSPF:
    def __init__(self):
        self.frr_command = FRRCommand()

    def run_vtysh_command(self, command):
        return self.frr_command.run_vtysh_command(command)

    def configure_ospf(self, pid, area_id=None, network=None, wildcard_mask=None, cost=None, priority=None, 
                       transmit_delay=None, retransmit_interval=None, hello_interval=None, dead_interval=None, 
                       auth_key=None, auth_key_id=None, auth_type=None, auth_key_encrypt=None, 
                       auth_key_encrypt_id=None, auth_key_encrypt_type=None, auth_key_encrypt_type_id=None):
        
        command = f'configure terminal ; router ospf {pid}'
        
        if area_id:
            command += f' area {area_id}'
        
        if network:
            command += f' network {network}'
        
        if wildcard_mask:
            command += f' wildcard-mask {wildcard_mask}'
        
        if cost:
            command += f' cost {cost}'
        
        if priority:
            command += f' priority {priority}'
        
        if transmit_delay:
            command += f' transmit-delay {transmit_delay}'
        
        if retransmit_interval:
            command += f' retransmit-interval {retransmit_interval}'
        
        if hello_interval:
            command += f' hello-interval {hello_interval}'
        
        if dead_interval:
            command += f' dead-interval {dead_interval}'
        
        if auth_key:
            command += f' authentication-key {auth_key}'
        
        if auth_key_id:
            command += f' authentication-key-id {auth_key_id}'
        
        if auth_type:
            command += f' authentication-type {auth_type}'
        
        if auth_key_encrypt:
            command += f' authentication-key-encrypt {auth_key_encrypt}'
        
        if auth_key_encrypt_id:
            command += f' authentication-key-encrypt-id {auth_key_encrypt_id}'
        
        if auth_key_encrypt_type:
            command += f' authentication-key-encrypt-type {auth_key_encrypt_type}'
        
        if auth_key_encrypt_type_id:
            command += f' authentication-key-encrypt-type-id {auth_key_encrypt_type_id}'
        
        return self.run_vtysh_command(command)

  


















#   class FRRClientFiltering:
#     def __init__(self):
#         # Initialization as needed
#         pass
    
#     def run_vtysh_command(self, command):
#         # Placeholder for running VTYSH commands
#         return "Output from command execution", None

#     # OSPFv2 Configuration Commands
#     def router_ospf(self):
#         command = 'configure terminal ; router ospf'
#         return self.run_vtysh_command(command)

#     def router_ospf_with_pid(self, pid):
#         command = f'configure terminal ; router ospf {pid}'
#         return self.run_vtysh_command(command)

#     def router_ospf_with_pid_area(self, pid, area_id):
#         command = f'configure terminal ; router ospf {pid} area {area_id}'
#         return self.run_vtysh_command(command)

#     def router_ospf_with_pid_area_network(self, pid, area_id, network):
#         command = f'configure terminal ; router ospf {pid} area {area_id} network {network}'
#         return self.run_vtysh_command(command)

#     def router_ospf_with_pid_area_network_wildcard(self, pid, area_id, network, wildcard_mask):
#         command = f'configure terminal ; router ospf {pid} area {area_id} network {network} wildcard-mask {wildcard_mask}'
#         return self.run_vtysh_command(command)

#     def router_ospf_with_pid_area_network_wildcard_cost(self, pid, area_id, network, wildcard_mask, cost):
#         command = f'configure terminal ; router ospf {pid} area {area_id} network {network} wildcard-mask {wildcard_mask} cost {cost}'
#         return self.run_vtysh_command(command)

#     def router_ospf_with_pid_area_network_wildcard_cost_priority(self, pid, area_id, network, wildcard_mask, cost, priority):
#         command = f'configure terminal ; router ospf {pid} area {area_id} network {network} wildcard-mask {wildcard_mask} cost {cost} priority {priority}'
#         return self.run_vtysh_command(command)

#     def router_ospf_with_pid_area_network_wildcard_cost_priority_transmit_delay(self, pid, area_id, network, wildcard_mask, cost, priority, transmit_delay):
#         command = f'configure terminal ; router ospf {pid} area {area_id} network {network} wildcard-mask {wildcard_mask} cost {cost} priority {priority} transmit-delay {transmit_delay}'
#         return self.run_vtysh_command(command)

#     def router_ospf_with_pid_area_network_wildcard_cost_priority_transmit_delay_retransmit_interval(self, pid, area_id, network, wildcard_mask, cost, priority, transmit_delay, retransmit_interval):
#         command = f'configure terminal ; router ospf {pid} area {area_id} network {network} wildcard-mask {wildcard_mask} cost {cost} priority {priority} transmit-delay {transmit_delay} retransmit-interval {retransmit_interval}'
#         return self.run_vtysh_command(command)

#     def router_ospf_with_pid_area_network_wildcard_cost_priority_transmit_delay_retransmit_interval_hello_interval(self, pid, area_id, network, wildcard_mask, cost, priority, transmit_delay, retransmit_interval, hello_interval):
#         command = f'configure terminal ; router ospf {pid} area {area_id} network {network} wildcard-mask {wildcard_mask} cost {cost} priority {priority} transmit-delay {transmit_delay} retransmit-interval {retransmit_interval} hello-interval {hello_interval}'
#         return self.run_vtysh_command(command)

#     def router_ospf_with_pid_area_network_wildcard_cost_priority_transmit_delay_retransmit_interval_hello_interval_dead_interval(self, pid, area_id, network, wildcard_mask, cost, priority, transmit_delay, retransmit_interval, hello_interval, dead_interval):
#         command = f'configure terminal ; router ospf {pid} area {area_id} network {network} wildcard-mask {wildcard_mask} cost {cost} priority {priority} transmit-delay {transmit_delay} retransmit-interval {retransmit_interval} hello-interval {hello_interval} dead-interval {dead_interval}'
#         return self.run_vtysh_command(command)

#     def router_ospf_with_pid_area_network_wildcard_cost_priority_transmit_delay_retransmit_interval_hello_interval_dead_interval_auth_key(self, pid, area_id, network, wildcard_mask, cost, priority, transmit_delay, retransmit_interval, hello_interval, dead_interval, auth_key):
#         command = f'configure terminal ; router ospf {pid} area {area_id} network {network} wildcard-mask {wildcard_mask} cost {cost} priority {priority} transmit-delay {transmit_delay} retransmit-interval {retransmit_interval} hello-interval {hello_interval} dead-interval {dead_interval} authentication-key {auth_key}'
#         return self.run_vtysh_command(command)

#     def router_ospf_with_pid_area_network_wildcard_cost_priority_transmit_delay_retransmit_interval_hello_interval_dead_interval_auth_key_auth_key_id(self, pid, area_id, network, wildcard_mask, cost, priority, transmit_delay, retransmit_interval, hello_interval, dead_interval, auth_key, auth_key_id):
#         command = f'configure terminal ; router ospf {pid} area {area_id} network {network} wildcard-mask {wildcard_mask} cost {cost} priority {priority} transmit-delay {transmit_delay} retransmit-interval {retransmit_interval} hello-interval {hello_interval} dead-interval {dead_interval} authentication-key {auth_key} authentication-key-id {auth_key_id}'
#         return self.run_vtysh_command(command)

#     def router_ospf_with_pid_area_network_wildcard_cost_priority_transmit_delay_retransmit_interval_hello_interval_dead_interval_auth_key_auth_key_id_auth_type(self, pid, area_id, network, wildcard_mask, cost, priority, transmit_delay, retransmit_interval, hello_interval, dead_interval, auth_key, auth_key_id, auth_type):
#         command = f'configure terminal ; router ospf {pid} area {area_id} network {network} wildcard-mask {wildcard_mask} cost {cost} priority {priority} transmit-delay {transmit_delay} retransmit-interval {retransmit_interval} hello-interval {hello_interval} dead-interval {dead_interval} authentication-key {auth_key} authentication-key-id {auth_key_id} authentication-type {auth_type}'
#         return self.run_vtysh_command(command)

#     def router_ospf_with_pid_area_network_wildcard_cost_priority_transmit_delay_retransmit_interval_hello_interval_dead_interval_auth_key_auth_key_id_auth_type_auth_key_encrypt(self, pid, area_id, network, wildcard_mask, cost, priority, transmit_delay, retransmit_interval, hello_interval, dead_interval, auth_key, auth_key_id, auth_type, auth_key_encrypt):
#         command = f'configure terminal ; router ospf {pid} area {area_id} network {network} wildcard-mask {wildcard_mask} cost {cost} priority {priority} transmit-delay {transmit_delay} retransmit-interval {retransmit_interval} hello-interval {hello_interval} dead-interval {dead_interval} authentication-key {auth_key} authentication-key-id {auth_key_id} authentication-type {auth_type} authentication-key-encrypt {auth_key_encrypt}'
#         return self.run_vtysh_command(command)

#     def router_ospf_with_pid_area_network_wildcard_cost_priority_transmit_delay_retransmit_interval_hello_interval_dead_interval_auth_key_auth_key_id_auth_type_auth_key_encrypt_auth_key_encrypt_id(self, pid, area_id, network, wildcard_mask, cost, priority, transmit_delay, retransmit_interval, hello_interval, dead_interval, auth_key, auth_key_id, auth_type, auth_key_encrypt, auth_key_encrypt_id):
#         command = f'configure terminal ; router ospf {pid} area {area_id} network {network} wildcard-mask {wildcard_mask} cost {cost} priority {priority} transmit-delay {transmit_delay} retransmit-interval {retransmit_interval} hello-interval {hello_interval} dead-interval {dead_interval} authentication-key {auth_key} authentication-key-id {auth_key_id} authentication-type {auth_type} authentication-key-encrypt {auth_key_encrypt} authentication-key-encrypt-id {auth_key_encrypt_id}'
#         return self.run_vtysh_command(command)

#     def router_ospf_with_pid_area_network_wildcard_cost_priority_transmit_delay_retransmit_interval_hello_interval_dead_interval_auth_key_auth_key_id_auth_type_auth_key_encrypt_auth_key_encrypt_id_auth_key_encrypt_type(self, pid, area_id, network, wildcard_mask, cost, priority, transmit_delay, retransmit_interval, hello_interval, dead_interval, auth_key, auth_key_id, auth_type, auth_key_encrypt, auth_key_encrypt_id, auth_key_encrypt_type):
#         command = f'configure terminal ; router ospf {pid} area {area_id} network {network} wildcard-mask {wildcard_mask} cost {cost} priority {priority} transmit-delay {transmit_delay} retransmit-interval {retransmit_interval} hello-interval {hello_interval} dead-interval {dead_interval} authentication-key {auth_key} authentication-key-id {auth_key_id} authentication-type {auth_type} authentication-key-encrypt {auth_key_encrypt} authentication-key-encrypt-id {auth_key_encrypt_id} authentication-key-encrypt-type {auth_key_encrypt_type}'
#         return self.run_vtysh_command(command)

#     def router_ospf_with_pid_area_network_wildcard_cost_priority_transmit_delay_retransmit_interval_hello_interval_dead_interval_auth_key_auth_key_id_auth_type_auth_key_encrypt_auth_key_encrypt_id_auth_key_encrypt_type_auth_key_encrypt_type_id(self, pid, area_id, network, wildcard_mask, cost, priority, transmit_delay, retransmit_interval, hello_interval, dead_interval, auth_key, auth_key_id, auth_type, auth_key_encrypt, auth_key_encrypt_id, auth_key_encrypt_type, auth_key_encrypt_type_id):
#         command = f'configure terminal ; router ospf {pid} area {area_id} network {network} wildcard-mask {wildcard_mask} cost {cost} priority {priority} transmit-delay {transmit_delay} retransmit-interval {retransmit_interval} hello-interval {hello_interval} dead-interval {dead_interval} authentication-key {auth_key} authentication-key-id {auth_key_id} authentication-type {auth_type} authentication-key-encrypt {auth_key_encrypt} authentication-key-encrypt-id {auth_key_encrypt_id} authentication-key-encrypt-type {auth_key_encrypt_type} authentication-key-encrypt-type-id {auth_key_encrypt_type_id}'
#         return self.run_vtysh_command(command)

#     # Additional OSPF commands can be added here as needed
