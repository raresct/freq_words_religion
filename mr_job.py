#!/usr/bin/env python

import sys
import boto.emr
from boto.emr.step import StreamingStep

def main():
    conn = boto.emr.connect_to_region('us-west-2')
    word_count_step = StreamingStep(
        name    ='Word count',
        mapper  ='s3://raresreligion/count_mapper.py',
        reducer ='s3://raresreligion/count_reducer.py',
        input   ='s3://raresreligion/input',
        output  ='s3://raresreligion/wordcount_output'
    )
    jobid = conn.run_jobflow(
        name    ='Frequent words in sacred texts',
        log_uri ='s3://raresreligion/jobflow_logs',
        steps   =[word_count_step],
        num_instances=sys.argv[1]
    )

if __name__=="__main__":
    main()
