#!/usr/bin/env python

import boto.ec2
import sys

def main():
    conn = boto.ec2.connect_to_region("us-west-2")
    conn.run_instances('ami-8ef297be', min_count=sys.argv[1], max_count=sys.argv[1])

if __name__=="__main__":
    main()


