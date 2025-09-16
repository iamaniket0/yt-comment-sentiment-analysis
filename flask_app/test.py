from mlflow.tracking import MlflowClient
import mlflow

# Connect to MLflow tracking server
mlflow.set_tracking_uri("http://ec2-13-218-248-178.compute-1.amazonaws.com:5000/")  # your MLflow server
client = MlflowClient()

# List all registered models
for rm in client.search_registered_models():
    print(rm.name)

