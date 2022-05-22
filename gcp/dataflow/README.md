# Dataflow

## Prerequesits

1. install apache-beam

```
pip3 install apache-beam[gcp]
```

2. make sure you logged in as "Application Default"

```
gcloud auth application-default login
```

## Apache WordCount Examples

```
python3 -m \
    apache_beam.examples.wordcount \
    --region us-central1 \
    --input gs://dataflow-samples/shakespeare/kinglear.txt \
    --output gs://<YOUR_OUTPUT_FILE_PATH> \
    --runner DataflowRunner \
    --project <YOUR_PROJECT_NAME> \
    --temp_location gs://<YOUR_TEMP_LOCATION>
```

## WordCount Custom Code Examples

```

```

## Reference

- [GCP Workflow Guide](https://cloud.google.com/workflows/docs/how-to)
