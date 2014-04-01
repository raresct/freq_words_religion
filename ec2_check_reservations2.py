#!/usr/bin/env python

import boto.ec2

def main():
    conn = boto.ec2.connect_to_region("us-west-2")
    reservations = conn.get_all_reservations()
    print reservations
    print [r.instances for r in reservations]
    print [i.public_dns_name for r in reservations for i in r.instances]

if __name__=="__main__":
    main()
