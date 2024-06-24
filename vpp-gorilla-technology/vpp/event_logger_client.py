import logging
from command import VPPCommand

# Configure logging
logging.basicConfig(filename='logs/vpppy.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class EventLoggerClient:
    def __init__(self):
        self.vpp_command = VPPCommand()
        self.logger = logging.getLogger(__name__)

    def run_vpp_command(self, command):
        return self.vpp_command.run_vpp_command(command)

    ### Event Logger Commands ###

    def clear_event_log(self):
        command = 'event-logger clear'
        return self.run_vpp_command(command)

    def resize_event_log(self, size):
        command = f'event-logger resize {size}'
        return self.run_vpp_command(command)

    def restart_event_logger(self):
        command = 'event-logger restart'
        return self.run_vpp_command(command)

    def save_event_log(self, filename):
        command = f'event-logger save {filename}'
        return self.run_vpp_command(command)

    def stop_event_logger(self):
        command = 'event-logger stop'
        return self.run_vpp_command(command)

    def show_event_logger_info(self):
        command = 'show event-logger'
        return self.run_vpp_command(command)

        