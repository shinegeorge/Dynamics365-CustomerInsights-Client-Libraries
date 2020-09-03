# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class InstanceInfo(Model):
    """Represents an instance.

    :param instance_id: Gets the unique ID for this instance.
    :type instance_id: str
    :param name: Gets the instance name. (not persisted in store)
    :type name: str
    :param instance_type: Possible values include: 'trial', 'sandbox',
     'production'
    :type instance_type: str or ~dynamics.customerinsights.api.models.enum
    :param expiry_time_utc: Gets the time the instance is set to expire. (not
     persisted in store)
    :type expiry_time_utc: datetime
    """

    _attribute_map = {
        'instance_id': {'key': 'instanceId', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'instance_type': {'key': 'instanceType', 'type': 'str'},
        'expiry_time_utc': {'key': 'expiryTimeUtc', 'type': 'iso-8601'},
    }

    def __init__(self, *, instance_id: str=None, name: str=None, instance_type=None, expiry_time_utc=None, **kwargs) -> None:
        super(InstanceInfo, self).__init__(**kwargs)
        self.instance_id = instance_id
        self.name = name
        self.instance_type = instance_type
        self.expiry_time_utc = expiry_time_utc
