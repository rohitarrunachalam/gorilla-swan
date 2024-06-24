# from flask import Flask, request, jsonify
# from frr.frr_client_routing import FRRClientRouting
# from frr.frr_client_system import FRRClientSystem
# from frr.frr_client_filtering import FRRClientFiltering
# from frr.frr_client_routemap import FRRClientRouteMap
# import logging

# # Configure logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# app = Flask(__name__)
# frr_client_routing = FRRClientRouting()
# frr_client_system = FRRClientSystem()
# frr_client_filtering = FRRClientFiltering()
# frr_client_routemap = FRRClientRouteMap()

# @app.route('/execute', methods=['POST'])
# def execute_command():
#     try:
#         data = request.get_json()
#         command = data.get('command')
#         if not command:
#             raise ValueError("Command is required")
#         stdout, stderr = frr_client_system.execute_command(command)
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error executing command: {e}")
#         return jsonify({'error': str(e)}), 500

# # BGP Endpoints
# @app.route('/bgp/neighbors', methods=['GET'])
# def get_bgp_neighbors():
#     try:
#         stdout, stderr = frr_client_routing.get_bgp_neighbors()
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error retrieving BGP neighbors: {e}")
#         return jsonify({'error': str(e)}), 500

# @app.route('/bgp/neighbor', methods=['POST'])
# def add_bgp_neighbor():
#     try:
#         data = request.get_json()
#         neighbor_address = data.get('neighbor_address')
#         peer_as = data.get('peer_as')
#         if not neighbor_address or not peer_as:
#             raise ValueError("neighbor_address and peer_as are required")
#         stdout, stderr = frr_client_routing.add_bgp_neighbor(64512, neighbor_address, peer_as)
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error adding BGP neighbor: {e}")
#         return jsonify({'error': str(e)}), 500

# @app.route('/bgp/neighbor', methods=['DELETE'])
# def remove_bgp_neighbor():
#     try:
#         data = request.get_json()
#         neighbor_address = data.get('neighbor_address')
#         if not neighbor_address:
#             raise ValueError("neighbor_address is required")
#         stdout, stderr = frr_client_routing.remove_bgp_neighbor(64512, neighbor_address)
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error removing BGP neighbor: {e}")
#         return jsonify({'error': str(e)}), 500

# # OSPF Endpoints
# @app.route('/ospf/neighbors', methods=['GET'])
# def get_ospf_neighbors():
#     try:
#         stdout, stderr = frr_client_routing.get_ospf_neighbors()
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error retrieving OSPF neighbors: {e}")
#         return jsonify({'error': str(e)}), 500

# @app.route('/ospf/network', methods=['POST'])
# def add_ospf_network():
#     try:
#         data = request.get_json()
#         network = data.get('network')
#         area = data.get('area')
#         if not network or not area:
#             raise ValueError("network and area are required")
#         stdout, stderr = frr_client_routing.add_ospf_network(network, area)
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error adding OSPF network: {e}")
#         return jsonify({'error': str(e)}), 500

# @app.route('/ospf/network', methods=['DELETE'])
# def remove_ospf_network():
#     try:
#         data = request.get_json()
#         network = data.get('network')
#         if not network:
#             raise ValueError("network is required")
#         stdout, stderr = frr_client_routing.remove_ospf_network(network)
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error removing OSPF network: {e}")
#         return jsonify({'error': str(e)}), 500

# # Filtering Endpoints
# @app.route('/filter/access_list', methods=['POST'])
# def add_access_list():
#     try:
#         data = request.get_json()
#         name = data.get('name')
#         action = data.get('action')
#         network = data.get('network')
#         seq = data.get('seq')
#         if not name or not action or not network:
#             raise ValueError("name, action, and network are required")
#         stdout, stderr = frr_client_filtering.add_access_list(name, action, network, seq)
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error adding access list: {e}")
#         return jsonify({'error': str(e)}), 500

