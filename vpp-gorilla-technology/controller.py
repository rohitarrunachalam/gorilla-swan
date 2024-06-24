from flask import Flask, request
from flask_restx import Api, Resource, fields
import logging
from vpp.debug_client import DebugClient
from vpp.event_logger_client import EventLoggerClient
from vpp.interface_manager_client import InterfaceManagerClient
from vpp.vlib_api_client import VlibApiClient
from vpp.vxlan_client import VxlanClient
# Vnet
from vpp.vnet.appacket_client import APPacketClient
from vpp.vnet.cdp_client import CdpClient
from vpp.vnet.classify_client import ClassifyClient
from vpp.vnet.cop_client import COPClient
from vpp.vnet.dhcp_client import Dhcpv6Client
from vpp.vnet.dhcp_client import DhcpClient
from vpp.vnet.dpdk_client import DpdkClient
from vpp.vnet.flow_client import FlowClient
from vpp.vnet.gre_client import GreClient
from vpp.vnet.netmap_client import NetmapClient
from vpp.vnet.virtio_client import VirtioClient
from vpp.vnet.vnet_client import VNetClient

# Plugins
from vpp.plugins.ila_client import IlaClient
from vpp.plugins.ioam_client import IoamClient
from vpp.plugins.lb_client import LbClient
from vpp.plugins.snat_client import SnatClient
from vpp.plugins.vcgn_client import VcgnClient

# VPP
from vpp.vpp_app import VPPAppCommands 
from vpp.vpp_oam import VPPOAMCommands
from vpp.vpp_vpp_api import VPPClientVppApi

# Initialize Flask application and Flask-RESTx API
app = Flask(__name__)
api = Api(app, version='1.0', title='VPP Management API', description='APIs for managing VPP operations')

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

# Initialize clients
debug_client = DebugClient()
event_logger_client = EventLoggerClient()
interface_manager_client = InterfaceManagerClient()
vlib_api_client = VlibApiClient()
vxlan_client = VxlanClient() 
ap_packet_client = APPacketClient()
cdp_client = CdpClient()
classify_client = ClassifyClient()
cop_client = COPClient()
dhcp_client = DhcpClient()
dhcpv6_client = Dhcpv6Client()
dpdk_client = DpdkClient()
flow_client = FlowClient()
gre_client = GreClient()
netmap_client = NetmapClient()
virtio_client = VirtioClient()
vnet_client = VNetClient()
# Plugin
ila_client = IlaClient()
ioam_client = IoamClient()
lb_client = LbClient()
snat_client = SnatClient()
vcgn_client = VcgnClient()

vpp_app_commands = VPPAppCommands()
vpp_oam = VPPOAMCommands()

# Define namespaces
debug_ns = api.namespace('debug', description='Debug Operations')
event_logger_ns = api.namespace('event-logger', description='Event Logger Operations')
interface_ns = api.namespace('interface', description='Interface Management Operations')
vlib_ns = api.namespace('vlib', description='Vlib API Operations')
vxlan_ns = api.namespace('vxlan', description='VxLAN Operations')

# Vnet based endpoints' namespace
ap_packet_ns = api.namespace('ap-packet', description='APPacket Operations')
cdp_ns = api.namespace('cdp', description='CDP Operations')
classify_ns = api.namespace('classify', description='Classify Operations')
cop_ns = api.namespace('cop', description='COP Operations')
dhcp_ns = api.namespace('dhcp', description='DHCP Operations')
dhcpv6_ns = api.namespace('dhcpv6', description='DHCPv6 Operations')
dpdk_ns = api.namespace('dpdk', description='DPDK Operations')
flow_ns = api.namespace('flow', description='Flow Operations')
gre_ns = api.namespace('gre', description='GRE Tunnel Operations')
netmap_ns = api.namespace('netmap', description='Netmap Operations')
virtio_ns = api.namespace('virtio', description='Virtio Operations')
vnet_ns = api.namespace('vnet', description='VNet Operations')

# Plugin
ila_ns = api.namespace('ila', description='ILA Operations')
ioam_ns = api.namespace('ioam', description='IOAM Operations')
lb_ns = api.namespace('lb', description='LB Operations')
snat_ns = api.namespace('snat', description='SNAT Operations')
vcgn_ns = api.namespace('vcgn', description='VCGN Operations')
# vpp
vpp_app_ns = api.namespace('vpp-app', description='VPP Application Commands')
oam_ns = api.namespace('oam', description='Operations and Administration Maintenance (OAM) Commands')
vpp_commands_ns = api.namespace('vpp-commands', description='VPP Command Operations')




# Define DTOs (Data Transfer Objects) for request payloads
loopback_model = api.model('LoopbackInterface', {
    'mac_address': fields.String(required=False, description='MAC address for loopback interface')
})

proxy_arp_model = api.model('ProxyARPInterface', {
    'interface': fields.String(required=True, description='Interface name'),
    'enable': fields.Boolean(required=False, default=True, description='Enable or disable Proxy ARP')
})

ip_arp_model = api.model('IPARPInterface', {
    'interface': fields.String(required=True, description='Interface name'),
    'ip_address': fields.String(required=True, description='IP address for ARP entry'),
    'mac_address': fields.String(required=True, description='MAC address for ARP entry'),
    'static': fields.Boolean(required=False, default=False, description='Static ARP entry')
})

command_model = api.model('Command', {
    'command': fields.String(required=True, description='Command to execute')
})

size_model = api.model('Size', {
    'size': fields.Integer(required=True, description='Size for resizing event log')
})

filename_model = api.model('Filename', {
    'filename': fields.String(required=True, description='Filename for saving event log')
})

# Debug endpoints
@debug_ns.route('/execute')
class ExecuteCommand(Resource):
    @api.expect(command_model)
    def post(self):
        try:
            data = request.json
            command = data.get('command')
            if not command:
                return {'error': 'Command is required'}, 400
            output = debug_client.run_vpp_command(command)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error executing command: {e}")
            return {'error': str(e)}, 500

@debug_ns.route('/history')
class ShowCliHistory(Resource):
    def get(self):
        try:
            output = debug_client.show_cli_history()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error showing CLI history: {e}")
            return {'error': str(e)}, 500

@debug_ns.route('/quit')
class QuitCli(Resource):
    def get(self):
        try:
            output = debug_client.quit_cli()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error quitting CLI: {e}")
            return {'error': str(e)}, 500

@debug_ns.route('/terminal/ansi')
class SetTerminalAnsi(Resource):
    @api.expect(fields.Boolean)
    def post(self):
        try:
            data = request.json
            enable = data.get('enable', True)
            output = debug_client.set_terminal_ansi(enable)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error setting terminal ANSI: {e}")
            return {'error': str(e)}, 500

