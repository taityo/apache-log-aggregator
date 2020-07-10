from abc import ABCMeta, abstractmethod
import apache_log_parser as alp

class LogData():
    time_format = "%Y/%m/%d %H:%M:%S"
    
    # timeは"%Y/%m/%d %H:%M:%S"の形式で入力する
    def __init__(self, time, remote_host):
        self.time = time
        self.remote_host = remote_host

class LogDataFormatter(metaclass=ABCMeta):
    @abstractmethod
    def get_log_data(self, log_lines):
        return []
    
class ApatchLogDataFormatter(LogDataFormatter):
    def __init__(self):
        self.apatch_parser = alp.make_parser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")

    def get_log_data(self, log_lines):
        log_data_list = []
        for log_line in log_lines:
            parsed_log_line = self.apatch_parser(log_line)
            log_data = LogData(parsed_log_line["time_received_datetimeobj"].strftime(LogData.time_format), 
                               parsed_log_line["remote_host"])
            log_data_list.append(log_data)
            
        return log_data_list