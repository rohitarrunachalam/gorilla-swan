import logging
from command import VPPCommand

logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class VcgnClient:
    def __init__(self):
        self.vpp_command = VPPCommand()
        self.logger = logging.getLogger(__name__)

    def run_vpp_command(self, command):
        return self.vpp_command.run_vpp_command(command)

    ### VCGN Plugin Commands ###

    def set_vcgn_default_timeout(self, protocol):
        command = f'set vcgn default timeout protocol {protocol}'
        return self.run_vpp_command(command)

    def set_vcgn_dynamic_port_start(self, port_start):
        command = f'set vcgn dynamic port start {port_start}'
        return self.run_vpp_command(command)

    def set_vcgn_icmp_timeout(self, timeout):
        command = f'set vcgn icmp timeout {timeout}'
        return self.run_vpp_command(command)

    def set_vcgn_inside(self, inside_intfc, outside_intfc):
        command = f'set vcgn inside {inside_intfc} outside {outside_intfc}'
        return self.run_vpp_command(command)

    def set_vcgn_map(self, lo_address, hi_address=None):
        command = f'set vcgn map {lo_address}'
        if hi_address:
            command += f' - {hi_address}'
        return self.run_vpp_command(command)

    def set_vcgn_nfv9_logging_config(self, inside_intfc, server_ip, port, refresh_rate=None, timeout=None, pmtu=None, del_flag=False):
        command = 'set vcgn nfv9'
        if del_flag:
            command += ' del'
        command += f' inside {inside_intfc} server {server_ip} port {port}'
        if refresh_rate:
            command += f' refresh-rate {refresh_rate}'
        if timeout:
            command += f' timeout {timeout}'
        if pmtu:
            command += f' pmtu {pmtu}'
        return self.run_vpp_command(command)

    def set_vcgn_port_limit(self, port_limit):
        command = f'set vcgn port limit {port_limit}'
        return self.run_vpp_command(command)

    def set_vcgn_tcp_timeout(self, active_timeout, init_timeout):
        command = f'set vcgn tcp timeout active {active_timeout} init {init_timeout}'
        return self.run_vpp_command(command)

    def set_vcgn_udp_timeout(self, active_timeout, init_timeout):
        command = f'set vcgn udp timeout active {active_timeout} init {init_timeout}'
        return self.run_vpp_command(command)

    def show_vcgn_config(self):
        command = 'show vcgn config'
        return self.run_vpp_command(command)

    def show_vcgn_inside_translation(self, protocol, inside_if, inside_addr, start_port=None, end_port=None):
        command = f'show vcgn inside-translation protocol {protocol} interface {inside_if} inside-addr {inside_addr}'
        if start_port:
            command += f' start-port {start_port}'
        if end_port:
            command += f' end-port {end_port}'
        return self.run_vpp_command(command)

    def show_vcgn_outside_translation(self, protocol, outside_if, outside_addr, start_port=None, end_port=None):
        command = f'show vcgn outside-translation protocol {protocol} interface {outside_if} outside-addr {outside_addr}'
        if start_port:
            command += f' start-port {start_port}'
        if end_port:
            command += f' end-port {end_port}'
        return self.run_vpp_command(command)

    def show_vcgn_statistics(self):
        command = 'show vcgn statistics'
        return self.run_vpp_command(command)