@debug_ns.route('/terminal/history')
class SetTerminalHistory(Resource):
    @api.expect(fields.Boolean)
    def post(self):
        try:
            data = request.json
            enable = data.get('enable', True)
            limit = data.get('limit')
            output = debug_client.set_terminal_history(enable, limit)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error setting terminal history: {e}")
            return {'error': str(e)}, 500

@debug_ns.route('/terminal/pager')
class SetTerminalPager(Resource):
    @api.expect(fields.Boolean)
    def post(self):
        try:
            data = request.json
            enable = data.get('enable', True)
            limit = data.get('limit')
            output = debug_client.set_terminal_pager(enable, limit)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error setting terminal pager: {e}")
            return {'error': str(e)}, 500

@debug_ns.route('/terminal/settings')
class ShowTerminalSettings(Resource):
    def get(self):
        try:
            output = debug_client.show_terminal_settings()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error showing terminal settings: {e}")
            return {'error': str(e)}, 500

@debug_ns.route('/unix-errors')
class ShowUnixErrors(Resource):
    def get(self):
        try:
            output = debug_client.show_unix_errors()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error showing Unix errors: {e}")
            return {'error': str(e)}, 500

# Event Logger endpoints
@event_logger_ns.route('/clear')
class ClearEventLog(Resource):
    def get(self):
        try:
            output = event_logger_client.clear_event_log()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error clearing event log: {e}")
            return {'error': str(e)}, 500

@event_logger_ns.route('/resize')
class ResizeEventLog(Resource):
    @api.expect(size_model)
    def post(self):
        try:
            data = request.json
            size = data.get('size')
            output = event_logger_client.resize_event_log(size)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error resizing event log: {e}")
            return {'error': str(e)}, 500

@event_logger_ns.route('/restart')
class RestartEventLogger(Resource):
    def get(self):
        try:
            output = event_logger_client.restart_event_logger()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error restarting event logger: {e}")
            return {'error': str(e)}, 500

@event_logger_ns.route('/save')
class SaveEventLog(Resource):
    @api.expect(filename_model)
    def post(self):
        try:
            data = request.json
            filename = data.get('filename')
            output = event_logger_client.save_event_log(filename)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error saving event log: {e}")
            return {'error': str(e)}, 500

@event_logger_ns.route('/stop')
class StopEventLogger(Resource):
    def get(self):
        try:
            output = event_logger_client.stop_event_logger()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error stopping event logger: {e}")
            return {'error': str(e)}, 500

@event_logger_ns.route('/info')
class ShowEventLoggerInfo(Resource):
    def get(self):
        try:
            output = event_logger_client.show_event_logger_info()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error showing event logger info: {e}")
            return {'error': str(e)}, 500

# Interface Manager endpoints
@interface_ns.route('/list')
class ListInterfaces(Resource):
    def get(self):
        try:
            output = interface_manager_client.list_interfaces()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error listing interfaces: {e}")
            return {'error': str(e)}, 500

@interface_ns.route('/detail/<interface_name>')
class InterfaceDetail(Resource):
    def get(self, interface_name):
        try:
            output = interface_manager_client.get_interface_detail(interface_name)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error getting interface detail for {interface_name}: {e}")
            return {'error': str(e)}, 500

@interface_ns.route('/create-loopback')
class CreateLoopbackInterface(Resource):
    @api.expect(loopback_model)
    def post(self):
        try:
            data = request.json
            mac_address = data.get('mac_address')
            output = interface_manager_client.create_loopback_interface(mac_address)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error creating loopback interface: {e}")
            return {'error': str(e)}, 500

@interface_ns.route('/delete-loopback/<interface>')
class DeleteLoopbackInterface(Resource):
    def delete(self, interface):
        try:
            output = interface_manager_client.delete_loopback_interface(interface)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error deleting loopback interface {interface}: {e}")
            return {'error': str(e)}, 500

@interface_ns.route('/set-proxy-arp')
class SetProxyARP(Resource):
    @api.expect(proxy_arp_model)
    def post(self):
        try:
            data = request.json
            interface = data.get('interface')
            enable = data.get('enable', True)
            output = interface_manager_client.set_interface_proxy_arp(interface, enable)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error setting Proxy ARP for interface {interface}: {e}")
            return {'error': str(e)}, 500

@interface_ns.route('/set-ip-arp')
class SetIPARP(Resource):
    @api.expect(ip_arp_model)
    def post(self):
        try:
            data = request.json
            interface = data.get('interface')
            ip_address = data.get('ip_address')
            mac_address = data.get('mac_address')
            static = data.get('static', False)
            output = interface_manager_client.set_ip_arp(interface, ip_address, mac_address, static)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error setting IP ARP for interface {interface}: {e}")
            return {'error': str(e)}, 500

# Vlib API endpoints (new endpoints for VlibApiClient)
@vlib_ns.route('/api_trace')
class ApiTrace(Resource):
    @api.expect(fields.String(required=True))
    def post(self):
        try:
            data = request.json
            action = data.get('action')
            file = data.get('file')
            result = vlib_api_client.api_trace(action, file)
            return {'result': result}
        except Exception as e:
            logging.exception(f"Error in API trace: {e}")
            return {'error': str(e)}, 500

@vlib_ns.route('/test_node_serialize')
class TestNodeSerialize(Resource):
    @api.expect(fields.Integer)
    def post(self):
        try:
            data = request.json
            max_threads = data.get('max_threads')
            result = vlib_api_client.test_node_serialize(max_threads)
            return {'result': result}
        except Exception as e:
            logging.exception(f"Error in test node serialize: {e}")
            return {'error': str(e)}, 500

@vlib_ns.route('/clear_api_histogram')
class ClearApiHistogram(Resource):
    def get(self):
        try:
            result = vlib_api_client.clear_api_histogram()
            return {'result': result}
        except Exception as e:
            logging.exception(f"Error clearing API histogram: {e}")
            return {'error': str(e)}, 500

@vlib_ns.route('/set_api_trace')
class SetApiTrace(Resource):
    def get(self):
        try:
            result = vlib_api_client.set_api_trace()
            return {'result': result}
        except Exception as e:
            logging.exception(f"Error setting API trace: {e}")
            return {'error': str(e)}, 500

@vlib_ns.route('/show_api')
class ShowApi(Resource):
    def get(self):
        try:
            result = vlib_api_client.show_api()
            return {'result': result}
        except Exception as e:
            logging.exception(f"Error showing API: {e}")
            return {'error': str(e)}, 500

@vlib_ns.route('/show_api_clients')
class ShowApiClients(Resource):
    def get(self):
        try:
            result = vlib_api_client.show_api_clients()
            return {'result': result}
        except Exception as e:
            logging.exception(f"Error showing API clients: {e}")
            return {'error': str(e)}, 500

