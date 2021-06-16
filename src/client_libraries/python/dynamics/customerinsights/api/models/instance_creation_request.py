# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class InstanceCreationRequest(Model):
    """InstanceCreationRequest.

    :param instance_metadata:
    :type instance_metadata:
     ~dynamics.customerinsights.api.models.InstanceMetadata
    :param byosa_resource_metadata:
    :type byosa_resource_metadata:
     ~dynamics.customerinsights.api.models.ResourceMetadata
    :param cds_resource_metadata:
    :type cds_resource_metadata:
     ~dynamics.customerinsights.api.models.ResourceMetadata
    :param byo_pbi_provisioning_info:
    :type byo_pbi_provisioning_info:
     ~dynamics.customerinsights.api.models.ByoPbiProvisioningInfo
    :param is_cds_mdl_storage_enabled:
    :type is_cds_mdl_storage_enabled: bool
    :param is_ci_to_byosa_migration_enabled:
    :type is_ci_to_byosa_migration_enabled: bool
    :param bap_provisioning_type: Possible values include: 'skip', 'create',
     'attach'
    :type bap_provisioning_type: str or
     ~dynamics.customerinsights.api.models.enum
    :param is_pbi_provisioning_required:
    :type is_pbi_provisioning_required: bool
    """

    _attribute_map = {
        'instance_metadata': {'key': 'instanceMetadata', 'type': 'InstanceMetadata'},
        'byosa_resource_metadata': {'key': 'byosaResourceMetadata', 'type': 'ResourceMetadata'},
        'cds_resource_metadata': {'key': 'cdsResourceMetadata', 'type': 'ResourceMetadata'},
        'byo_pbi_provisioning_info': {'key': 'byoPbiProvisioningInfo', 'type': 'ByoPbiProvisioningInfo'},
        'is_cds_mdl_storage_enabled': {'key': 'isCdsMdlStorageEnabled', 'type': 'bool'},
        'is_ci_to_byosa_migration_enabled': {'key': 'isCiToByosaMigrationEnabled', 'type': 'bool'},
        'bap_provisioning_type': {'key': 'bapProvisioningType', 'type': 'str'},
        'is_pbi_provisioning_required': {'key': 'isPbiProvisioningRequired', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(InstanceCreationRequest, self).__init__(**kwargs)
        self.instance_metadata = kwargs.get('instance_metadata', None)
        self.byosa_resource_metadata = kwargs.get('byosa_resource_metadata', None)
        self.cds_resource_metadata = kwargs.get('cds_resource_metadata', None)
        self.byo_pbi_provisioning_info = kwargs.get('byo_pbi_provisioning_info', None)
        self.is_cds_mdl_storage_enabled = kwargs.get('is_cds_mdl_storage_enabled', None)
        self.is_ci_to_byosa_migration_enabled = kwargs.get('is_ci_to_byosa_migration_enabled', None)
        self.bap_provisioning_type = kwargs.get('bap_provisioning_type', None)
        self.is_pbi_provisioning_required = kwargs.get('is_pbi_provisioning_required', None)
