from abc import ABCMeta, abstractmethod

class AccessAggregator(metaclass=ABCMeta):
    def __init__(self):
        super().__init__()
        self.result = {}
        
    def get_result(self):
        return self.result
   
    def set_term(self, first, secound):
        self.first = first
        self.secound = secound

    @abstractmethod 
    def aggregate(self, log_data_list):
        pass
    
class TimeAccessAggregator(AccessAggregator):
    def aggregate(self, log_data_list):
        for log_data in log_data_list:
            if ("first" not in vars(self).keys()) or (self.first <= log_data.time and log_data <= self.secound):
                if log_data.time in self.result.keys():
                    self.result[log_data.time] += 1
                else:
                    self.result[log_data.time] = 1
    
class RemoteHostAccessAggregator(AccessAggregator):
    def aggregate(self, log_data_list):
        for log_data in log_data_list:
            if ("first" not in vars(self).keys()) or (self.first <= log_data.time and log_data <= self.secound):
                if log_data.remote_host in self.result.keys():
                    self.result[log_data.remote_host] += 1
                else:
                    self.result[log_data.remote_host] = 1
    