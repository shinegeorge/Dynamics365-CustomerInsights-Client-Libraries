# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MeasureAggregate(Model):
    """Represents an aggregate.

    :param operation: Possible values include: 'sum', 'avg', 'min', 'max',
     'count', 'countDistinct', 'first', 'last'
    :type operation: str or ~dynamics.customerinsights.api.models.enum
    :param field: Gets the field on which the aggregate operation is applied
    :type field: str
    :param alias: Gets the alias for the field
    :type alias: str
    :param display_name: Gets the display name for the aggregate
    :type display_name: str
    :param order: Gets the order for the aggregate
    :type order: int
    """

    _attribute_map = {
        'operation': {'key': 'operation', 'type': 'str'},
        'field': {'key': 'field', 'type': 'str'},
        'alias': {'key': 'alias', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'order': {'key': 'order', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(MeasureAggregate, self).__init__(**kwargs)
        self.operation = kwargs.get('operation', None)
        self.field = kwargs.get('field', None)
        self.alias = kwargs.get('alias', None)
        self.display_name = kwargs.get('display_name', None)
        self.order = kwargs.get('order', None)
