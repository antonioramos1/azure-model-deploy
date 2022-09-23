from azureml.core import Workspace
from azureml.core.compute import AksCompute, ComputeTarget

AKS_NAME = "AntonioAksModel"
ws = Workspace.from_config()
prov_cfg = AksCompute.provisioning_configuration()
aks = ComputeTarget.create(workspace=ws, name=AKS_NAME, provisioning_configuration=prov_cfg)
