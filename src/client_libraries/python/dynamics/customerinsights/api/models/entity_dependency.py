# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EntityDependency(Model):
    """Represents a reference to an entity.

    :param qualified_entity_name: Gets the qualified entity name.
    :type qualified_entity_name: str
    :param type: Possible values include: 'unspecified', 'profile',
     'conflationMap', 'activity', 'aggregateKpi', 'profileKpi',
     'unifiedActivity', 'segment', 'intelligence', 'genericPrediction',
     'enrichment', 'insights', 'derivedEntity', 'quarantine'
    :type type: str or ~dynamics.customerinsights.api.models.enum
    :param attribute_names: Gets the list of attributes included in the
     dependency.
    :type attribute_names: list[str]
    :param relationship_names: Gets the list of relationships included in the
     dependency
    :type relationship_names: list[str]
    """

    _attribute_map = {
        'qualified_entity_name': {'key': 'qualifiedEntityName', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'attribute_names': {'key': 'attributeNames', 'type': '[str]'},
        'relationship_names': {'key': 'relationshipNames', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(EntityDependency, self).__init__(**kwargs)
        self.qualified_entity_name = kwargs.get('qualified_entity_name', None)
        self.type = kwargs.get('type', None)
        self.attribute_names = kwargs.get('attribute_names', None)
        self.relationship_names = kwargs.get('relationship_names', None)