@vlib_ns.route('/show_api_histogram')
class ShowApiHistogram(Resource):
    def get(self):
        try:
            result = vlib_api_client.show_api_histogram()
            return {'result': result}
        except Exception as e:
            logging.exception(f"Error showing API histogram: {e}")
            return {'error': str(e)}, 500

@vlib_ns.route('/show_api_message_table')
class ShowApiMessageTable(Resource):
    def get(self):
        try:
            result = vlib_api_client.show_api_message_table()
            return {'result': result}
        except Exception as e:
            logging.exception(f"Error showing API message table: {e}")
            return {'error': str(e)}, 500

@vlib_ns.route('/show_api_plugin')
class ShowApiPlugin(Resource):
    def get(self):
        try:
            result = vlib_api_client.show_api_plugin()
            return {'result': result}
        except Exception as e:
            logging.exception(f"Error showing API plugin: {e}")
            return {'error': str(e)}, 500

@vlib_ns.route('/show_api_ring_stats')
class ShowApiRingStats(Resource):
    def get(self):
        try:
            result = vlib_api_client.show_api_ring_stats()
            return {'result': result}
        except Exception as e:
            logging.exception(f"Error showing API ring stats: {e}")
            return {'error': str(e)}, 500

@vlib_ns.route('/show_pci')
class ShowPci(Resource):
    @api.expect(fields.Boolean)
    def get(self):
        try:
            show_all = request.args.get('show_all', type=bool, default=False)
            result = vlib_api_client.show_pci(show_all)
            return {'result': result}
        except Exception as e:
            logging.exception(f"Error showing PCI: {e}")
            return {'error': str(e)}, 500


# VxLAN endpoints
@vxlan_ns.route('/create_tunnel')
class CreateVxlanTunnel(Resource):
    @api.expect(fields.String(required=True), fields.String(required=True), fields.Integer(required=True), fields.Integer(required=False), fields.String(required=False), fields.Boolean(required=False, default=False))
    def post(self):
        try:
            data = request.json
            src_addr = data.get('src_addr')
            dst_addr = data.get('dst_addr')
            vni = data.get('vni')
            encap_vrf_id = data.get('encap_vrf_id')
            decap_next = data.get('decap_next')
            delete = data.get('delete', False)
            
            output = vxlan_client.create_vxlan_tunnel(src_addr, dst_addr, vni, encap_vrf_id, decap_next, delete)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error creating VXLAN tunnel: {e}")
            return {'error': str(e)}, 500

@vxlan_ns.route('/show_tunnel')
class ShowVxlanTunnel(Resource):
    def get(self):
        try:
            output = vxlan_client.show_vxlan_tunnel()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error showing VXLAN tunnel: {e}")
            return {'error': str(e)}, 500

# Endpoints defined for APPacketClient
@ap_packet_ns.route('/create_host_interface')
class CreateHostInterface(Resource):
    @api.expect(fields.String(required=True))
    def post(self):
        try:
            data = request.json
            name = data.get('name')
            output = ap_packet_client.create_host_interface(name)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error creating host interface: {e}")
            return {'error': str(e)}, 500

@ap_packet_ns.route('/delete_host_interface/<name>')
class DeleteHostInterface(Resource):
    def delete(self, name):
        try:
            output = ap_packet_client.delete_host_interface(name)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error deleting host interface {name}: {e}")
            return {'error': str(e)}, 500


# Endpoints defined for CdpClient
@cdp_ns.route('/show_cdp')
class ShowCdp(Resource):
    def get(self):
        try:
            output = cdp_client.show_cdp()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error showing CDP: {e}")
            return {'error': str(e)}, 500


# Endpoints for ClassifyClient
@classify_ns.route('/set_interface_input_acl')
class SetInterfaceInputACL(Resource):
    @api.expect(fields.String(required=True), fields.Integer(required=True))
    def post(self):
        try:
            data = request.json
            interface_name = data.get('interface_name')
            acl_index = data.get('acl_index')
            output = classify_client.set_interface_input_acl(interface_name, acl_index)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error setting interface input ACL: {e}")
            return {'error': str(e)}, 500

@classify_ns.route('/show_inacl')
class ShowInACL(Resource):
    def get(self):
        try:
            output = classify_client.show_inacl()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error showing inacl: {e}")
            return {'error': str(e)}, 500

@classify_ns.route('/set_policer_classify')
class SetPolicerClassify(Resource):
    @api.expect(api.model('SetPolicerClassify', {
        'policer_name': fields.String(required=True),
        'table_index': fields.Integer(required=True)
    }))
    def post(self):
        try:
            data = request.json
            policer_name = data['policer_name']
            table_index = data['table_index']
            output = classify_client.set_policer_classify(policer_name, table_index)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error setting policer classify: {e}")
            return {'error': str(e)}, 500


@classify_ns.route('/show_classify_policer')
class ShowClassifyPolicer(Resource):
    def get(self):
        try:
            output = classify_client.show_classify_policer()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error showing classify policer: {e}")
            return {'error': str(e)}, 500


@classify_ns.route('/classify_session')
class ClassifySession(Resource):
    @api.expect(api.model('ClassifySession', {
        'table_index': fields.Integer(required=True),
        'match': fields.String(required=True),
        'hit_next_index': fields.String(required=True),
        'l2': fields.String(),
        'miss_next_index': fields.String()
    }))
    def post(self):
        try:
            data = request.json
            table_index = data['table_index']
            match = data['match']
            hit_next_index = data['hit_next_index']
            l2 = data.get('l2')
            miss_next_index = data.get('miss_next_index')
            output = classify_client.classify_session(table_index, match, hit_next_index, l2, miss_next_index)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error executing classify session: {e}")
            return {'error': str(e)}, 500

@classify_ns.route('/classify_table')
class ClassifyTable(Resource):
    @api.expect(api.model('ClassifyTable', {
        'table_index': fields.Integer(required=True),
        'next_table_index': fields.Integer(),
        'miss_next_index': fields.Integer(),
        'skip_n': fields.Integer(),
        'match_n': fields.Integer(),
        'mask': fields.Integer(),
        'delete': fields.Boolean()
    }))
    def post(self):
        try:
            data = request.json
            table_index = data['table_index']
            next_table_index = data.get('next_table_index')
            miss_next_index = data.get('miss_next_index')
            skip_n = data.get('skip_n')
            match_n = data.get('match_n')
            mask = data.get('mask')
            delete = data.get('delete', False)
            output = classify_client.classify_table(table_index, next_table_index, miss_next_index, skip_n, match_n, mask, delete)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error executing classify table: {e}")
            return {'error': str(e)}, 500


@classify_ns.route('/show_classify_tables')
class ShowClassifyTables(Resource):
    def get(self):
        try:
            output = classify_client.show_classify_tables()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error showing classify tables: {e}")
            return {'error': str(e)}, 500

