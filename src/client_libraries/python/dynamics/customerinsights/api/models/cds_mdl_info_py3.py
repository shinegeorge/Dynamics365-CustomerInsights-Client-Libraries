# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CdsMdlInfo(Model):
    """The information on CDS MDL workspaces.

    :param private_work_space:
    :type private_work_space:
     ~dynamics.customerinsights.api.models.WorkSpaceDetail
    :param public_work_space:
    :type public_work_space:
     ~dynamics.customerinsights.api.models.WorkSpaceDetail
    """

    _attribute_map = {
        'private_work_space': {'key': 'privateWorkSpace', 'type': 'WorkSpaceDetail'},
        'public_work_space': {'key': 'publicWorkSpace', 'type': 'WorkSpaceDetail'},
    }

    def __init__(self, *, private_work_space=None, public_work_space=None, **kwargs) -> None:
        super(CdsMdlInfo, self).__init__(**kwargs)
        self.private_work_space = private_work_space
        self.public_work_space = public_work_space