# @app.route('/filter/access_list', methods=['DELETE'])
# def remove_access_list():
#     try:
#         data = request.get_json()
#         name = data.get('name')
#         seq = data.get('seq')
#         if not name or not seq:
#             raise ValueError("name and seq are required")
#         stdout, stderr = frr_client_filtering.remove_access_list(name, seq)
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error removing access list: {e}")
#         return jsonify({'error': str(e)}), 500

# @app.route('/filter/prefix_list', methods=['POST'])
# def add_prefix_list():
#     try:
#         data = request.get_json()
#         name = data.get('name')
#         action = data.get('action')
#         prefix = data.get('prefix')
#         seq = data.get('seq')
#         le = data.get('le')
#         ge = data.get('ge')
#         if not name or not action or not prefix:
#             raise ValueError("name, action, and prefix are required")
#         stdout, stderr = frr_client_filtering.add_prefix_list(name, action, prefix, seq, le, ge)
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error adding prefix list: {e}")
#         return jsonify({'error': str(e)}), 500

# @app.route('/filter/prefix_list', methods=['DELETE'])
# def remove_prefix_list():
#     try:
#         data = request.get_json()
#         name = data.get('name')
#         seq = data.get('seq')
#         if not name or not seq:
#             raise ValueError("name and seq are required")
#         stdout, stderr = frr_client_filtering.remove_prefix_list(name, seq)
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error removing prefix list: {e}")
#         return jsonify({'error': str(e)}), 500

# # Route Map Endpoints
# @app.route('/routemap', methods=['POST'])
# def add_route_map():
#     try:
#         data = request.get_json()
#         name = data.get('name')
#         action = data.get('action')
#         order = data.get('order')
#         if not name or not action or not order:
#             raise ValueError("name, action, and order are required")
#         stdout, stderr = frr_client_routemap.add_route_map(name, action, order)
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error adding route map: {e}")
#         return jsonify({'error': str(e)}), 500

# @app.route('/routemap', methods=['DELETE'])
# def remove_route_map():
#     try:
#         data = request.get_json()
#         name = data.get('name')
#         if not name:
#             raise ValueError("name is required")
#         stdout, stderr = frr_client_routemap.remove_route_map(name)
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error removing route map: {e}")
#         return jsonify({'error': str(e)}), 500

# # Additional system endpoints
# @app.route('/version', methods=['GET'])
# def get_version():
#     try:
#         stdout, stderr = frr_client_system.get_version()
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error retrieving version: {e}")
#         return jsonify({'error': str(e)}), 500

# @app.route('/interfaces', methods=['GET'])
# def get_interfaces():
#     try:
#         stdout, stderr = frr_client_system.get_interfaces()
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error retrieving interfaces: {e}")
#         return jsonify({'error': str(e)}), 500

# @app.route('/static_route', methods=['POST'])
# def add_static_route():
#     try:
#         data = request.get_json()
#         destination = data.get('destination')
#         gateway = data.get('gateway')
#         if not destination or not gateway:
#             raise ValueError("destination and gateway are required")
#         stdout, stderr = frr_client_routing.add_static_route(destination, gateway)
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error adding static route: {e}")
#         return jsonify({'error': str(e)}), 500

# @app.route('/static_route', methods=['DELETE'])
# def remove_static_route():
#     try:
#         data = request.get_json()
#         destination = data.get('destination')
#         if not destination:
#             raise ValueError("destination is required")
#         stdout, stderr = frr_client_routing.remove_static_route(destination)
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error removing static route: {e}")
#         return jsonify({'error': str(e)}), 500
    

# @app.route('/bgp/start', methods=['POST'])
# def start_bgp():
#     try:
#         data = request.get_json()
#         port = data.get('port')
#         listenon = data.get('listenon')
#         daemon = data.get('daemon')
#         config_file = data.get('config_file')
#         no_kernel = data.get('no_kernel')
#         stdout, stderr = frr_client_routing.start_bgp(port, listenon, daemon, config_file, no_kernel)
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error starting BGP: {e}")
#         return jsonify({'error': str(e)}), 500