@classify_ns.route('/test_classify')
class TestClassify(Resource):
    def get(self):
        try:
            output = classify_client.test_classify()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error testing classify: {e}")
            return {'error': str(e)}, 500

# Endpoints for COP client
@cop_ns.route('/cop_interface/<string:interface_name>')
class COPInterface(Resource):
    @api.expect(api.parser().add_argument('options', action='append', help='Optional arguments'))
    def post(self, interface_name):
        try:
            options = request.args.getlist('options')
            output = cop_client.cop_interface(interface_name, *options)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error executing cop interface command: {e}")
            return {'error': str(e)}, 500

@cop_ns.route('/cop_whitelist')
class COPWhitelist(Resource):
    @api.expect(api.parser().add_argument('options', action='append', help='Optional arguments'))
    def post(self):
        try:
            options = request.args.getlist('options')
            output = cop_client.cop_whitelist(*options)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error executing cop whitelist command: {e}")
            return {'error': str(e)}, 500


# dhcp endpoints
@dhcp_ns.route('/set_dhcp_client/<string:interface_name>')
class SetDhcpClient(Resource):
    def post(self, interface_name):
        try:
            output = dhcp_client.set_dhcp_client(interface_name)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error setting DHCP client: {e}")
            return {'error': str(e)}, 500

@dhcp_ns.route('/show_dhcp_client')
class ShowDhcpClient(Resource):
    def get(self):
        try:
            output = dhcp_client.show_dhcp_client()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error showing DHCP client: {e}")
            return {'error': str(e)}, 500

@dhcp_ns.route('/set_dhcp_option_82_vss')
class SetDhcpOption82Vss(Resource):
    def post(self):
        try:
            output = dhcp_client.set_dhcp_option_82_vss()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error setting DHCP Option 82 VSS: {e}")
            return {'error': str(e)}, 500

@dhcp_ns.route('/set_dhcp_proxy')
class SetDhcpProxy(Resource):
    def post(self):
        try:
            output = dhcp_client.set_dhcp_proxy()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error setting DHCP proxy: {e}")
            return {'error': str(e)}, 500

@dhcp_ns.route('/show_dhcp_option_82_address_interface')
class ShowDhcpOption82AddressInterface(Resource):
    def get(self):
        try:
            output = dhcp_client.show_dhcp_option_82_address_interface()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error showing DHCP Option 82 address interface: {e}")
            return {'error': str(e)}, 500

@dhcp_ns.route('/show_dhcp_proxy')
class ShowDhcpProxy(Resource):
    def get(self):
        try:
            output = dhcp_client.show_dhcp_proxy()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error showing DHCP proxy: {e}")
            return {'error': str(e)}, 500

@dhcp_ns.route('/show_dhcp_vss')
class ShowDhcpVss(Resource):
    def get(self):
        try:
            output = dhcp_client.show_dhcp_vss()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error showing DHCP VSS: {e}")
            return {'error': str(e)}, 500
# dhcpv6 endpoint

@dhcpv6_ns.route('/set_dhcpv6_proxy/<string:interface_name>')
class SetDhcpv6Proxy(Resource):
    def post(self, interface_name):
        try:
            output = dhcpv6_client.set_dhcpv6_proxy(interface_name)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error setting DHCPv6 proxy: {e}")
            return {'error': str(e)}, 500

@dhcpv6_ns.route('/set_dhcpv6_vss/<string:interface_name>')
class SetDhcpv6Vss(Resource):
    @api.expect(api.parser().add_argument('enable', type=bool, default=True, help='Enable or disable DHCPv6 VSS'))
    def post(self, interface_name):
        try:
            enable = api.payload.get('enable', True)
            output = dhcpv6_client.set_dhcpv6_vss(interface_name, enable)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error setting DHCPv6 VSS: {e}")
            return {'error': str(e)}, 500

@dhcpv6_ns.route('/show_dhcpv6_link_address_interface')
class ShowDhcpv6LinkAddressInterface(Resource):
    def get(self):
        try:
            output = dhcpv6_client.show_dhcpv6_link_address_interface()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error showing DHCPv6 link address interface: {e}")
            return {'error': str(e)}, 500

@dhcpv6_ns.route('/show_dhcpv6_proxy')
class ShowDhcpv6Proxy(Resource):
    def get(self):
        try:
            output = dhcpv6_client.show_dhcpv6_proxy()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error showing DHCPv6 proxy: {e}")
            return {'error': str(e)}, 500

@dhcpv6_ns.route('/show_dhcpv6_vss')
class ShowDhcpv6Vss(Resource):
    def get(self):
        try:
            output = dhcpv6_client.show_dhcpv6_vss()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error showing DHCPv6 VSS: {e}")
            return {'error': str(e)}, 500

# dpdk client
@dpdk_ns.route('/clear_efd')
class ClearEfd(Resource):
    def post(self):
        try:
            output = dpdk_client.clear_efd()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error clearing EFD: {e}")
            return {'error': str(e)}, 500

@dpdk_ns.route('/pcap_tx_trace/<string:state>')
class PcapTxTrace(Resource):
    @api.expect(api.parser().add_argument('max_packets', type=int, help='Maximum packets to trace (optional)'))
    @api.expect(api.parser().add_argument('interface', help='Interface name (optional)'))
    @api.expect(api.parser().add_argument('file', help='File name (optional)'))
    def post(self, state):
        try:
            max_packets = api.payload.get('max_packets')
            interface = api.payload.get('interface')
            file = api.payload.get('file')
            output = dpdk_client.pcap_tx_trace(state, max_packets, interface, file)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error executing pcap tx trace: {e}")
            return {'error': str(e)}, 500

@dpdk_ns.route('/set_dpdk_interface_descriptors/<string:interface>')
class SetDpdkInterfaceDescriptors(Resource):
    @api.expect(api.parser().add_argument('n_rx_desc', type=int, help='Number of RX descriptors (optional)'))
    @api.expect(api.parser().add_argument('n_tx_desc', type=int, help='Number of TX descriptors (optional)'))
    def post(self, interface):
        try:
            n_rx_desc = api.payload.get('n_rx_desc')
            n_tx_desc = api.payload.get('n_tx_desc')
            output = dpdk_client.set_dpdk_interface_descriptors(interface, n_rx_desc, n_tx_desc)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error setting DPDK interface descriptors: {e}")
            return {'error': str(e)}, 500

@dpdk_ns.route('/set_dpdk_interface_placement/<string:interface>/<int:workers>')
class SetDpdkInterfacePlacement(Resource):
    def post(self, interface, workers):
        try:
            output = dpdk_client.set_dpdk_interface_placement(interface, workers)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error setting DPDK interface placement: {e}")
            return {'error': str(e)}, 500

