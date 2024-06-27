import logging
from vpp_papi import VPPApiClient

logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


class FlowClient:
    def __init__(self):
        self.vpp = VPPApiClient()
        self.vpp.connect('vpp_api_client')
        self.logger = logging.getLogger(__name__)

    def run_vpp_command(self, command, **params):
        self.logger.debug(f"Running command: {command} with parameters {params}")
        try:
            response = getattr(self.vpp.api, command)(**params)
            return response, None
        except AttributeError:
            error_msg = f"Command '{command}' not available in VPP API"
            self.logger.error(error_msg)
            return None, error_msg
        except Exception as e:
            self.logger.error(f"Error executing command {command}: {e}")
            return None, str(e)

    def set_ipfix(self, collector_ip, collector_port, src_ip=None, vrf_id=None, path_mtu=None):
        params = {
            'collector_ip': collector_ip,
            'collector_port': collector_port
        }
        if src_ip:
            params['src_ip'] = src_ip
        if vrf_id:
            params['vrf_id'] = vrf_id
        if path_mtu:
            params['path_mtu'] = path_mtu
        return self.run_vpp_command('set_ipfix', **params)

    def flow_classify(self, flow_name, match_criteria, action):
        params = {
            'flow_name': flow_name,
            'match_criteria': match_criteria,
            'action': action
        }
        return self.run_vpp_command('flow_classify', **params)


# Example usage
if __name__ == "__main__":
    flow_client = FlowClient()

    # Example: Set IPFIX collector
    response, error = flow_client.set_ipfix('192.168.1.1', 4739, src_ip='192.168.1.2', vrf_id=0, path_mtu=1500)
    if error:
        print(f"Error setting IPFIX collector: {error}")
    else:
        print(f"IPFIX collector set successfully: {response}")

    # Example: Flow classify
    response, error = flow_client.flow_classify('test_flow', 'src_ip 192.168.1.3', 'allow')
    if error:
        print(f"Error classifying flow: {error}")
    else:
        print(f"Flow classified successfully: {response}")

    # Add additional example usages as needed
