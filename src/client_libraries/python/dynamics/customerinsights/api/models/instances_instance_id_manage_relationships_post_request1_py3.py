# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .relationship_metadata_py3 import RelationshipMetadata


class InstancesInstanceIdManageRelationshipsPostRequest1(RelationshipMetadata):
    """Represents a Relationship.

    :param friendly_name: Gets the friendly name of the relationship.
    :type friendly_name: str
    :param name: Gets the unique name for relationship
    :type name: str
    :param description: Gets the description for relationship
    :type description: str
    :param relationship_type: Possible values include:
     'singleKeyRelationshipOrigin', 'singleKeyRelationshipDestination',
     'dataSourceLineageOrigin', 'dataSourceLineageDestination'
    :type relationship_type: str or ~dynamics.customerinsights.api.models.enum
    :param from_attribute_name: Gets the name of the foreign key reference
     attribute that this relationship originates from.
    :type from_attribute_name: str
    :param from_entity_name: Gets the name of the entity this relationship
     originates from.
    :type from_entity_name: str
    :param to_attribute_name: Gets the name of the foreign key attribute that
     this relationship points to.
    :type to_attribute_name: str
    :param to_entity_name: Gets the name of the entity this relationship
     points to.
    :type to_entity_name: str
    :param cardinality: Possible values include: 'oneToMany', 'oneToOne',
     'manyToOne'
    :type cardinality: str or ~dynamics.customerinsights.api.models.enum
    :param source: Possible values include: 'user', 'system', 'inferred'
    :type source: str or ~dynamics.customerinsights.api.models.enum
    :param version: Version number of this object.
    :type version: long
    :param updated_by: UPN of the user who last updated this record.
    :type updated_by: str
    :param updated_utc: Time this object was last updated.
    :type updated_utc: datetime
    :param created_by: Email address of the user who created this record.
    :type created_by: str
    :param created_utc: Time this object was initially created.
    :type created_utc: datetime
    :param instance_id: Customer Insights instance id associated with this
     object.
    :type instance_id: str
    """

    _attribute_map = {
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'relationship_type': {'key': 'relationshipType', 'type': 'str'},
        'from_attribute_name': {'key': 'fromAttributeName', 'type': 'str'},
        'from_entity_name': {'key': 'fromEntityName', 'type': 'str'},
        'to_attribute_name': {'key': 'toAttributeName', 'type': 'str'},
        'to_entity_name': {'key': 'toEntityName', 'type': 'str'},
        'cardinality': {'key': 'cardinality', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'},
        'version': {'key': 'version', 'type': 'long'},
        'updated_by': {'key': 'updatedBy', 'type': 'str'},
        'updated_utc': {'key': 'updatedUtc', 'type': 'iso-8601'},
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'created_utc': {'key': 'createdUtc', 'type': 'iso-8601'},
        'instance_id': {'key': 'instanceId', 'type': 'str'},
    }

    def __init__(self, *, friendly_name: str=None, name: str=None, description: str=None, relationship_type=None, from_attribute_name: str=None, from_entity_name: str=None, to_attribute_name: str=None, to_entity_name: str=None, cardinality=None, source=None, version: int=None, updated_by: str=None, updated_utc=None, created_by: str=None, created_utc=None, instance_id: str=None, **kwargs) -> None:
        super(InstancesInstanceIdManageRelationshipsPostRequest1, self).__init__(friendly_name=friendly_name, name=name, description=description, relationship_type=relationship_type, from_attribute_name=from_attribute_name, from_entity_name=from_entity_name, to_attribute_name=to_attribute_name, to_entity_name=to_entity_name, cardinality=cardinality, source=source, version=version, updated_by=updated_by, updated_utc=updated_utc, created_by=created_by, created_utc=created_utc, instance_id=instance_id, **kwargs)