@dpdk_ns.route('/set_efd/<string:mode>')
class SetEfd(Resource):
    @api.expect(api.parser().add_argument('interface', help='Interface name (optional)'))
    def post(self, mode):
        try:
            interface = api.payload.get('interface')
            output = dpdk_client.set_efd(mode, interface)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error setting EFD: {e}")
            return {'error': str(e)}, 500

@dpdk_ns.route('/show_dpdk_buffer')
class ShowDpdkBuffer(Resource):
    def get(self):
        try:
            output = dpdk_client.show_dpdk_buffer()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error showing DPDK buffer: {e}")
            return {'error': str(e)}, 500

@dpdk_ns.route('/show_dpdk_interface_placement')
class ShowDpdkInterfacePlacement(Resource):
    def get(self):
        try:
            output = dpdk_client.show_dpdk_interface_placement()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error showing DPDK interface placement: {e}")
            return {'error': str(e)}, 500

@dpdk_ns.route('/show_efd')
class ShowEfd(Resource):
    def get(self):
        try:
            output = dpdk_client.show_efd()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error showing EFD: {e}")
            return {'error': str(e)}, 500

@dpdk_ns.route('/test_dpdk_buffer')
class TestDpdkBuffer(Resource):
    def get(self):
        try:
            output = dpdk_client.test_dpdk_buffer()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error testing DPDK buffer: {e}")
            return {'error': str(e)}, 500

@dpdk_ns.route('/create_vhost_user/<string:socket>')
class CreateVhostUser(Resource):
    @api.expect(api.parser().add_argument('server', help='Server name (optional)'))
    def post(self, socket):
        try:
            server = api.payload.get('server')
            output = dpdk_client.create_vhost_user(socket, server)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error creating vhost user: {e}")
            return {'error': str(e)}, 500

@dpdk_ns.route('/delete_vhost_user/<string:socket>')
class DeleteVhostUser(Resource):
    def delete(self, socket):
        try:
            output = dpdk_client.delete_vhost_user(socket)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error deleting vhost user: {e}")
            return {'error': str(e)}, 500

@dpdk_ns.route('/show_vhost_user')
class ShowVhostUser(Resource):
    def get(self):
        try:
            output = dpdk_client.show_vhost_user()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error showing vhost user: {e}")
            return {'error': str(e)}, 500



# Flow client
@flow_ns.route('/set_ipfix/<string:collector_ip>/<int:collector_port>')
class SetIpfix(Resource):
    @api.expect(api.parser().add_argument('src_ip', help='Source IP address (optional)'))
    @api.expect(api.parser().add_argument('vrf_id', type=int, help='VRF ID (optional)'))
    @api.expect(api.parser().add_argument('path_mtu', type=int, help='Path MTU (optional)'))
    def post(self, collector_ip, collector_port):
        try:
            src_ip = api.payload.get('src_ip')
            vrf_id = api.payload.get('vrf_id')
            path_mtu = api.payload.get('path_mtu')
            output = flow_client.set_ipfix(collector_ip, collector_port, src_ip, vrf_id, path_mtu)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error setting IPFIX: {e}")
            return {'error': str(e)}, 500

@flow_ns.route('/flow_classify/<string:flow_name>/<string:match_criteria>/<string:action>')
class FlowClassify(Resource):
    def post(self, flow_name, match_criteria, action):
        try:
            output = flow_client.flow_classify(flow_name, match_criteria, action)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error classifying flow: {e}")
            return {'error': str(e)}, 500

# GRE endpoint
@gre_ns.route('/create_gre_tunnel/<string:tunnel_name>/<string:src_address>/<string:dst_address>')
class CreateGreTunnel(Resource):
    @api.expect(api.parser().add_argument('outer_fib_id', type=int, help='Outer FIB ID (optional)'))
    @api.expect(api.parser().add_argument('session_id', type=int, help='Session ID (optional)'))
    def post(self, tunnel_name, src_address, dst_address):
        try:
            outer_fib_id = api.payload.get('outer_fib_id')
            session_id = api.payload.get('session_id')
            output = gre_client.create_gre_tunnel(tunnel_name, src_address, dst_address, outer_fib_id, session_id)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error creating GRE tunnel: {e}")
            return {'error': str(e)}, 500

@gre_ns.route('/show_gre_tunnel')
class ShowGreTunnel(Resource):
    def get(self):
        try:
            output = gre_client.show_gre_tunnel()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error showing GRE tunnel: {e}")
            return {'error': str(e)}, 500


# Netmap client endpoint
@netmap_ns.route('/create_netmap/<string:interface>')
class CreateNetmap(Resource):
    @api.expect(api.parser().add_argument('options', action='append', help='Additional options (optional)'))
    def post(self, interface):
        try:
            options = api.payload.get('options', [])
            output = netmap_client.create_netmap(interface, *options)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error creating Netmap: {e}")
            return {'error': str(e)}, 500

@netmap_ns.route('/delete_netmap/<string:interface>')
class DeleteNetmap(Resource):
    def delete(self, interface):
        try:
            output = netmap_client.delete_netmap(interface)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error deleting Netmap: {e}")
            return {'error': str(e)}, 500

# Virtio client
@virtio_ns.route('/create_vhost_user/<string:socket_path>')
class CreateVhostUser(Resource):
    @api.expect(api.parser().add_argument('options', action='append', help='Additional options (optional)'))
    def post(self, socket_path):
        try:
            options = api.payload.get('options', [])
            output = virtio_client.create_vhost_user(socket_path, *options)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error creating Vhost User: {e}")
            return {'error': str(e)}, 500

@virtio_ns.route('/delete_vhost_user/<string:socket_path>')
class DeleteVhostUser(Resource):
    def delete(self, socket_path):
        try:
            output = virtio_client.delete_vhost_user(socket_path)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error deleting Vhost User: {e}")
            return {'error': str(e)}, 500

@virtio_ns.route('/show_vhost_user')
class ShowVhostUser(Resource):
    @api.expect(api.parser().add_argument('socket_path', help='Socket path (optional)'))
    def get(self):
        try:
            socket_path = api.payload.get('socket_path')
            output = virtio_client.show_vhost_user(socket_path)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error showing Vhost User: {e}")
            return {'error': str(e)}, 500


# Vnet client
@vnet_ns.route('/set_interface_handoff/<string:interface_name>/<string:workers_list>')
class SetInterfaceHandoff(Resource):
    def post(self, interface_name, workers_list):
        try:
            workers = workers_list.split()
            output = vnet_client.set_interface_handoff(interface_name, workers)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error setting interface handoff: {e}")
            return {'error': str(e)}, 500

