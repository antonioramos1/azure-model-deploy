from azureml.core import Model

MODEL_PATH = "model.pkl"
MODEL_NAME = "model"
ws = Workspace.from_config()
Model.register(model_path=MODEL_PATH, model_name=MODEL_NAME, workspace=ws)
