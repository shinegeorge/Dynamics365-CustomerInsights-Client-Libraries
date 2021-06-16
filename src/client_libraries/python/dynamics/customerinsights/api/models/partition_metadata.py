# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PartitionMetadata(Model):
    """Represents a DCI entity data partition.

    :param name: Gets the name of the data partition
    :type name: str
    :param location: Gets the uri location of the data
    :type location: str
    :param refresh_time: Gets the refresh time of the data partition
    :type refresh_time: datetime
    :param file_format_settings:
    :type file_format_settings: object
    :param is_ci_generated: Gets a value indicating whether a partition is CI
     Generated or not.
    :type is_ci_generated: bool
    :param force_sas_auth: Gets a value indicating whether a partition need to
     be forced for SAS authentication.
    :type force_sas_auth: bool
    :param has_header: Flag to represent header presence (if any)
    :type has_header: bool
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'refresh_time': {'key': 'refreshTime', 'type': 'iso-8601'},
        'file_format_settings': {'key': 'fileFormatSettings', 'type': 'object'},
        'is_ci_generated': {'key': 'isCIGenerated', 'type': 'bool'},
        'force_sas_auth': {'key': 'forceSasAuth', 'type': 'bool'},
        'has_header': {'key': 'hasHeader', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(PartitionMetadata, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.location = kwargs.get('location', None)
        self.refresh_time = kwargs.get('refresh_time', None)
        self.file_format_settings = kwargs.get('file_format_settings', None)
        self.is_ci_generated = kwargs.get('is_ci_generated', None)
        self.force_sas_auth = kwargs.get('force_sas_auth', None)
        self.has_header = kwargs.get('has_header', None)