@vnet_ns.route('/clear_hardware_interfaces')
class ClearHardwareInterfaces(Resource):
    @api.expect(api.parser().add_argument('brief', type=bool, help='Brief mode (optional)'))
    @api.expect(api.parser().add_argument('verbose', type=bool, help='Verbose mode (optional)'))
    @api.expect(api.parser().add_argument('detail', type=bool, help='Detail mode (optional)'))
    @api.expect(api.parser().add_argument('bond', help='Bond (optional)'))
    @api.expect(api.parser().add_argument('interfaces', action='append', help='Interfaces (optional)'))
    def post(self):
        try:
            brief = api.payload.get('brief', False)
            verbose = api.payload.get('verbose', False)
            detail = api.payload.get('detail', False)
            bond = api.payload.get('bond')
            interfaces = api.payload.get('interfaces', [])
            output = vnet_client.clear_hardware_interfaces(brief, verbose, detail, bond, *interfaces)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error clearing hardware interfaces: {e}")
            return {'error': str(e)}, 500

@vnet_ns.route('/clear_interfaces')
class ClearInterfaces(Resource):
    def post(self):
        try:
            output = vnet_client.clear_interfaces()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error clearing interfaces: {e}")
            return {'error': str(e)}, 500

@vnet_ns.route('/create_sub_interfaces/<string:interface_name>/<string:sub_interface_range>')
class CreateSubInterfaces(Resource):
    @api.expect(api.parser().add_argument('options', action='append', help='Additional options (optional)'))
    def post(self, interface_name, sub_interface_range):
        try:
            options = api.payload.get('options', [])
            output = vnet_client.create_sub_interfaces(interface_name, sub_interface_range, *options)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error creating sub-interfaces: {e}")
            return {'error': str(e)}, 500

@vnet_ns.route('/interface_commands')
class InterfaceCommands(Resource):
    def get(self):
        try:
            output = vnet_client.interface_commands()
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error fetching interface commands: {e}")
            return {'error': str(e)}, 500

@vnet_ns.route('/renumber_interface/<string:interface_name>/<int:new_dev_instance>')
class RenumberInterface(Resource):
    def post(self, interface_name, new_dev_instance):
        try:
            output = vnet_client.renumber_interface(interface_name, new_dev_instance)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error renumbering interface: {e}")
            return {'error': str(e)}, 500

@vnet_ns.route('/set_interface/<string:interface_name>')
class SetInterface(Resource):
    @api.expect(api.parser().add_argument('options', action='append', help='Additional options (optional)'))
    def post(self, interface_name):
        try:
            options = api.payload.get('options', [])
            output = vnet_client.set_interface(interface_name, *options)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error setting interface: {e}")
            return {'error': str(e)}, 500

@vnet_ns.route('/set_interface_hw_class/<string:interface_name>/<string:hardware_class>')
class SetInterfaceHwClass(Resource):
    def post(self, interface_name, hardware_class):
        try:
            output = vnet_client.set_interface_hw_class(interface_name, hardware_class)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error setting interface hardware class: {e}")
            return {'error': str(e)}, 500

@vnet_ns.route('/set_interface_mtu/<int:value>/<string:interface_name>')
class SetInterfaceMtu(Resource):
    def post(self, value, interface_name):
        try:
            output = vnet_client.set_interface_mtu(value, interface_name)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error setting interface MTU: {e}")
            return {'error': str(e)}, 500

@vnet_ns.route('/set_interface_promiscuous/<string:state>/<string:interface_name>')
class SetInterfacePromiscuous(Resource):
    def post(self, state, interface_name):
        try:
            output = vnet_client.set_interface_promiscuous(state, interface_name)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error setting interface promiscuous state: {e}")
            return {'error': str(e)}, 500

@vnet_ns.route('/set_interface_state/<string:interface_name>/<string:state>')
class SetInterfaceState(Resource):
    def post(self, interface_name, state):
        try:
            output = vnet_client.set_interface_state(interface_name, state)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error setting interface state: {e}")
            return {'error': str(e)}, 500

@vnet_ns.route('/set_interface_unnumbered/<string:interface_name>')
class SetInterfaceUnnumbered(Resource):
    @api.expect(api.parser().add_argument('use_interface', help='Use interface (optional)'))
    @api.expect(api.parser().add_argument('delete_interface', help='Delete interface (optional)'))
    def post(self, interface_name):
        try:
            use_interface = api.payload.get('use_interface')
            delete_interface = api.payload.get('delete_interface')
            output = vnet_client.set_interface_unnumbered(interface_name, use_interface, delete_interface)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error setting interface unnumbered: {e}")
            return {'error': str(e)}, 500

@vnet_ns.route('/show_hardware_interfaces')
class ShowHardwareInterfaces(Resource):
    @api.expect(api.parser().add_argument('mode', help='Mode (optional)'))
    @api.expect(api.parser().add_argument('interfaces', action='append', help='Interfaces (optional)'))
    def get(self):
        try:
            mode = api.payload.get('mode')
            interfaces = api.payload.get('interfaces', [])
            output = vnet_client.show_hardware_interfaces(mode, *interfaces)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error showing hardware interfaces: {e}")
            return {'error': str(e)}, 500

@vnet_ns.route('/show_interfaces')
class ShowInterfaces(Resource):
    @api.expect(api.parser().add_argument('mode', help='Mode (optional)'))
    @api.expect(api.parser().add_argument('interfaces', action='append', help='Interfaces (optional)'))
    def get(self):
        try:
            mode = api.payload.get('mode')
            interfaces = api.payload.get('interfaces', [])
            output = vnet_client.show_interfaces(mode, *interfaces)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error showing interfaces: {e}")
            return {'error': str(e)}, 500

@vnet_ns.route('/pcap_drop_trace/<string:state>/<int:max_packets>/<string:interface_name>/<string:file_name>/<string:status>')
class PcapDropTrace(Resource):
    def post(self, state, max_packets, interface_name, file_name, status):
        try:
            output = vnet_client.pcap_drop_trace(state, max_packets, interface_name, file_name, status)
            return {'output': output}
        except Exception as e:
            logging.exception(f"Error performing pcap drop trace: {e}")
            return {'error': str(e)}, 500
# ILA

@ila_ns.route('/ila_entry')
class IlaEntry(Resource):
    @ila_ns.expect(ila_ns.model('IlaEntry', {
        'type': fields.String(required=False, description='Type'),
        'sir_address': fields.String(required=False, description='Sir Address'),
        'locator': fields.String(required=False, description='Locator'),
        'vnid': fields.String(required=False, description='VNID'),
        'adj_index': fields.String(required=False, description='Adj Index'),
        'next_hop': fields.String(required=False, description='Next Hop'),
        'direction': fields.String(required=False, description='Direction'),
        'csum_mode': fields.String(required=False, description='Checksum Mode'),
        'delete': fields.Boolean(required=False, description='Delete')
    }))
    def post(self):
        type = request.json.get('type')
        sir_address = request.json.get('sir_address')
        locator = request.json.get('locator')
        vnid = request.json.get('vnid')
        adj_index = request.json.get('adj_index')
        next_hop = request.json.get('next_hop')
        direction = request.json.get('direction')
        csum_mode = request.json.get('csum_mode')
        delete = request.json.get('delete', False)
        return ila_client.ila_entry(type, sir_address, locator, vnid, adj_index, next_hop, direction, csum_mode, delete)