# @app.route('/bgp/debug', methods=['POST'])
# def debug_bgp():
#     try:
#         data = request.get_json()
#         command = data.get('command')
#         if not command:
#             raise ValueError("command is required")
#         stdout, stderr = frr_client_routing.debug_bgp(command)
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error debugging BGP: {e}")
#         return jsonify({'error': str(e)}), 500

# @app.route('/bgp/dump', methods=['POST'])
# def dump_bgp():
#     try:
#         data = request.get_json()
#         command = data.get('command')
#         if not command:
#             raise ValueError("command is required")
#         stdout, stderr = frr_client_routing.dump_bgp(command)
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error dumping BGP: {e}")
#         return jsonify({'error': str(e)}), 500

# @app.route('/bgp/show', methods=['GET'])
# def show_bgp():
#     try:
#         command = request.args.get('command')
#         if not command:
#             raise ValueError("command is required")
#         stdout, stderr = frr_client_routing.show_bgp(command)
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error showing BGP information: {e}")
#         return jsonify({'error': str(e)}), 500

# @app.route('/bgp/dampening', methods=['GET'])
# def show_bgp_dampening():
#     try:
#         command = request.args.get('command')
#         if not command:
#             raise ValueError("command is required")
#         stdout, stderr = frr_client_routing.show_bgp_dampening(command)
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error showing BGP dampening information: {e}")
#         return jsonify({'error': str(e)}), 500

# @app.route('/bgp/segment_routing', methods=['GET'])
# def show_bgp_segment_routing():
#     try:
#         stdout, stderr = frr_client_routing.show_bgp_segment_routing()
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error showing BGP segment routing information: {e}")
#         return jsonify({'error': str(e)}), 500

# @app.route('/bgp/route_reflector', methods=['GET'])
# def show_bgp_route_reflector():
#     try:
#         stdout, stderr = frr_client_routing.show_bgp_route_reflector()
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error showing BGP route reflector information: {e}")
#         return jsonify({'error': str(e)}), 500

# @app.route('/bgp/statistics', methods=['GET'])
# def show_bgp_statistics():
#     try:
#         stdout, stderr = frr_client_routing.show_bgp_statistics()
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error showing BGP statistics: {e}")
#         return jsonify({'error': str(e)}), 500

# @app.route('/bgp/cidr_only', methods=['GET'])
# def show_bgp_cidr_only():
#     try:
#         stdout, stderr = frr_client_routing.show_bgp_cidr_only()
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error showing BGP CIDR-only routes: {e}")
#         return jsonify({'error': str(e)}), 500

# @app.route('/bgp/neighbor_routes', methods=['GET'])
# def show_bgp_neighbor_routes():
#     try:
#         command = request.args.get('command')
#         if not command:
#             raise ValueError("command is required")
#         stdout, stderr = frr_client_routing.show_bgp_neighbor_routes(command)
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error showing BGP neighbor routes: {e}")
#         return jsonify({'error': str(e)}), 500
    
# # OSPFv2 Commands

# @app.route('/ospf/start', methods=['POST'])
# def start_ospf():
#     try:
#         data = request.get_json()
#         instance = data.get('instance')
#         vrf = data.get('vrf')
#         stdout, stderr = frr_client_routing.start_ospf(instance, vrf)
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error starting OSPF: {e}")
#         return jsonify({'error': str(e)}), 500

# @app.route('/ospf/router_id', methods=['POST'])
# def set_ospf_router_id():
#     try:
#         data = request.get_json()
#         router_id = data.get('router_id')
#         stdout, stderr = frr_client_routing.set_ospf_router_id(router_id)
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error setting OSPF router ID: {e}")
#         return jsonify({'error': str(e)}), 500

# @app.route('/ospf/debug', methods=['POST'])
# def debug_ospf():
#     try:
#         data = request.get_json()
#         command = data.get('command')
#         if not command:
#             raise ValueError("command is required")
#         stdout, stderr = frr_client_routing.debug_ospf(command)
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error debugging OSPF: {e}")
#         return jsonify({'error': str(e)}), 500

