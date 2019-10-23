#!/usr/bin/env python

import sys
import boto3

action = sys.argv[1]
target = sys.argv[2]

metrics = boto3.resource('ec2')
instance = metrics.Instance(target)
client = boto3.client('ec2')

if action == "start":

    if instance.state['Name'] == "running":
        print("Already running!")
        sys.exit(0)
    else:
        waiter = client.get_waiter('instance_running')
        client.start_instances(InstanceIds=[target])
        waiter.wait(InstanceIds=[target])

elif action == "stop":

    if instance.state['Name'] == "stopped":
        print("Already stopped!")
        sys.exit(0)
    else:
        waiter = client.get_waiter('instance_stopped')
        client.stop_instances(InstanceIds=[target])
        waiter.wait(InstanceIds=[target])
else:
    print("ERROR Usage: commands.py start/stop instance-id")
    sys.exit(1)

