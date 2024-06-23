from flask import Flask, request, jsonify
from flask_restx import Api, Resource

from frr.frr_client_routing import FRRClientRouting
from frr.frr_client_system import FRRClientSystem
import logging
from frr.frr_client_filtering import FRRClientFiltering
from frr.frr_client_routemap import FRRClientRouteMap
from frr.frr_client_ospf import FRRClientOSPF

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
api = Api(app)

frr_client_routing = FRRClientRouting()
frr_client_system = FRRClientSystem()
frr_client_filtering = FRRClientFiltering()
frr_client_routemap = FRRClientRouteMap()
frr_client_ospf = FRRClientOSPF()

class ExecuteCommand(Resource):
    def post(self):
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

class BGPNeighbors(Resource):
    def get(self):
        try:
            stdout, stderr = frr_client_routing.get_bgp_neighbors()
            if stderr:
                return jsonify({'error': stderr}), 400
            return jsonify({'output': stdout})
        except Exception as e:
            logging.exception(f"Error retrieving BGP neighbors: {e}")
            return jsonify({'error': str(e)}), 500

class AddBGPNeighbor(Resource):
    def post(self):
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

class RemoveBGPNeighbor(Resource):
    def delete(self):
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

class OSPFNeighbors(Resource):
    def get(self):
        try:
            stdout, stderr = frr_client_routing.get_ospf_neighbors()
            if stderr:
                return jsonify({'error': stderr}), 400
            return jsonify({'output': stdout})
        except Exception as e:
            logging.exception(f"Error retrieving OSPF neighbors: {e}")
            return jsonify({'error': str(e)}), 500

class AddOSPFNetwork(Resource):
    def post(self):
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

class RemoveOSPFNetwork(Resource):
    def delete(self):
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

class Version(Resource):
    def get(self):
        try:
            stdout, stderr = frr_client_routing.get_version()
            if stderr:
                return jsonify({'error': stderr}), 400
            return jsonify({'output': stdout})
        except Exception as e:
            logging.exception(f"Error retrieving version: {e}")
            return jsonify({'error': str(e)}), 500

class Interfaces(Resource):
    def get(self):
        try:
            stdout, stderr = frr_client_system.get_interfaces()
            if stderr:
                return jsonify({'error': stderr}), 400
            return jsonify({'output': stdout})
        except Exception as e:
            logging.exception(f"Error retrieving interfaces: {e}")
            return jsonify({'error': str(e)}), 500

class AddStaticRoute(Resource):
    def post(self):
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

class RemoveStaticRoute(Resource):
    def delete(self):
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

class CreateAccessList(Resource):
    def post(self):
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

class GetAccessLists(Resource):
    def get(self):
        try:
            json_output = 'json' in request.args
            stdout, stderr = frr_client_filtering.show_access_lists(json_output=json_output)
            if stderr:
                return jsonify({'error': stderr}), 400
            return jsonify({'output': stdout})
        except Exception as e:
            logging.exception(f"Error retrieving access lists: {e}")
            return jsonify({'error': str(e)}), 500

class CreateRouteMapEntry(Resource):
    def post(self):
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

class AddRouteMapMatch(Resource):
    def post(self, name):
        try:
            data = request.get_json()
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

class ConfigureOSPF(Resource):
    def post(self):
        try:
            data = request.get_json()
            router_id = data.get('router_id')
            if not router_id:
                raise ValueError("router_id is required")
            stdout, stderr = frr_client_ospf.configure_ospf(router_id)
            if stderr:
                return jsonify({'error': stderr}), 400
            return jsonify({'output': stdout})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

class AddOSPFNetwork(Resource):
    def post(self):
        try:
            data = request.get_json()
            network = data.get('network')
            area = data.get('area')
            if not network or not area:
                raise ValueError("network and area are required")
            stdout, stderr = frr_client_ospf.add_network(network, area)
            if stderr:
                return jsonify({'error': stderr}), 400
            return jsonify({'output': stdout})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

class SetOSPFInterfaceCost(Resource):
    def post(self):
        try:
            data = request.get_json()
            interface = data.get('interface')
            cost = data.get('cost')
            if not interface or not cost:
                raise ValueError("interface and cost are required")
            stdout, stderr = frr_client_ospf.set_interface_cost(interface, cost)
            if stderr:
                return jsonify({'error': stderr}), 400
            return jsonify({'output': stdout})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

# Add resources to API
api.add_resource(ExecuteCommand, '/api/system/execute_command')
api.add_resource(BGPNeighbors, '/api/routing/bgp_neighbors')
api.add_resource(AddBGPNeighbor, '/api/routing/add_bgp_neighbor')
api.add_resource(RemoveBGPNeighbor, '/api/routing/remove_bgp_neighbor')
api.add_resource(OSPFNeighbors, '/api/routing/ospf_neighbors')
api.add_resource(AddOSPFNetwork, '/api/routing/add_ospf_network')
api.add_resource(RemoveOSPFNetwork, '/api/routing/remove_ospf_network')
api.add_resource(Version, '/api/routing/version')
api.add_resource(Interfaces, '/api/system/interfaces')
api.add_resource(AddStaticRoute, '/api/routing/add_static_route')
api.add_resource(RemoveStaticRoute, '/api/routing/remove_static_route')
api.add_resource(CreateAccessList, '/api/filtering/create_access_list')
api.add_resource(GetAccessLists, '/api/filtering/access_lists')
api.add_resource(CreateRouteMapEntry, '/api/routemap/create_route_map_entry')
api.add_resource(AddRouteMapMatch, '/api/routemap/<name>/add_route_map_match')
api.add_resource(ConfigureOSPF, '/api/ospf/configure')
api.add_resource(AddOSPFNetwork, '/api/ospf/add_network')
api.add_resource(SetOSPFInterfaceCost, '/api/ospf/set_interface_cost')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
