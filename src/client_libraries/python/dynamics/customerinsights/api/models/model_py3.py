# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Model(Model):
    """Model.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param name:
    :type name: str
    :param description:
    :type description: str
    :param is_hidden:
    :type is_hidden: bool
    :param version:
    :type version: str
    :param culture:
    :type culture: str
    :param pbitime_zone:
    :type pbitime_zone: str
    :param modified_time:
    :type modified_time: datetime
    :param pbimashup:
    :type pbimashup: ~dynamics.customerinsights.api.models.Mashup
    :ivar annotations:
    :vartype annotations:
     list[~dynamics.customerinsights.api.models.Annotation]
    :ivar entities:
    :vartype entities: list[~dynamics.customerinsights.api.models.Entity]
    :ivar relationships:
    :vartype relationships:
     list[~dynamics.customerinsights.api.models.Relationship]
    :ivar reference_models:
    :vartype reference_models:
     list[~dynamics.customerinsights.api.models.ReferenceModel]
    """

    _validation = {
        'annotations': {'readonly': True},
        'entities': {'readonly': True},
        'relationships': {'readonly': True},
        'reference_models': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'is_hidden': {'key': 'isHidden', 'type': 'bool'},
        'version': {'key': 'version', 'type': 'str'},
        'culture': {'key': 'culture', 'type': 'str'},
        'pbitime_zone': {'key': 'pbi:timeZone', 'type': 'str'},
        'modified_time': {'key': 'modifiedTime', 'type': 'iso-8601'},
        'pbimashup': {'key': 'pbi:mashup', 'type': 'Mashup'},
        'annotations': {'key': 'annotations', 'type': '[Annotation]'},
        'entities': {'key': 'entities', 'type': '[Entity]'},
        'relationships': {'key': 'relationships', 'type': '[Relationship]'},
        'reference_models': {'key': 'referenceModels', 'type': '[ReferenceModel]'},
    }

    def __init__(self, *, name: str=None, description: str=None, is_hidden: bool=None, version: str=None, culture: str=None, pbitime_zone: str=None, modified_time=None, pbimashup=None, **kwargs) -> None:
        super(Model, self).__init__(**kwargs)
        self.name = name
        self.description = description
        self.is_hidden = is_hidden
        self.version = version
        self.culture = culture
        self.pbitime_zone = pbitime_zone
        self.modified_time = modified_time
        self.pbimashup = pbimashup
        self.annotations = None
        self.entities = None
        self.relationships = None
        self.reference_models = None