@ila_ns.route('/ila_interface/<string:interface_name>')
class IlaInterface(Resource):
    @ila_ns.doc(params={'disable': 'Disable'})
    def post(self, interface_name):
        disable = request.args.get('disable', False, type=bool)
        return ila_client.ila_interface(interface_name, disable)

@ila_ns.route('/show_ila_entries')
class ShowIlaEntries(Resource):
    def get(self):
        return ila_client.show_ila_entries()
# ioam
@ioam_ns.route('/show_ioam_pot_statistics')
class ShowIoamPotStatistics(Resource):
    def get(self):
        return ioam_client.show_ioam_pot_statistics()

@ioam_ns.route('/clear_pot_profile')
class ClearPotProfile(Resource):
    @ioam_ns.doc(params={'index': 'Index'})
    def post(self):
        index = request.args.get('index', None, type=int)
        return ioam_client.clear_pot_profile(index)

@ioam_ns.route('/set_pot_profile/<string:name>/<int:id>')
class SetPotProfile(Resource):
    @ioam_ns.doc(params={
        'validator_key': 'Validator Key',
        'prime_number': 'Prime Number',
        'secret_share': 'Secret Share',
        'lpc': 'LPC',
        'polynomial2': 'Polynomial2',
        'bits_in_random': 'Bits in Random'
    })
    def post(self, name, id):
        validator_key = request.json.get('validator_key')
        prime_number = request.json.get('prime_number')
        secret_share = request.json.get('secret_share')
        lpc = request.json.get('lpc')
        polynomial2 = request.json.get('polynomial2')
        bits_in_random = request.json.get('bits_in_random')
        return ioam_client.set_pot_profile(name, id, validator_key, prime_number, secret_share, lpc, polynomial2, bits_in_random)

@ioam_ns.route('/set_pot_profile_active/<string:name>/<int:id>')
class SetPotProfileActive(Resource):
    def post(self, name, id):
        return ioam_client.set_pot_profile_active(name, id)

@ioam_ns.route('/show_pot_profile')
class ShowPotProfile(Resource):
    def get(self):
        return ioam_client.show_pot_profile()


@lb_ns.route('/lb_as/<string:vip_prefix>')
class LbAs(Resource):
    @lb_ns.doc(params={'addresses': 'Addresses', 'delete': 'Delete'})
    @lb_ns.expect(lb_ns.model('LbAs', {
        'addresses': fields.List(fields.String),
        'delete': fields.Boolean(default=False)
    }))
    def post(self, vip_prefix):
        addresses = request.json.get('addresses', [])
        delete = request.json.get('delete', False)
        return lb_client.lb_as(vip_prefix, addresses, delete)

@lb_ns.route('/lb_bypass/<string:prefix>/<string:address>')
class LbBypass(Resource):
    @lb_ns.doc(params={'disable': 'Disable'})
    def post(self, prefix, address):
        disable = request.args.get('disable', False, type=bool)
        return lb_client.lb_bypass(prefix, address, disable)

@lb_ns.route('/lb_conf')
class LbConf(Resource):
    @lb_ns.doc(params={
        'ip4_src_address': 'IP4 Source Address',
        'ip6_src_address': 'IP6 Source Address',
        'buckets': 'Buckets',
        'timeout': 'Timeout'
    })
    def post(self):
        ip4_src_address = request.json.get('ip4_src_address')
        ip6_src_address = request.json.get('ip6_src_address')
        buckets = request.json.get('buckets')
        timeout = request.json.get('timeout')
        return lb_client.lb_conf(ip4_src_address, ip6_src_address, buckets, timeout)

@lb_ns.route('/lb_vip/<string:prefix>')
class LbVip(Resource):
    @lb_ns.doc(params={'encap': 'Encap', 'new_len': 'New Length', 'delete': 'Delete'})
    def post(self, prefix):
        encap = request.json.get('encap')
        new_len = request.json.get('new_len')
        delete = request.json.get('delete', False)
        return lb_client.lb_vip(prefix, encap, new_len, delete)

@lb_ns.route('/show_lb')
class ShowLb(Resource):
    def get(self):
        return lb_client.show_lb()

@lb_ns.route('/show_lb_vips')
class ShowLbVips(Resource):
    @lb_ns.doc(params={'verbose': 'Verbose'})
    def get(self):
        verbose = request.args.get('verbose', False, type=bool)
        return lb_client.show_lb_vips(verbose)



# Snatclient
@snat_ns.route('/set_interface_snat/<string:in_intfc>/<string:out_intfc>')
class SetInterfaceSnat(Resource):
    @snat_ns.doc(params={'delete': 'Delete'})
    def post(self, in_intfc, out_intfc):
        delete = request.args.get('delete', False, type=bool)
        return snat_client.set_interface_snat(in_intfc, out_intfc, delete)

@snat_ns.route('/show_snat')
class ShowSnat(Resource):
    def get(self):
        return snat_client.show_snat()

@snat_ns.route('/snat_add_address/<string:ip4_range_start>')
class SnatAddAddress(Resource):
    @snat_ns.doc(params={'ip4_range_end': 'IP4 Range End'})
    def post(self, ip4_range_start):
        ip4_range_end = request.json.get('ip4_range_end')
        return snat_client.snat_add_address(ip4_range_start, ip4_range_end)

# VGCN client



@vcgn_ns.route('/set_vcgn_default_timeout/<string:protocol>')
class SetVcgnDefaultTimeout(Resource):
    def post(self, protocol):
        return vcgn_client.set_vcgn_default_timeout(protocol)

@vcgn_ns.route('/set_vcgn_dynamic_port_start/<int:port_start>')
class SetVcgnDynamicPortStart(Resource):
    def post(self, port_start):
        return vcgn_client.set_vcgn_dynamic_port_start(port_start)

@vcgn_ns.route('/set_vcgn_icmp_timeout/<int:timeout>')
class SetVcgnIcmpTimeout(Resource):
    def post(self, timeout):
        return vcgn_client.set_vcgn_icmp_timeout(timeout)

@vcgn_ns.route('/set_vcgn_inside/<string:inside_intfc>/<string:outside_intfc>')
class SetVcgnInside(Resource):
    def post(self, inside_intfc, outside_intfc):
        return vcgn_client.set_vcgn_inside(inside_intfc, outside_intfc)

