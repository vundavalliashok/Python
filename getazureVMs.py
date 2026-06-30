from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient


def list_azure_vms(subscription_id):
    credential = DefaultAzureCredential()
    compute_client = ComputeManagementClient(credential, subscription_id)

    for vm in compute_client.virtual_machines.list_all():
        print(f"Name: {vm.name}, Location: {vm.location}, Type: {vm.type}")


if __name__ == "__main__":
    subscription_id = "<YOUR_SUBSCRIPTION_ID>"
    list_azure_vms(subscription_id)
    