# @app.route('/ospf/show', methods=['GET'])
# def show_ospf():
#     try:
#         command = request.args.get('command')
#         if not command:
#             raise ValueError("command is required")
#         stdout, stderr = frr_client_routing.show_ospf(command)
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error showing OSPF information: {e}")
#         return jsonify({'error': str(e)}), 500

# @app.route('/ospf/clear', methods=['POST'])
# def clear_ospf():
#     try:
#         data = request.get_json()
#         command = data.get('command')
#         if not command:
#             raise ValueError("command is required")
#         stdout, stderr = frr_client_routing.clear_ospf(command)
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error clearing OSPF: {e}")
#         return jsonify({'error': str(e)}), 500

# # OSPFv3 Commands

# @app.route('/ospfv3/start', methods=['POST'])
# def start_ospfv3():
#     try:
#         stdout, stderr = frr_client_routing.start_ospfv3()
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error starting OSPFv3: {e}")
#         return jsonify({'error': str(e)}), 500

# @app.route('/ospfv3/router_id', methods=['POST'])
# def set_ospfv3_router_id():
#     try:
#         data = request.get_json()
#         router_id = data.get('router_id')
#         stdout, stderr = frr_client_routing.set_ospfv3_router_id(router_id)
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error setting OSPFv3 router ID: {e}")
#         return jsonify({'error': str(e)}), 500

# @app.route('/ospfv3/debug', methods=['POST'])
# def debug_ospfv3():
#     try:
#         data = request.get_json()
#         command = data.get('command')
#         if not command:
#             raise ValueError("command is required")
#         stdout, stderr = frr_client_routing.debug_ospfv3(command)
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error debugging OSPFv3: {e}")
#         return jsonify({'error': str(e)}), 500

# @app.route('/ospfv3/show', methods=['GET'])
# def show_ospfv3():
#     try:
#         command = request.args.get('command')
#         if not command:
#             raise ValueError("command is required")
#         stdout, stderr = frr_client_routing.show_ospfv3(command)
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error showing OSPFv3 information: {e}")
#         return jsonify({'error': str(e)}), 500

# @app.route('/ospfv3/clear', methods=['POST'])
# def clear_ospfv3():
#     try:
#         data = request.get_json()
#         command = data.get('command')
#         if not command:
#             raise ValueError("command is required")
#         stdout, stderr = frr_client_routing.clear_ospfv3(command)
#         if stderr:
#             return jsonify({'error': stderr}), 400
#         return jsonify({'output': stdout})
#     except Exception as e:
#         logging.exception(f"Error clearing OSPFv3: {e}")
#         return jsonify({'error': str(e)}), 500



# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)


from flask import Flask, request
from flask_restx import Api, Resource, fields
from frr.frr_client_routing import FRRClientRouting
from frr.frr_client_system import FRRClientSystem
from frr.frr_client_filtering import FRRClientFiltering
from frr.frr_client_routemap import FRRClientRouteMap
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
api = Api(app, version='1.0', title='FRR API', description='API for managing FRR configurations')

frr_client_routing = FRRClientRouting()
frr_client_system = FRRClientSystem()
frr_client_filtering = FRRClientFiltering()
frr_client_routemap = FRRClientRouteMap()

# Define namespaces
ns_system = api.namespace('system', description='System operations')
ns_bgp = api.namespace('bgp', description='BGP operations')
ns_ospf = api.namespace('ospf', description='OSPF operations')
ns_ospfv3 = api.namespace('ospfv3', description='OSPFv3 operations')
ns_filter = api.namespace('filter', description='Filtering operations')
ns_routemap = api.namespace('routemap', description='Route map operations')

# Models for request validation
command_model = api.model('Command', {
    'command': fields.String(required=True, description='The command to execute')
})

bgp_neighbor_model = api.model('BGPLocalNeighbor', {
    'neighbor_address': fields.String(required=True, description='BGP neighbor address'),
    'peer_as': fields.Integer(required=True, description='Peer AS number')
})

