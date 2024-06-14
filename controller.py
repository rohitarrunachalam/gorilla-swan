from flask import Flask, request, jsonify
from frr.frr_client_routing import FRRClientRouting
from frr.frr_client_system import FRRClientSystem
import logging
from  frr.frr_client_filtering import FRRClientFiltering
from  frr.frr_client_routemap import FRRClientRouteMap
from  frr.frr_client_ospf import FRRClientOSPF


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
frr_client_routing = FRRClientRouting()
frr_client_system  = FRRClientSystem()
frr_client_filtering = FRRClientFiltering()
frr_client_routemap = FRRClientRouteMap()
frr_client_ospf = FRRClientOSPF()



@app.route('/execute', methods=['POST'])
def execute_command():
    try:
        data = request.get_json()
        command = data.get('command')
        if not command:
            raise ValueError("Command is required")
        stdout, stderr = frr_client_system.execute_command(command)
        if stderr:
            return jsonify({'error': stderr}), 400
        return jsonify({'output': stdout})
    except Exception as e:
        logging.exception(f"Error executing command: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/bgp/neighbors', methods=['GET'])
def get_bgp_neighbors():
    try:
        stdout, stderr = frr_client_routing.get_bgp_neighbors()
        if stderr:
            return jsonify({'error': stderr}), 400
        return jsonify({'output': stdout})
    except Exception as e:
        logging.exception(f"Error retrieving BGP neighbors: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/bgp/neighbor', methods=['POST'])
def add_bgp_neighbor():
    try:
        data = request.get_json()
        neighbor_address = data.get('neighbor_address')
        peer_as = data.get('peer_as')
        if not neighbor_address or not peer_as:
            raise ValueError("neighbor_address and peer_as are required")
        stdout, stderr = frr_client_routing.add_bgp_neighbor(64512, neighbor_address, peer_as)
        if stderr:
            return jsonify({'error': stderr}), 400
        return jsonify({'output': stdout})
    except Exception as e:
        logging.exception(f"Error adding BGP neighbor: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/bgp/neighbor', methods=['DELETE'])
def remove_bgp_neighbor():
    try:
        data = request.get_json()
        neighbor_address = data.get('neighbor_address')
        if not neighbor_address:
            raise ValueError("neighbor_address is required")
        stdout, stderr = frr_client_routing.remove_bgp_neighbor(64512, neighbor_address)
        if stderr:
            return jsonify({'error': stderr}), 400
        return jsonify({'output': stdout})
    except Exception as e:
        logging.exception(f"Error removing BGP neighbor: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/ospf/neighbors', methods=['GET'])
def get_ospf_neighbors():
    try:
        stdout, stderr = frr_client_routing.get_ospf_neighbors()
        if stderr:
            return jsonify({'error': stderr}), 400
        return jsonify({'output': stdout})
    except Exception as e:
        logging.exception(f"Error retrieving OSPF neighbors: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/ospf/network', methods=['POST'])
def add_ospf_network():
    try:
        data = request.get_json()
        network = data.get('network')
        area = data.get('area')
        if not network or not area:
            raise ValueError("network and area are required")
        stdout, stderr = frr_client_routing.add_ospf_network(network, area)
        if stderr:
            return jsonify({'error': stderr}), 400
        return jsonify({'output': stdout})
    except Exception as e:
        logging.exception(f"Error adding OSPF network: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/ospf/network', methods=['DELETE'])
def remove_ospf_network():
    try:
        data = request.get_json()
        network = data.get('network')
        if not network:
            raise ValueError("network is required")
        stdout, stderr = frr_client_routing.remove_ospf_network(network)
        if stderr:
            return jsonify({'error': stderr}), 400
        return jsonify({'output': stdout})
    except Exception as e:
        logging.exception(f"Error removing OSPF network: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/version', methods=['GET'])
def get_version():
    try:
        stdout, stderr = frr_client_routing.get_version()
        if stderr:
            return jsonify({'error': stderr}), 400
        return jsonify({'output': stdout})
    except Exception as e:
        logging.exception(f"Error retrieving version: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/interfaces', methods=['GET'])
def get_interfaces():
    try:
        stdout, stderr = frr_client_system.get_interfaces()
        if stderr:
            return jsonify({'error': stderr}), 400
        return jsonify({'output': stdout})
    except Exception as e:
        logging.exception(f"Error retrieving interfaces: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/static_route', methods=['POST'])
def add_static_route():
    try:
        data = request.get_json()
        destination = data.get('destination')
        gateway = data.get('gateway')
        if not destination or not gateway:
            raise ValueError("destination and gateway are required")
        stdout, stderr = frr_client_routing.add_static_route(destination, gateway)
        if stderr:
            return jsonify({'error': stderr}), 400
        return jsonify({'output': stdout})
    except Exception as e:
        logging.exception(f"Error adding static route: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/static_route', methods=['DELETE'])
def remove_static_route():
    try:
        data = request.get_json()
        destination = data.get('destination')
        if not destination:
            raise ValueError("destination is required")
        stdout, stderr = frr_client_routing.remove_static_route(destination)
        if stderr:
            return jsonify({'error': stderr}), 400
        return jsonify({'output': stdout})
    except Exception as e:
        logging.exception(f"Error removing static route: {e}")
        return jsonify({'error': str(e)}), 500
    



# Filtering

@app.route('/access-lists', methods=['POST'])
def create_access_list():
    try:
        data = request.get_json()
        name = data.get('name')
        seq = data.get('seq')
        action = data.get('action')
        network = data.get('network')

        if not name or not action or not network:
            raise ValueError("name, action, and network are required")

        stdout, stderr = frr_client_filtering.create_access_list(name, seq, action, network)
        if stderr:
            return jsonify({'error': stderr}), 400
        return jsonify({'output': stdout})
    except Exception as e:
        logging.exception(f"Error creating access list: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/access-lists', methods=['GET'])
def get_access_lists():
    try:
        json_output = 'json' in request.args  # Check if JSON output is requested
        stdout, stderr = frr_client_filtering.show_access_lists(json_output=json_output)
        if stderr:
            return jsonify({'error': stderr}), 400
        return jsonify({'output': stdout})
    except Exception as e:
        logging.exception(f"Error retrieving access lists: {e}")
        return jsonify({'error': str(e)}), 500





# Route Maps

@app.route('/route-maps', methods=['POST'])
def create_route_map_entry():
    try:
        data = request.get_json()
        name = data.get('name')
        action = data.get('action')
        order = data.get('order')

        if not name or not action or not order:
            raise ValueError("name, action, and order are required")

        stdout, stderr = frr_client_routemap.create_route_map_entry(name, action, order)
        if stderr:
            return jsonify({'error': stderr}), 400
        return jsonify({'output': stdout})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/route-maps/<name>/matches', methods=['POST'])
def add_route_map_match():
    try:
        data = request.get_json()
        name = data.get('name')
        match_type = data.get('match_type')
        match_value = data.get('match_value')

        if not match_type or not match_value:
            raise ValueError("match_type and match_value are required")

        stdout, stderr = frr_client_routemap.add_route_map_match(name, match_type, match_value)
        if stderr:
            return jsonify({'error': stderr}), 400
        return jsonify({'output': stdout})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    







#OSPF V2


@app.route('/ospf', methods=['POST'])
def configure_ospf():
    try:
        data = request.get_json()
        pid = data.get('pid')
        area_id = data.get('area_id')
        network = data.get('network')
        wildcard_mask = data.get('wildcard_mask')
        cost = data.get('cost')
        priority = data.get('priority')
        transmit_delay = data.get('transmit_delay')
        retransmit_interval = data.get('retransmit_interval')
        hello_interval = data.get('hello_interval')
        dead_interval = data.get('dead_interval')
        auth_key = data.get('auth_key')
        auth_key_id = data.get('auth_key_id')
        auth_type = data.get('auth_type')
        auth_key_encrypt = data.get('auth_key_encrypt')
        auth_key_encrypt_id = data.get('auth_key_encrypt_id')
        auth_key_encrypt_type = data.get('auth_key_encrypt_type')
        auth_key_encrypt_type_id = data.get('auth_key_encrypt_type_id')
        
        if not pid:
            raise ValueError("pid is required")

        stdout, stderr = frr_client_ospf.configure_ospf(
            pid, area_id, network, wildcard_mask, cost, priority, transmit_delay, 
            retransmit_interval, hello_interval, dead_interval, auth_key, auth_key_id, 
            auth_type, auth_key_encrypt, auth_key_encrypt_id, auth_key_encrypt_type, auth_key_encrypt_type_id
        )
        



        # if not pid:
        #     raise ValueError("pid is required")

        # if area_id and network and wildcard_mask and cost and priority and transmit_delay and retransmit_interval and hello_interval and dead_interval and auth_key and auth_key_id and auth_type and auth_key_encrypt and auth_key_encrypt_id and auth_key_encrypt_type and auth_key_encrypt_type_id:
        #     stdout, stderr = frr_client_filtering.router_ospf_with_pid_area_network_wildcard_cost_priority_transmit_delay_retransmit_interval_hello_interval_dead_interval_auth_key_auth_key_id_auth_type_auth_key_encrypt_auth_key_encrypt_id_auth_key_encrypt_type_auth_key_encrypt_type_id(
        #         pid, area_id, network, wildcard_mask, cost, priority, transmit_delay, retransmit_interval, hello_interval, dead_interval, auth_key, auth_key_id, auth_type, auth_key_encrypt, auth_key_encrypt_id, auth_key_encrypt_type, auth_key_encrypt_type_id)
        # elif area_id and network and wildcard_mask and cost and priority and transmit_delay and retransmit_interval and hello_interval and dead_interval and auth_key and auth_key_id and auth_type and auth_key_encrypt and auth_key_encrypt_id and auth_key_encrypt_type:
        #     stdout, stderr = frr_client_filtering.router_ospf_with_pid_area_network_wildcard_cost_priority_transmit_delay_retransmit_interval_hello_interval_dead_interval_auth_key_auth_key_id_auth_type_auth_key_encrypt_auth_key_encrypt_id_auth_key_encrypt_type(
        #         pid, area_id, network, wildcard_mask, cost, priority, transmit_delay, retransmit_interval, hello_interval, dead_interval, auth_key, auth_key_id, auth_type, auth_key_encrypt, auth_key_encrypt_id, auth_key_encrypt_type)
        # elif area_id and network and wildcard_mask and cost and priority and transmit_delay and retransmit_interval and hello_interval and dead_interval and auth_key and auth_key_id and auth_type and auth_key_encrypt and auth_key_encrypt_id:
        #     stdout, stderr = frr_client_filtering.router_ospf_with_pid_area_network_wildcard_cost_priority_transmit_delay_retransmit_interval_hello_interval_dead_interval_auth_key_auth_key_id_auth_type_auth_key_encrypt_auth_key_encrypt_id(
        #         pid, area_id, network, wildcard_mask, cost, priority, transmit_delay, retransmit_interval, hello_interval, dead_interval, auth_key, auth_key_id, auth_type, auth_key_encrypt, auth_key_encrypt_id)
        # elif area_id and network and wildcard_mask and cost and priority and transmit_delay and retransmit_interval and hello_interval and dead_interval and auth_key and auth_key_id and auth_type and auth_key_encrypt:
        #     stdout, stderr = frr_client_filtering.router_ospf_with_pid_area_network_wildcard_cost_priority_transmit_delay_retransmit_interval_hello_interval_dead_interval_auth_key_auth_key_id_auth_type_auth_key_encrypt(
        #         pid, area_id, network, wildcard_mask, cost, priority, transmit_delay, retransmit_interval, hello_interval, dead_interval, auth_key, auth_key_id, auth_type, auth_key_encrypt)
        # elif area_id and network and wildcard_mask and cost and priority and transmit_delay and retransmit_interval and hello_interval and dead_interval and auth_key and auth_key_id and auth_type:
        #     stdout, stderr = frr_client_filtering.router_ospf_with_pid_area_network_wildcard_cost_priority_transmit_delay_retransmit_interval_hello_interval_dead_interval_auth_key_auth_key_id_auth_type(
        #         pid, area_id, network, wildcard_mask, cost, priority, transmit_delay, retransmit_interval, hello_interval, dead_interval, auth_key, auth_key_id, auth_type)
        # elif area_id and network and wildcard_mask and cost and priority and transmit_delay and retransmit_interval and hello_interval and dead_interval and auth_key and auth_key_id:
        #     stdout, stderr = frr_client_filtering.router_ospf_with_pid_area_network_wildcard_cost_priority_transmit_delay_retransmit_interval_hello_interval_dead_interval_auth_key_auth_key_id(
        #         pid, area_id, network, wildcard_mask, cost, priority, transmit_delay, retransmit_interval, hello_interval, dead_interval, auth_key, auth_key_id)
        # elif area_id and network and wildcard_mask and cost and priority and transmit_delay and retransmit_interval and hello_interval and dead_interval and auth_key:
        #     stdout, stderr = frr_client_filtering.router_ospf_with_pid_area_network_wildcard_cost_priority_transmit_delay_retransmit_interval_hello_interval_dead_interval_auth_key(
        #         pid, area_id, network, wildcard_mask, cost, priority, transmit_delay, retransmit_interval, hello_interval, dead_interval, auth_key)
        # elif area_id and network and wildcard_mask and cost and priority and transmit_delay and retransmit_interval and hello_interval and dead_interval:
        #     stdout, stderr = frr_client_filtering.router_ospf_with_pid_area_network_wildcard_cost_priority_transmit_delay_retransmit_interval_hello_interval_dead_interval(
        #         pid, area_id, network, wildcard_mask, cost, priority, transmit_delay, retransmit_interval, hello_interval, dead_interval)
        # elif area_id and network and wildcard_mask and cost and priority and transmit_delay and retransmit_interval and hello_interval:
        #     stdout, stderr = frr_client_filtering.router_ospf_with_pid_area_network_wildcard_cost_priority_transmit_delay_retransmit_interval_hello_interval(
        #         pid, area_id, network, wildcard_mask, cost, priority, transmit_delay, retransmit_interval, hello_interval)
        # elif area_id and network and wildcard_mask and cost and priority and transmit_delay and retransmit_interval:
        #     stdout, stderr = frr_client_filtering.router_ospf_with_pid_area_network_wildcard_cost_priority_transmit_delay_retransmit_interval(
        #         pid, area_id, network, wildcard_mask, cost, priority, transmit_delay, retransmit_interval)
        # elif area_id and network and wildcard_mask and cost and priority and transmit_delay:
        #     stdout, stderr = frr_client_filtering.router_ospf_with_pid_area_network_wildcard_cost_priority_transmit_delay(
        #         pid, area_id, network, wildcard_mask, cost, priority, transmit_delay)
        # elif area_id and network and wildcard_mask and cost and priority:
        #     stdout, stderr = frr_client_filtering.router_ospf_with_pid_area_network_wildcard_cost_priority(
        #         pid, area_id, network, wildcard_mask, cost, priority)
        # elif area_id and network and wildcard_mask and cost:
        #     stdout, stderr = frr_client_filtering.router_ospf_with_pid_area_network_wildcard_cost(
        #         pid, area_id, network, wildcard_mask, cost)
        # elif area_id and network and wildcard_mask:
        #     stdout, stderr = frr_client_filtering.router_ospf_with_pid_area_network_wildcard(
        #         pid, area_id, network, wildcard_mask)
        # elif area_id and network:
        #     stdout, stderr = frr_client_filtering.router_ospf_with_pid_area_network(
        #         pid, area_id, network)
        # elif area_id:
        #     stdout, stderr = frr_client_filtering.router_ospf_with_pid_area(
        #         pid, area_id)
        # else:
        #     stdout, stderr = frr_client_filtering.router_ospf_with_pid(
        #         pid)
            
        if stderr:
            return jsonify({'error': stderr}), 400
        return jsonify({'output': stdout})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
