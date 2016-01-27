import logging

from raven import Client
from loggerglue.server import SyslogServer, SyslogHandler

client = Client(dsn='<your dsn here>')

PRIVAL_SEVERITY = {
    0 : logging.CRITICAL,
    1 : logging.CRITICAL,
    2 : logging.CRITICAL,
    3 : logging.ERROR,
    4 : logging.WARNING,
    5 : logging.INFO,
    6 : logging.INFO,
    7 : logging.DEBUG,
}

PRIVAL_FACILITY = {
    0 : "LOG_KERN",
    1 : "LOG_USER",
    2 : "LOG_MAIL",
    3 : "LOG_DAEMON",
    4 : "LOG_AUTH",
    5 : "LOG_SYSLOG",
    6 : "LOG_LPR",
    7 : "LOG_NEWS",
    8 : "LOG_UUCP",
    9 : "LOG_CRON",
    10 : "LOG_AUTHPRIV",
    16 : "LOG_LOCAL0",
    17 : "LOG_LOCAL1",
    18 : "LOG_LOCAL2",
    19 : "LOG_LOCAL3",
    20 : "LOG_LOCAL4",
    21 : "LOG_LOCAL5",
    22 : "LOG_LOCAL6",
    23 : "LOG_LOCAL7",
}

def prival(prival):
    sev_num = prival % 8
    fac_num = (prival - sev_num) / 8
    return (PRIVAL_SEVERITY[sev_num], PRIVAL_FACILITY[fac_num])

class SimpleHandler(SyslogHandler):
    def handle_entry(self, entry):
        level, fac = prival(entry.prival)
        client.name = entry.hostname

        data = {'level': level, "culprit" : ".".join([fac, entry.app_name]),
                'logger' : ".".join([fac, entry.app_name])}

        client.capture('Message', message=entry.msg,
                            date=entry.timestamp, data=data)


s = SyslogServer(('192.168.0.1', 10514), SimpleHandler)
s.serve_forever()