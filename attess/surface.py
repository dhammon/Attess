import boto3
import botocore
from sys import exit

#TODO https://github.com/SummitRoute/aws_exposable_resources
#api gateway
#cloudfront
#redshift
#rds
#ec2
#eip
#global accelerator?
#elb
#lightsail
#neptune?
#elasticCache
#emr


class Surface:

    #https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html
    regions = [
        'us-east-2',
        'us-east-1',
        'us-west-1',
        'us-west-2',
        'af-south-1',
        'ap-east-1',
        'ap-south-2',
        'ap-southeast-3',
        'ap-southeast-4',
        'ap-south-1',
        'ap-northeast-3',
        'ap-northeast-2',
        'ap-southeast-1',
        'ap-southeast-2',
        'ap-northeast-1',
        'ca-central-1',
        'ca-west-1',
        'eu-central-1',
        'eu-west-1',
        'eu-west-2',
        'eu-south-1',
        'eu-west-3',
        'eu-south-2',
        'eu-north-1',
        'eu-central-2',
        'il-central-1',
        'me-south-1',
        'me-central-1',
        'sa-east-1',
        'us-gov-east-1',
        'us-gov-west-1',

    ]

    
    def get_surface(region='all'):
        Surface.validate_region(region)
        public_ec2 = Surface.get_ec2_ips(region)
        #TODO better report/output
        print(public_ec2)
    

    def validate_region(region):
        if region not in Surface.regions or region == 'all':
            Exception("[-] Exception: Region not valid")


    def get_ec2_ips(region):
        public_ec2 = []
        if region == 'all':
            for list_region in Surface.regions:
                public_ec2 = Surface.search_instances(list_region, public_ec2)
        else:
            public_ec2 = Surface.search_instances(region, public_ec2)
        return public_ec2


    def search_instances(region, public_ec2):
        try:
            client = boto3.client('ec2', region_name=region)
            paginator = client.get_paginator('describe_instances')
            page_iterator = paginator.paginate()
            for page in page_iterator:
                Surface.handle_ec2_reservations(page, public_ec2)
            return public_ec2
        except botocore.exceptions.ClientError as error:
            #TODO verbose enable/disable
            print("[!] Client Error:", region, error)
            return public_ec2
        except:
            print("[-] Exception: Failed Getting EC2s")
            exit()


    def handle_ec2_reservations(reservations, public_ec2):
        try:
            if reservations == []:
                return public_ec2
            for reservation in reservations['Reservations']:
                if "PublicIpAddress" in reservation['Instances'][0]:
                    ip_address = reservation['Instances'][0]['PublicIpAddress']
                    public_ec2.append(ip_address)
            return public_ec2
        except:
            print("[-] Exception: Failed EC2 reservations inspection")


