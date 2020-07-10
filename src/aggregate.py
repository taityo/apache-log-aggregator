from abc import ABCMeta, abstractmethod
from datetime import datetime

class AccessAggregator(metaclass=ABCMeta):
    def __init__(self):
        super().__init__()
        self.result = {}
        
    def get_result(self):
        return self.result
   
    def set_term(self, first, secound):
        #first_day = [int(x) for x in first.split("/")]
        #secound_day = [int(x) for x in secound.split("/")]
        self.first = first
        self.secound = secound

    @abstractmethod 
    def aggregate(self, log_data_list):
        pass
    
class TimeAccessAggregator(AccessAggregator):
    def aggregate(self, log_data_list):
        for log_data in log_data_list:
            if ("first" not in vars(self).keys()) or (self.first <= log_data.time <= self.secound):
                if log_data.time in self.result.keys():
                    self.result[log_data.time] += 1
                else:
                    self.result[log_data.time] = 1
    
class RemoteHostAccessAggregator(AccessAggregator):
    def aggregate(self, log_data_list):
        for log_data in log_data_list:
            if ("first" not in vars(self).keys()) or (self.first <= log_data.time <= self.secound):
                if log_data.remote_host in self.result.keys():
                    self.result[log_data.remote_host] += 1
                else:
                    self.result[log_data.remote_host] = 1
    