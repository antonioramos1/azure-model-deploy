from azureml.core import Workspace, Environment, Model
from azureml.core.model import InferenceConfig
from azureml.core.conda_dependencies import CondaDependencies
from azureml.core.webservice import AksWebservice
from azureml.core.compute import AksCompute, ComputeTarget

MODEL_NAME = "model"
ENVIRONMENT_NAME = "myenv"
AKS_NAME = "AntonioAksModel"
ENTRY_SCRIPT_NAME = "score.py"
WEB_SERVICE_NAME = "model-service-v8"

ws = Workspace.from_config()

model = Model(ws, MODEL_NAME)

packages = ["scikit-learn==1.1.2", "joblib==1.2.0", "azureml-defaults"]
myenv = Environment(name=ENVIRONMENT_NAME)
dependencies = CondaDependencies.create(pip_packages=packages)
myenv.python.conda_dependencies = dependencies

aks = ComputeTarget(workspace=ws, name=AKS_NAME)
inf_cfg = InferenceConfig(entry_script=ENTRY_SCRIPT_NAME, environment=myenv)
deploy_cfg = AksWebservice.deploy_configuration()

aks_service = Model.deploy(
    workspace=ws,
    name=WEB_SERVICE_NAME,
    models=[model],
    inference_config=inf_cfg,
    deployment_config=deploy_cfg,
    deployment_target=aks,
)
