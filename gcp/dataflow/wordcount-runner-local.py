from __future__ import print_function
import re
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

pipeline_options = PipelineOptions(
  project='playground-yeoul-bb70',
  runner='DirectRunner',
)

with beam.Pipeline(options=pipeline_options) as p:
  p | 'Read' >> beam.io.ReadFromText("../lover.txt") \
    | 'Extract' >> beam.FlatMap(lambda s: re.split("\\W+", s)) \
    | 'Count' >> beam.combiners.Count.PerElement() \
    | 'Map' >> beam.Map(lambda w, c: "%s: %d" % (w, c)) \
    | 'Save' >> beam.io.textio.WriteToText("../lover-output.txt")

# Script
# python3 -m apache_beam.examples.wordcount \
# --input lover.txt  --output output.txt