#!/usr/bin/env python

import boto.emr
from boto.emr.step import StreamingStep

def main():
    conn = boto.emr.connect_to_region('us-west-2')
    word_count_step = StreamingStep(
        name    ='Wordcount sort',
        mapper  ='s3://raresreligion/freq_mapper.py',
        reducer ='s3://raresreligion/freq_reducer.py',
        input   ='s3://raresreligion/wordcount_output',
        output  ='s3://raresreligion/output'
    )
    jobid = conn.run_jobflow(
        name    ='Frequent words in sacred texts',
        log_uri ='s3://raresreligion/jobflow_logs',
        steps   =[word_count_step]
    )

if __name__=="__main__":
    main()
