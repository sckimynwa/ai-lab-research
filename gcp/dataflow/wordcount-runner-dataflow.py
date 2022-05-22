from __future__ import print_function
import re
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

pipeline_options = PipelineOptions(
  project='playground-yeoul-bb70',
  runner='DataflowRunner',
  region='us-east1',
  temp_location='gs://dataflow-test-yeoul/tmp'
)

def flat_map(word):
  return re.split("\\W+", word)

def format_result(word_count):
  (word, count) = word_count
  return '%s: %s' % (word, count)

with beam.Pipeline(options=pipeline_options) as p:
  p | 'Read' >> beam.io.ReadFromText("gs://dataflow-test-yeoul/lover.txt") \
    | 'Extract' >> beam.FlatMap(flat_map) \
    | 'Count' >> beam.combiners.Count.PerElement() \
    | 'Map' >> beam.Map(format_result) \
    | 'Save' >> beam.io.textio.WriteToText("gs://dataflow-test-yeoul/results/output")
    