# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ProfileStoreCollectionInfo(Model):
    """ProfileStoreCollectionInfo.

    :param current_state: Possible values include: 'empty', 'inBuild',
     'queryable'
    :type current_state: str or ~dynamics.customerinsights.api.models.enum
    :param row_count: Gets the row count of customer file yielded from merge
     output.
    :type row_count: long
    :param size: Gets the size of customer file yielded from merge .
    :type size: long
    :param profile_store_hydration_state_info: Gets the state of profile store
     hydration per job type.
    :type profile_store_hydration_state_info: dict[str, str]
    """

    _attribute_map = {
        'current_state': {'key': 'currentState', 'type': 'str'},
        'row_count': {'key': 'rowCount', 'type': 'long'},
        'size': {'key': 'size', 'type': 'long'},
        'profile_store_hydration_state_info': {'key': 'profileStoreHydrationStateInfo', 'type': '{str}'},
    }

    def __init__(self, *, current_state=None, row_count: int=None, size: int=None, profile_store_hydration_state_info=None, **kwargs) -> None:
        super(ProfileStoreCollectionInfo, self).__init__(**kwargs)
        self.current_state = current_state
        self.row_count = row_count
        self.size = size
        self.profile_store_hydration_state_info = profile_store_hydration_state_info
