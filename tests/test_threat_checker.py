# import unittest
# # from network_intelligence.connectors.abuseipdb_connector \
# # import AbuseIPDBConnector
# from network_intelligence.threat_checker import check_ips
#
#
# class MockConnector:
#     def check_ip(self, ip):
#         return {'data': {'totalReports': 0}}
#
#
# class TestThreatChecker(unittest.TestCase):
#     def test_check_ips(self):
#         connector = MockConnector()
#         ips = ['8.8.8.8', '1.1.1.1']
#         results = check_ips(connector, ips)
#         for ip in ips:
#             self.assertIn('data', results[ip])
#             self.assertIn('totalReports', results[ip]['data'])
#
#
# if __name__ == '__main__':
#     unittest.main()