@vcgn_ns.route('/set_vcgn_map/<string:lo_address>')
class SetVcgnMap(Resource):
    @vcgn_ns.doc(params={'hi_address': 'Hi Address'})
    def post(self, lo_address):
        hi_address = request.json.get('hi_address')
        return vcgn_client.set_vcgn_map(lo_address, hi_address)

@vcgn_ns.route('/set_vcgn_nfv9_logging_config/<string:inside_intfc>/<string:server_ip>/<int:port>')
class SetVcgnNfv9LoggingConfig(Resource):
    @vcgn_ns.doc(params={
        'refresh_rate': 'Refresh Rate',
        'timeout': 'Timeout',
        'pmtu': 'PMTU',
        'del_flag': 'Delete Flag'
    })
    def post(self, inside_intfc, server_ip, port):
        refresh_rate = request.json.get('refresh_rate')
        timeout = request.json.get('timeout')
        pmtu = request.json.get('pmtu')
        del_flag = request.json.get('del_flag', False)
        return vcgn_client.set_vcgn_nfv9_logging_config(inside_intfc, server_ip, port, refresh_rate, timeout, pmtu, del_flag)

@vcgn_ns.route('/set_vcgn_port_limit/<int:port_limit>')
class SetVcgnPortLimit(Resource):
    def post(self, port_limit):
        return vcgn_client.set_vcgn_port_limit(port_limit)

@vcgn_ns.route('/set_vcgn_tcp_timeout/<int:active_timeout>/<int:init_timeout>')
class SetVcgnTcpTimeout(Resource):
    def post(self, active_timeout, init_timeout):
        return vcgn_client.set_vcgn_tcp_timeout(active_timeout, init_timeout)

@vcgn_ns.route('/set_vcgn_udp_timeout/<int:active_timeout>/<int:init_timeout>')
class SetVcgnUdpTimeout(Resource):
    def post(self, active_timeout, init_timeout):
        return vcgn_client.set_vcgn_udp_timeout(active_timeout, init_timeout)

@vcgn_ns.route('/show_vcgn_config')
class ShowVcgnConfig(Resource):
    def get(self):
        return vcgn_client.show_vcgn_config()

@vcgn_ns.route('/show_vcgn_inside_translation/<string:protocol>/<string:inside_if>/<string:inside_addr>')
class ShowVcgnInsideTranslation(Resource):
    @vcgn_ns.doc(params={'start_port': 'Start Port', 'end_port': 'End Port'})
    def get(self, protocol, inside_if, inside_addr):
        start_port = request.args.get('start_port')
        end_port = request.args.get('end_port')
        return vcgn_client.show_vcgn_inside_translation(protocol, inside_if, inside_addr, start_port, end_port)

@vcgn_ns.route('/show_vcgn_outside_translation/<string:protocol>/<string:outside_if>/<string:outside_addr>')
class ShowVcgnOutsideTranslation(Resource):
    @vcgn_ns.doc(params={'start_port': 'Start Port', 'end_port': 'End Port'})
    def get(self, protocol, outside_if, outside_addr):
        start_port = request.args.get('start_port')
        end_port = request.args.get('end_port')
        return vcgn_client.show_vcgn_outside_translation(protocol, outside_if, outside_addr, start_port, end_port)

@vcgn_ns.route('/show_vcgn_statistics')
class ShowVcgnStatistics(Resource):
    def get(self):
        return vcgn_client.show_vcgn_statistics()


# VPP
@vpp_app_ns.route('/ip-sticky-classify')
class IPStickyClassify(Resource):
    @api.expect(command_model)
    def post(self):
        try:
            data = request.json
            command = data.get('command', 'ip sticky classify')
            stdout, stderr = vpp_app_commands.ip_sticky_classify(command)
            return {'stdout': stdout, 'stderr': stderr}
        except Exception as e:
            logging.exception(f"Error executing IP Sticky Classify command: {e}")
            return {'error': str(e)}, 500

# Example endpoint for 'show_sticky_classify'
@vpp_app_ns.route('/show-sticky-classify')
class ShowStickyClassify(Resource):
    @api.expect(command_model)
    def post(self):
        try:
            data = request.json
            command = data.get('command', 'show sticky classify')
            stdout, stderr = vpp_app_commands.show_sticky_classify(command)
            return {'stdout': stdout, 'stderr': stderr}
        except Exception as e:
            logging.exception(f"Error executing Show Sticky Classify command: {e}")
            return {'error': str(e)}, 500

# Example endpoint for 'show_version'
@vpp_app_ns.route('/show-version')
class ShowVersion(Resource):
    @api.expect(command_model)
    def post(self):
        try:
            data = request.json
            command = data.get('command', 'show version')
            stdout, stderr = vpp_app_commands.show_version(command)
            return {'stdout': stdout, 'stderr': stderr}
        except Exception as e:
            logging.exception(f"Error executing Show Version command: {e}")
            return {'error': str(e)}, 500

# Example endpoint for 'ip_virtual'
@vpp_app_ns.route('/ip-virtual')
class IPVirtual(Resource):
    @api.expect(command_model)
    def post(self):
        try:
            data = request.json
            command = data.get('command', 'ip virtual')
            stdout, stderr = vpp_app_commands.ip_virtual(command)
            return {'stdout': stdout, 'stderr': stderr}
        except Exception as e:
            logging.exception(f"Error executing IP Virtual command: {e}")
            return {'error': str(e)}, 500


@oam_ns.route('/execute-oam')
class ExecuteOAM(Resource):
    @api.expect(fields.String(required=True, description='Command to execute'))
    def post(self):
        try:
            data = request.json
            command = data.get('command')
            vpp_oam = VPPOAMCommands()
            stdout, stderr = vpp_oam.oam() if command == 'oam' else vpp_oam.show_oam()
            return {'stdout': stdout, 'stderr': stderr}, 200
        except Exception as e:
            logging.exception(f"Error executing OAM command: {e}")
            return {'error': str(e)}, 500


@vpp_commands_ns.route('/show-arp-event-registrations')
class ShowARPEventRegistrations(Resource):
    def get(self):
        try:
            vpp_client = VPPClientVppApi()
            stdout, stderr = vpp_client.show_arp_event_registrations()
            return {'stdout': stdout, 'stderr': stderr}, 200
        except Exception as e:
            logging.exception(f"Error executing Show ARP Event Registrations command: {e}")
            return {'error': str(e)}, 500

@vpp_commands_ns.route('/set-significant-error/<int:error_code>')
class SetSignificantError(Resource):
    def post(self, error_code):
        try:
            vpp_client = VPPClientVppApi()
            stdout, stderr = vpp_client.set_significant_error(error_code)
            return {'stdout': stdout, 'stderr': stderr}, 200
        except Exception as e:
            logging.exception(f"Error executing Set Significant Error command: {e}")
            return {'error': str(e)}, 500




if __name__ == '__main__':
    app.run(debug=True)
