# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SegmentationRowset(Model):
    """Represent a Row set.

    :param rowset_operation: Possible values include: 'union', 'intersect',
     'except', 'none', 'include', 'exclude'
    :type rowset_operation: str or ~dynamics.customerinsights.api.models.enum
    :param criteria:
    :type criteria:
     ~dynamics.customerinsights.api.models.SegmentMembershipCriteria
    :param paths: Gets the relationship path to use for segment criteria.
    :type paths: list[list[str]]
    :param rowset_id: Gets the rowset Id in the rowsets.
    :type rowset_id: str
    """

    _attribute_map = {
        'rowset_operation': {'key': 'rowsetOperation', 'type': 'str'},
        'criteria': {'key': 'criteria', 'type': 'SegmentMembershipCriteria'},
        'paths': {'key': 'paths', 'type': '[[str]]'},
        'rowset_id': {'key': 'rowsetId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SegmentationRowset, self).__init__(**kwargs)
        self.rowset_operation = kwargs.get('rowset_operation', None)
        self.criteria = kwargs.get('criteria', None)
        self.paths = kwargs.get('paths', None)
        self.rowset_id = kwargs.get('rowset_id', None)
