# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SegmentQueryStat(Model):
    """Represents a Segment Stat.

    :param rowset_stat: Gets a list of Rowset Stat.
    :type rowset_stat:
     list[~dynamics.customerinsights.api.models.SegmentRowsetStat]
    """

    _attribute_map = {
        'rowset_stat': {'key': 'rowsetStat', 'type': '[SegmentRowsetStat]'},
    }

    def __init__(self, *, rowset_stat=None, **kwargs) -> None:
        super(SegmentQueryStat, self).__init__(**kwargs)
        self.rowset_stat = rowset_stat
