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