ospf_network_model = api.model('OSPFNetwork', {
    'network': fields.String(required=True, description='OSPF network'),
    'area': fields.String(required=True, description='OSPF area')
})

access_list_model = api.model('AccessList', {
    'name': fields.String(required=True, description='Access list name'),
    'action': fields.String(required=True, description='Action (permit/deny)'),
    'network': fields.String(required=True, description='Network'),
    'seq': fields.Integer(required=False, description='Sequence number')
})

prefix_list_model = api.model('PrefixList', {
    'name': fields.String(required=True, description='Prefix list name'),
    'action': fields.String(required=True, description='Action (permit/deny)'),
    'prefix': fields.String(required=True, description='Prefix'),
    'seq': fields.Integer(required=False, description='Sequence number'),
    'le': fields.Integer(required=False, description='Less than or equal to'),
    'ge': fields.Integer(required=False, description='Greater than or equal to')
})

route_map_model = api.model('RouteMap', {
    'name': fields.String(required=True, description='Route map name'),
    'action': fields.String(required=True, description='Action (permit/deny)'),
    'order': fields.Integer(required=True, description='Order')
})

static_route_model = api.model('StaticRoute', {
    'destination': fields.String(required=True, description='Destination'),
    'gateway': fields.String(required=True, description='Gateway')
})

bgp_start_model = api.model('BGPStart', {
    'port': fields.Integer(required=False, description='Port'),
    'listenon': fields.String(required=False, description='Listen on'),
    'daemon': fields.String(required=False, description='Daemon'),
    'config_file': fields.String(required=False, description='Config file'),
    'no_kernel': fields.Boolean(required=False, description='No kernel')
})

router_id_model = api.model('RouterID', {
    'router_id': fields.String(required=True, description='Router ID')
})


# System endpoints
@ns_system.route('/execute')
class ExecuteCommand(Resource):
    @ns_system.expect(command_model)
    def post(self):
        data = request.json
        command = data['command']
        try:
            stdout, stderr = frr_client_system.execute_command(command)
            if stderr:
                return {'error': stderr}, 400
            return {'output': stdout}
        except Exception as e:
            logging.exception(f"Error executing command: {e}")
            return {'error': str(e)}, 500

@ns_system.route('/version')
class GetVersion(Resource):
    def get(self):
        try:
            stdout, stderr = frr_client_system.get_version()
            if stderr:
                return {'error': stderr}, 400
            return {'output': stdout}
        except Exception as e:
            logging.exception(f"Error retrieving version: {e}")
            return {'error': str(e)}, 500

@ns_system.route('/interfaces')
class GetInterfaces(Resource):
    def get(self):
        try:
            stdout, stderr = frr_client_system.get_interfaces()
            if stderr:
                return {'error': stderr}, 400
            return {'output': stdout}
        except Exception as e:
            logging.exception(f"Error retrieving interfaces: {e}")
            return {'error': str(e)}, 500


# BGP endpoints
@ns_bgp.route('/neighbors')
class GetBGPNeighbors(Resource):
    def get(self):
        try:
            stdout, stderr = frr_client_routing.get_bgp_neighbors()
            if stderr:
                return {'error': stderr}, 400
            return {'output': stdout}
        except Exception as e:
            logging.exception(f"Error retrieving BGP neighbors: {e}")
            return {'error': str(e)}, 500

@ns_bgp.route('/neighbor')
class BGPNeighbor(Resource):
    @ns_bgp.expect(bgp_neighbor_model)
    def post(self):
        data = request.json
        neighbor_address = data['neighbor_address']
        peer_as = data['peer_as']
        try:
            stdout, stderr = frr_client_routing.add_bgp_neighbor(64512, neighbor_address, peer_as)
            if stderr:
                return {'error': stderr}, 400
            return {'output': stdout}
        except Exception as e:
            logging.exception(f"Error adding BGP neighbor: {e}")
            return {'error': str(e)}, 500

    @ns_bgp.expect(command_model)
    def delete(self):
        data = request.json
        neighbor_address = data['neighbor_address']
        try:
            stdout, stderr = frr_client_routing.remove_bgp_neighbor(64512, neighbor_address)
            if stderr:
                return {'error': stderr}, 400
            return {'output': stdout}
        except Exception as e:
            logging.exception(f"Error removing BGP neighbor: {e}")
            return {'error': str(e)}, 500

