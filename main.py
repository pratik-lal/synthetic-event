from syntheticevent import SyntheticEvent
from logger import logger
import socket
import datetime


class MainProgram:
    @staticmethod
    def main():
        # Actual arguments for constructor - class syntheticevent
        event_init_time = datetime.datetime.now()
        event_start_time = event_init_time.strftime("%b %d %H:%M:%S")
        event_host_name = socket.gethostname()
        event_syslog_priority = "<999>"
        synthetic_event_name = "Sentinel Synthetic Event"
        event_provider_name = "LogAnalyticsAgent"

        # Class object
        sentinel_synthetic_event = SyntheticEvent(event_init_time, event_start_time, event_host_name,
                                                  event_syslog_priority, synthetic_event_name, event_provider_name)

        # Actual arguments for method synthetic_event_generator - class syntheticevent
        netcat_ip = "127.0.0.1"
        netcat_port = 25224

        try:
            sentinel_synthetic_event.synthetic_event_generator(netcat_ip, netcat_port)
        except Exception as e:
            logger.error("Error in main program. Unable to generate syslog - synthetic event.", exc_info=True)
            logger.error(e)


if __name__ == '__main__':
    MainProgram.main()


