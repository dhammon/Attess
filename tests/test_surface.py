
import unittest
import sys
import datetime
from dateutil.tz import tzutc
sys.path.insert(0, '../attess')
from attess.surface import Surface
from io import StringIO
from contextlib import redirect_stdout


class TestSurface(unittest.TestCase):

    def test_get_surface(self):
        f = StringIO()
        with redirect_stdout(f):
            actual = Surface.get_surface('us-east-1')
        result = f.getvalue()
        self.assertIn("[", result)
        self.assertIn("]", result)

        
    def test_validate_region_true(self):
        region = 'us-east-1'
        expected = None
        actual = Surface.validate_region(region)
        self.assertEqual(expected, actual)


    def test_validate_region_all(self):
        region = 'all'
        expected = None
        actual = Surface.validate_region(region)
        self.assertEqual(expected, actual)


    def test_validate_region_exception(self):
        region = 'lol'
        f = StringIO()
        with redirect_stdout(f):
            self.assertRaises(Exception, Surface.validate_region(region))


    def test_get_ec2_ips_all(self):
        f = StringIO()
        with redirect_stdout(f):
            region = 'all'
            actual = Surface.get_ec2_ips(region)
            self.assertTrue(isinstance(actual, list))

    
    def test_get_ec2_ips_single(self):
        region = 'us-east-1'
        actual = Surface.get_ec2_ips(region)
        self.assertTrue(isinstance(actual, list))


    def test_search_instances_true(self):
        region = 'us-east-1'
        public_ec2 = []
        actual = Surface.search_instances(region, public_ec2)
        self.assertTrue(isinstance(actual, list))


    def test_search_instances_exception(self):
        region = 'us-east-1'
        public_ec2 = []
        f = StringIO()
        with redirect_stdout(f):
            self.assertRaises(Exception, Surface.search_instances(region, public_ec2))


    def test_handle_ec2_reservations_positive(self):
        reservations = {'Reservations': [{'Groups': [], 'Instances': [{'AmiLaunchIndex': 0, 'ImageId': 'ami-04a81a99f5ec58529', 'InstanceId': 'i-03bf14927fbcef4e9', 'InstanceType': 't2.micro', 'LaunchTime': datetime.datetime(2024, 8, 18, 13, 39, 39, tzinfo=tzutc()), 'Monitoring': {'State': 'disabled'}, 'Placement': {'AvailabilityZone': 'us-east-1b', 'GroupName': '', 'Tenancy': 'default'}, 'PrivateDnsName': 'ip-172-31-29-216.ec2.internal', 'PrivateIpAddress': '172.31.29.216', 'ProductCodes': [], 'PublicDnsName': 'ec2-3-208-23-157.compute-1.amazonaws.com', 'PublicIpAddress': '3.208.23.157', 'State': {'Code': 16, 'Name': 'running'}, 'StateTransitionReason': '', 'SubnetId': 'subnet-09f2f5f5cf01c66fa', 'VpcId': 'vpc-0986f4e1e97edda89', 'Architecture': 'x86_64', 'BlockDeviceMappings': [{'DeviceName': '/dev/sda1', 'Ebs': {'AttachTime': datetime.datetime(2024, 8, 18, 13, 39, 40, tzinfo=tzutc()), 'DeleteOnTermination': True, 'Status': 'attached', 'VolumeId': 'vol-0cc99ce88983c0ec7'}}], 'ClientToken': '4423eb8a-7752-4e8d-9e93-0c672e6a12a4', 'EbsOptimized': False, 'EnaSupport': True, 'Hypervisor': 'xen', 'NetworkInterfaces': [{'Association': {'IpOwnerId': 'amazon', 'PublicDnsName': 'ec2-3-208-23-157.compute-1.amazonaws.com', 'PublicIp': '3.208.23.157'}, 'Attachment': {'AttachTime': datetime.datetime(2024, 8, 18, 13, 39, 39, tzinfo=tzutc()), 'AttachmentId': 'eni-attach-04faee857c01cdf93', 'DeleteOnTermination': True, 'DeviceIndex': 0, 'Status': 'attached', 'NetworkCardIndex': 0}, 'Description': '', 'Groups': [{'GroupName': 'default', 'GroupId': 'sg-0c400e99cef582922'}], 'Ipv6Addresses': [], 'MacAddress': '0a:ff:e3:30:ce:8f', 'NetworkInterfaceId': 'eni-0766d9bc8ed9646ff', 'OwnerId': '134672723840', 'PrivateDnsName': 'ip-172-31-29-216.ec2.internal', 'PrivateIpAddress': '172.31.29.216', 'PrivateIpAddresses': [{'Association': {'IpOwnerId': 'amazon', 'PublicDnsName': 'ec2-3-208-23-157.compute-1.amazonaws.com', 'PublicIp': '3.208.23.157'}, 'Primary': True, 'PrivateDnsName': 'ip-172-31-29-216.ec2.internal', 'PrivateIpAddress': '172.31.29.216'}], 'SourceDestCheck': True, 'Status': 'in-use', 'SubnetId': 'subnet-09f2f5f5cf01c66fa', 'VpcId': 'vpc-0986f4e1e97edda89', 'InterfaceType': 'interface'}], 'RootDeviceName': '/dev/sda1', 'RootDeviceType': 'ebs', 'SecurityGroups': [{'GroupName': 'default', 'GroupId': 'sg-0c400e99cef582922'}], 'SourceDestCheck': True, 'Tags': [{'Key': 'Name', 'Value': 'test1'}], 'VirtualizationType': 'hvm', 'CpuOptions': {'CoreCount': 1, 'ThreadsPerCore': 1}, 'CapacityReservationSpecification': {'CapacityReservationPreference': 'open'}, 'HibernationOptions': {'Configured': False}, 'MetadataOptions': {'State': 'applied', 'HttpTokens': 'required', 'HttpPutResponseHopLimit': 2, 'HttpEndpoint': 'enabled', 'HttpProtocolIpv6': 'disabled'}, 'EnclaveOptions': {'Enabled': False}, 'BootMode': 'uefi-preferred', 'PlatformDetails': 'Linux/UNIX', 'UsageOperation': 'RunInstances', 'UsageOperationUpdateTime': datetime.datetime(2024, 8, 18, 13, 39, 39, tzinfo=tzutc())}], 'OwnerId': '134672723840', 'ReservationId': 'r-051071fb090885460'}, {'Groups': [], 'Instances': [{'AmiLaunchIndex': 0, 'ImageId': 'ami-04a81a99f5ec58529', 'InstanceId': 'i-072cf44f3c79226e1', 'InstanceType': 't2.micro', 'LaunchTime': datetime.datetime(2024, 8, 18, 13, 40, 7, tzinfo=tzutc()), 'Monitoring': {'State': 'disabled'}, 'Placement': {'AvailabilityZone': 'us-east-1b', 'GroupName': '', 'Tenancy': 'default'}, 'PrivateDnsName': 'ip-172-31-20-252.ec2.internal', 'PrivateIpAddress': '172.31.20.252', 'ProductCodes': [], 'PublicDnsName': '', 'State': {'Code': 16, 'Name': 'running'}, 'StateTransitionReason': '', 'SubnetId': 'subnet-09f2f5f5cf01c66fa', 'VpcId': 'vpc-0986f4e1e97edda89', 'Architecture': 'x86_64', 'BlockDeviceMappings': [{'DeviceName': '/dev/sda1', 'Ebs': {'AttachTime': datetime.datetime(2024, 8, 18, 13, 40, 7, tzinfo=tzutc()), 'DeleteOnTermination': True, 'Status': 'attached', 'VolumeId': 'vol-0663ba71cb6b552ad'}}], 'ClientToken': 'cdb6a770-8d39-4ae3-9938-1843dd54f5db', 'EbsOptimized': False, 'EnaSupport': True, 'Hypervisor': 'xen', 'NetworkInterfaces': [{'Attachment': {'AttachTime': datetime.datetime(2024, 8, 18, 13, 40, 7, tzinfo=tzutc()), 'AttachmentId': 'eni-attach-002edd414f1ac01be', 'DeleteOnTermination': True, 'DeviceIndex': 0, 'Status': 'attached', 'NetworkCardIndex': 0}, 'Description': '', 'Groups': [{'GroupName': 'default', 'GroupId': 'sg-0c400e99cef582922'}], 'Ipv6Addresses': [], 'MacAddress': '0a:ff:f4:ae:8a:0d', 'NetworkInterfaceId': 'eni-01a10874284ebd0c9', 'OwnerId': '134672723840', 'PrivateDnsName': 'ip-172-31-20-252.ec2.internal', 'PrivateIpAddress': '172.31.20.252', 'PrivateIpAddresses': [{'Primary': True, 'PrivateDnsName': 'ip-172-31-20-252.ec2.internal', 'PrivateIpAddress': '172.31.20.252'}], 'SourceDestCheck': True, 'Status': 'in-use', 'SubnetId': 'subnet-09f2f5f5cf01c66fa', 'VpcId': 'vpc-0986f4e1e97edda89', 'InterfaceType': 'interface'}], 'RootDeviceName': '/dev/sda1', 'RootDeviceType': 'ebs', 'SecurityGroups': [{'GroupName': 'default', 'GroupId': 'sg-0c400e99cef582922'}], 'SourceDestCheck': True, 'Tags': [{'Key': 'Name', 'Value': 'test2'}], 'VirtualizationType': 'hvm', 'CpuOptions': {'CoreCount': 1, 'ThreadsPerCore': 1}, 'CapacityReservationSpecification': {'CapacityReservationPreference': 'open'}, 'HibernationOptions': {'Configured': False}, 'MetadataOptions': {'State': 'applied', 'HttpTokens': 'required', 'HttpPutResponseHopLimit': 2, 'HttpEndpoint': 'enabled', 'HttpProtocolIpv6': 'disabled'}, 'EnclaveOptions': {'Enabled': False}, 'BootMode': 'uefi-preferred', 'PlatformDetails': 'Linux/UNIX', 'UsageOperation': 'RunInstances', 'UsageOperationUpdateTime': datetime.datetime(2024, 8, 18, 13, 40, 7, tzinfo=tzutc())}], 'OwnerId': '134672723840', 'ReservationId': 'r-0007c54d5e52d20f8'}], 'ResponseMetadata': {'RequestId': '83a7e2a6-e23f-4902-80cf-9e453955c338', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '83a7e2a6-e23f-4902-80cf-9e453955c338', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'vary': 'accept-encoding', 'content-type': 'text/xml;charset=UTF-8', 'transfer-encoding': 'chunked', 'date': 'Sun, 18 Aug 2024 13:47:22 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}
        public_ec2 = []
        expected = ['3.208.23.157']
        actual = Surface.handle_ec2_reservations(reservations, public_ec2)
        self.assertEqual(expected, actual)


    def test_handle_ec2_reservations_none(self):
        reservations = []
        public_ec2 = []
        expected = []
        actual = Surface.handle_ec2_reservations(reservations, public_ec2)
        self.assertEqual(expected, actual)


    def test_handle_ec2_reservations_exception(self):
        f = StringIO()
        with redirect_stdout(f):
            reservations = "abc"
            public_ec2 = []
            self.assertRaises(Exception, Surface.handle_ec2_reservations(reservations, public_ec2))