@ns_bgp.route('/start')
class StartBGP(Resource):
    @ns_bgp.expect(bgp_start_model)
    def post(self):
        data = request.json
        port = data.get('port')
        listenon = data.get('listenon')
        daemon = data.get('daemon')
        config_file = data.get('config_file')
        no_kernel = data.get('no_kernel')
        try:
            stdout, stderr = frr_client_routing.start_bgp(port, listenon, daemon, config_file, no_kernel)
            if stderr:
                return {'error': stderr}, 400
            return {'output': stdout}
        except Exception as e:
            logging.exception(f"Error starting BGP: {e}")
            return {'error': str(e)}, 500

@ns_bgp.route('/debug')
class DebugBGP(Resource):
    @ns_bgp.expect(command_model)
    def post(self):
        data = request.json
        command = data['command']
        try:
            stdout, stderr = frr_client_routing.debug_bgp(command)
            if stderr:
                return {'error': stderr}, 400
            return {'output': stdout}
        except Exception as e:
            logging.exception(f"Error debugging BGP: {e}")
            return {'error': str(e)}, 500

@ns_bgp.route('/dump')
class DumpBGP(Resource):
    @ns_bgp.expect(command_model)
    def post(self):
        data = request.json
        command = data['command']
        try:
            stdout, stderr = frr_client_routing.dump_bgp(command)
            if stderr:
                return {'error': stderr}, 400
            return {'output': stdout}
        except Exception as e:
            logging.exception(f"Error dumping BGP: {e}")
            return {'error': str(e)}, 500

@ns_bgp.route('/show')
class ShowBGP(Resource):
    def get(self):
        command = request.args.get('command')
        if not command:
            return {'error': 'command is required'}, 400
        try:
            stdout, stderr = frr_client_routing.show_bgp(command)
            if stderr:
                return {'error': stderr}, 400
            return {'output': stdout}
        except Exception as e:
            logging.exception(f"Error showing BGP information: {e}")
            return {'error': str(e)}, 500

@ns_bgp.route('/dampening')
class ShowBGPDampening(Resource):
    def get(self):
        command = request.args.get('command')
        if not command:
            return {'error': 'command is required'}, 400
        try:
            stdout, stderr = frr_client_routing.show_bgp_dampening(command)
            if stderr:
                return {'error': stderr}, 400
            return {'output': stdout}
        except Exception as e:
            logging.exception(f"Error showing BGP dampening information: {e}")
            return {'error': str(e)}, 500


# OSPF endpoints
@ns_ospf.route('/network')
class OSPFNetwork(Resource):
    @ns_ospf.expect(ospf_network_model)
    def post(self):
        data = request.json
        network = data['network']
        area = data['area']
        try:
            stdout, stderr = frr_client_routing.add_ospf_network(network, area)
            if stderr:
                return {'error': stderr}, 400
            return {'output': stdout}
        except Exception as e:
            logging.exception(f"Error adding OSPF network: {e}")
            return {'error': str(e)}, 500

    @ns_ospf.expect(ospf_network_model)
    def delete(self):
        data = request.json
        network = data['network']
        area = data['area']
        try:
            stdout, stderr = frr_client_routing.remove_ospf_network(network, area)
            if stderr:
                return {'error': stderr}, 400
            return {'output': stdout}
        except Exception as e:
            logging.exception(f"Error removing OSPF network: {e}")
            return {'error': str(e)}, 500


