#!/usr/bin/env python

import boto.ec2

def main():
    conn = boto.ec2.connect_to_region("us-west-2")
    reservations = conn.get_all_reservations()   
    instances = [i for r in reservations for i in r.instances]
    instance_ids = [i.id for i in instances]
    if instances:
        conn.terminate_instances(instance_ids=instance_ids)

if __name__=="__main__":
    main()
