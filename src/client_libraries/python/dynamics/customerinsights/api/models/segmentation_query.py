# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SegmentationQuery(Model):
    """Represent a Segment Query.

    :param type: Possible values include: 'structured', 'manual'
    :type type: str or ~dynamics.customerinsights.api.models.enum
    :param projections: Gets list of attributes to be projected in segment.
     (DEPRECATED)
    :type projections: list[str]
    :param projected_attributes: Gets list of attributes to be projected in
     segment.
    :type projected_attributes:
     list[~dynamics.customerinsights.api.models.SegmentationProjection]
    :param rowsets: Gets list of rowsets of segment.
    :type rowsets:
     list[~dynamics.customerinsights.api.models.SegmentationRowset]
    :param segmentation_query_sql: Gets the user specified custom SQL query.
    :type segmentation_query_sql: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'projections': {'key': 'projections', 'type': '[str]'},
        'projected_attributes': {'key': 'projectedAttributes', 'type': '[SegmentationProjection]'},
        'rowsets': {'key': 'rowsets', 'type': '[SegmentationRowset]'},
        'segmentation_query_sql': {'key': 'segmentationQuerySql', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SegmentationQuery, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.projections = kwargs.get('projections', None)
        self.projected_attributes = kwargs.get('projected_attributes', None)
        self.rowsets = kwargs.get('rowsets', None)
        self.segmentation_query_sql = kwargs.get('segmentation_query_sql', None)
