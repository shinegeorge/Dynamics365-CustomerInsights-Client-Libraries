# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class IC360EntityModel(Model):
    """Represents Entity Model.

    :param instance_id: Gets the instance ID associated with the model.
    :type instance_id: str
    :param dataflow_id: Gets the dataflow ID associated with the model.
    :type dataflow_id: str
    :param datasource_id: Gets the datasource ID associated with the model.
    :type datasource_id: str
    :param dataflow_type: Possible values include: 'dynamics365',
     'salesforce', 'conflationSortAndRefine', 'conflationDeduplication',
     'conflationMatchPairs', 'conflationResolveConflicts', 'enriched', 'kpi',
     'powerQuery', 'dataPreparation', 'intelligence', 'unifiedActivity',
     'segmentation', 'ingestion', 'attachCdm', 'genericPrediction',
     'attachCds', 'unknown', 'powerPlatform', 'datahub', 'insights',
     'derivedEntity', 'powerPlatformSource', 'powerPlatformBYDL',
     'powerPlatformBYDLSource', 'semanticActivity', 'segmentMembership',
     'cjoData', 'eiData', 'hierarchy'
    :type dataflow_type: str or ~dynamics.customerinsights.api.models.enum
    :param entities: Gets entities in the model.
    :type entities:
     list[~dynamics.customerinsights.api.models.IEntityMetadata]
    """

    _attribute_map = {
        'instance_id': {'key': 'instanceId', 'type': 'str'},
        'dataflow_id': {'key': 'dataflowId', 'type': 'str'},
        'datasource_id': {'key': 'datasourceId', 'type': 'str'},
        'dataflow_type': {'key': 'dataflowType', 'type': 'str'},
        'entities': {'key': 'entities', 'type': '[IEntityMetadata]'},
    }

    def __init__(self, *, instance_id: str=None, dataflow_id: str=None, datasource_id: str=None, dataflow_type=None, entities=None, **kwargs) -> None:
        super(IC360EntityModel, self).__init__(**kwargs)
        self.instance_id = instance_id
        self.dataflow_id = dataflow_id
        self.datasource_id = datasource_id
        self.dataflow_type = dataflow_type
        self.entities = entities