# OSPFv3 endpoints
@ns_ospfv3.route('/network')
class OSPFv3Network(Resource):
    @ns_ospfv3.expect(ospf_network_model)
    def post(self):
        data = request.json
        network = data['network']
        area = data['area']
        try:
            stdout, stderr = frr_client_routing.add_ospfv3_network(network, area)
            if stderr:
                return {'error': stderr}, 400
            return {'output': stdout}
        except Exception as e:
            logging.exception(f"Error adding OSPFv3 network: {e}")
            return {'error': str(e)}, 500

    @ns_ospfv3.expect(ospf_network_model)
    def delete(self):
        data = request.json
        network = data['network']
        area = data['area']
        try:
            stdout, stderr = frr_client_routing.remove_ospfv3_network(network, area)
            if stderr:
                return {'error': stderr}, 400
            return {'output': stdout}
        except Exception as e:
            logging.exception(f"Error removing OSPFv3 network: {e}")
            return {'error': str(e)}, 500


# Filtering endpoints
@ns_filter.route('/access-list')
class AccessList(Resource):
    @ns_filter.expect(access_list_model)
    def post(self):
        data = request.json
        name = data['name']
        action = data['action']
        network = data['network']
        seq = data.get('seq')
        try:
            stdout, stderr = frr_client_filtering.add_access_list(name, action, network, seq)
            if stderr:
                return {'error': stderr}, 400
            return {'output': stdout}
        except Exception as e:
            logging.exception(f"Error adding access list: {e}")
            return {'error': str(e)}, 500

    @ns_filter.expect(access_list_model)
    def delete(self):
        data = request.json
        name = data['name']
        action = data['action']
        network = data['network']
        seq = data.get('seq')
        try:
            stdout, stderr = frr_client_filtering.remove_access_list(name, action, network, seq)
            if stderr:
                return {'error': stderr}, 400
            return {'output': stdout}
        except Exception as e:
            logging.exception(f"Error removing access list: {e}")
            return {'error': str(e)}, 500

@ns_filter.route('/prefix-list')
class PrefixList(Resource):
    @ns_filter.expect(prefix_list_model)
    def post(self):
        data = request.json
        name = data['name']
        action = data['action']
        prefix = data['prefix']
        seq = data.get('seq')
        le = data.get('le')
        ge = data.get('ge')
        try:
            stdout, stderr = frr_client_filtering.add_prefix_list(name, action, prefix, seq, le, ge)
            if stderr:
                return {'error': stderr}, 400
            return {'output': stdout}
        except Exception as e:
            logging.exception(f"Error adding prefix list: {e}")
            return {'error': str(e)}, 500

    @ns_filter.expect(prefix_list_model)
    def delete(self):
        data = request.json
        name = data['name']
        action = data['action']
        prefix = data['prefix']
        seq = data.get('seq')
        le = data.get('le')
        ge = data.get('ge')
        try:
            stdout, stderr = frr_client_filtering.remove_prefix_list(name, action, prefix, seq, le, ge)
            if stderr:
                return {'error': stderr}, 400
            return {'output': stdout}
        except Exception as e:
            logging.exception(f"Error removing prefix list: {e}")
            return {'error': str(e)}, 500


# Route map endpoints
@ns_routemap.route('/')
class RouteMap(Resource):
    @ns_routemap.expect(route_map_model)
    def post(self):
        data = request.json
        name = data['name']
        action = data['action']
        order = data['order']
        try:
            stdout, stderr = frr_client_routemap.add_route_map(name, action, order)
            if stderr:
                return {'error': stderr}, 400
            return {'output': stdout}
        except Exception as e:
            logging.exception(f"Error adding route map: {e}")
            return {'error': str(e)}, 500

    @ns_routemap.expect(route_map_model)
    def delete(self):
        data = request.json
        name = data['name']
        action = data['action']
        order = data['order']
        try:
            stdout, stderr = frr_client_routemap.remove_route_map(name, action, order)
            if stderr:
                return {'error': stderr}, 400
            return {'output': stdout}
        except Exception as e:
            logging.exception(f"Error removing route map: {e}")
            return {'error': str(e)}, 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

