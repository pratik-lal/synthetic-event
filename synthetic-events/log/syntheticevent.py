import os
import datetime
import socket


class SyntheticEvent:
    # constructor
    def __init__(self, init_time, start_time, host_name, syslog_priority, event_name, provider_name):
        self.init_time = init_time
        self.start_time = start_time
        self.host_name = host_name
        self.syslog_priority = syslog_priority
        self.event_name = event_name
        self.provider_name = provider_name

    '''
    Generate synthetic event using netcat command and send as synthetic-event message to local ip address and port number.
    IP address should be loopback address i.e. 127.0.0.1 in most of the cases.
    Check oms agent configuration file for synthetic-event port number. 
    We're using tcp protocol with synthetic-event by default. use  nc -u for udp if needed.
    '''
    def synthetic_event_generator(self, ip_address, port_number):
        synthetic_event_message = str(self.syslog_priority + self.start_time
                                      + " " + self.host_name
                                      + " " + self.provider_name
                                      + " " + self.event_name)
        # Example: syslog_command = "echo '{}' | nc -q 1 127.0.0.1 25224" .format(synthetic_event_message)
        syslog_command = "echo '{}' | nc -q 1 '{}' '{}'".format(synthetic_event_message, ip_address, port_number)
        try:
            synthetic_event_syslog = os.system(syslog_command)
            print("Syslog message has been sent. Exit code: {}" .format(synthetic_event_syslog))
            return synthetic_event_syslog
        except Exception as e:
            print(e)


# Actual arguments for constructor
event_init_time = datetime.datetime.now()
event_start_time = event_init_time.strftime("%b %d %H:%M:%S")
event_host_name = socket.gethostname()
event_syslog_priority = "<999>"
synthetic_event_name = "Sentinel Synthetic Event"
event_provider_name = "LogAnalyticsAgent"

# Class object
SentinelSyntheticEvent = SyntheticEvent(event_init_time, event_start_time, event_host_name, event_syslog_priority,
                                        synthetic_event_name, event_provider_name)

# Actual arguments for method synthetic_event_generator
netcat_ip = "127.0.0.1"
netcat_port = 25224

# Calling synthetic_event_generator() method.
SentinelSyntheticEvent.synthetic_event_generator(netcat_ip, netcat_port)
