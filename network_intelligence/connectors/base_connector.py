class BaseConnector:
    def check_ip(self, ip):
        raise NotImplementedError("Subclasses should implement this method")
