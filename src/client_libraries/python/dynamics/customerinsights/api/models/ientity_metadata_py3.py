# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class IEntityMetadata(Model):
    """Represents Entity Metadata.

    :param name: Gets the name of the entity. eg: Contact.
    :type name: str
    :param qualified_entity_name: Gets the unqiue logical name for the entity
     If entity is from a datasource, QualifiedEntityName =
     datasourceId_EntityName eg: d8d3b26a-a8ad-42f7-901e-f7f745003a84_Contact.
     If entity is generated by C360, QualifiedEntityName = EntityName eg:
     Contact.
    :type qualified_entity_name: str
    :param data_source_name: Gets the datasource name of this entity, if no
     data source, return null or emptyString
    :type data_source_name: str
    :param dataflow_type: Possible values include: 'dynamics365',
     'salesforce', 'conflationSortAndRefine', 'conflationDeduplication',
     'conflationMatchPairs', 'conflationResolveConflicts', 'enriched', 'kpi',
     'powerQuery', 'dataPreparation', 'intelligence', 'unifiedActivity',
     'segmentation', 'ingestion', 'attachCdm', 'genericPrediction',
     'attachCds', 'unknown', 'powerPlatform', 'datahub', 'insights',
     'derivedEntity', 'powerPlatformSource', 'powerPlatformBYDL',
     'powerPlatformBYDLSource', 'semanticActivity', 'segmentMembership',
     'firstParty', 'hierarchy', 'contact', 'semanticEntity', 'attachSynapse',
     'transform'
    :type dataflow_type: str or ~dynamics.customerinsights.api.models.enum
    :param should_use_spark_sas_auth: Gets a value indicating whether Sas Auth
     is used for the entity.
    :type should_use_spark_sas_auth: bool
    :param datasource_id: Gets the original datasourceid of this entity, if no
     data source, return null or emptyString
    :type datasource_id: str
    :param entity_type: Possible values include: 'unspecified', 'profile',
     'conflationMap', 'activity', 'aggregateKpi', 'profileKpi',
     'unifiedActivity', 'segment', 'intelligence', 'genericPrediction',
     'enrichment', 'insights', 'derivedEntity', 'corrupt', 'selfConflation',
     'conflationManualReview', 'selfConflationManualReview',
     'semanticActivity', 'segmentMembership', 'hierarchy', 'dataLineage',
     'transform', 'semanticEntity'
    :type entity_type: str or ~dynamics.customerinsights.api.models.enum
    :param attributes: Gets entity attributes.
    :type attributes:
     list[~dynamics.customerinsights.api.models.IAttributeMetadata]
    :param keys: Gets the keys of the entity.
    :type keys:
     list[list[~dynamics.customerinsights.api.models.IAttributeMetadata]]
    :param relationships: Gets entity relationships.
    :type relationships:
     list[~dynamics.customerinsights.api.models.IRelationshipMetadata]
    :param timestamp_attribute:
    :type timestamp_attribute:
     ~dynamics.customerinsights.api.models.IAttributeMetadata
    :param incremental_attribute:
    :type incremental_attribute:
     ~dynamics.customerinsights.api.models.IAttributeMetadata
    :param semantic_type: Possible values include: 'Account', 'AccountLeads',
     'ActivityParty', 'ActivityPointer', 'Annotation', 'Appointment',
     'BusinessUnit', 'Campaign', 'CampaignActivity', 'CampaignItem',
     'CampaignResponse', 'Characteristic', 'Competitor', 'CompetitorAddress',
     'CompetitorProduct', 'Connection', 'ConnectionRole', 'Contact',
     'Contract', 'ContractDetail', 'Customer', 'CustomerAddress',
     'CustomerRelationship', 'Discount', 'DiscountType', 'Email',
     'Entitlement', 'Equipment', 'Fax', 'Feedback', 'Goal', 'Incident',
     'Invoice', 'InvoiceDetail', 'KbArticle', 'KnowledgeArticle', 'Lead',
     'LeadAddress', 'Letter', 'Metric', 'Opportunity', 'Organization', 'Owner',
     'PhoneCall', 'Position', 'PriceLevel', 'Product', 'Quote', 'RatingModel',
     'Resource', 'ResourceGroup', 'SalesLiterature', 'SalesOrder', 'Service',
     'ServiceAppointment', 'Site', 'SLA', 'SocialActivity', 'SocialProfile',
     'SystemUser', 'Task', 'Team', 'Territory', 'UoM'
    :type semantic_type: str or ~dynamics.customerinsights.api.models.enum
    :param refresh_time: Gets last refresh time for entity.
    :type refresh_time: datetime
    :param partitions: Gets entity data partitions.
    :type partitions:
     list[~dynamics.customerinsights.api.models.PartitionMetadata]
    :param incremental_upsert_partitions: Gets entity incremental upsert data
     partitions.
    :type incremental_upsert_partitions:
     list[~dynamics.customerinsights.api.models.PartitionMetadata]
    :param incremental_delete_partitions: Gets entity incremental delete data
     partitions.
    :type incremental_delete_partitions:
     list[~dynamics.customerinsights.api.models.PartitionMetadata]
    :param full_partitions_parquet: Gets entity data parquet partitions.
    :type full_partitions_parquet:
     list[~dynamics.customerinsights.api.models.PartitionMetadata]
    :param incremental_upsert_partitions_parquet: Gets entity incremental
     upsert data parquet partitions.
    :type incremental_upsert_partitions_parquet:
     list[~dynamics.customerinsights.api.models.PartitionMetadata]
    :param incremental_delete_partitions_parquet: Gets entity incremental
     delete data parquet partitions.
    :type incremental_delete_partitions_parquet:
     list[~dynamics.customerinsights.api.models.PartitionMetadata]
    :param annotations: Gets base entity name
    :type annotations: list[~dynamics.customerinsights.api.models.Annotation]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'qualified_entity_name': {'key': 'qualifiedEntityName', 'type': 'str'},
        'data_source_name': {'key': 'dataSourceName', 'type': 'str'},
        'dataflow_type': {'key': 'dataflowType', 'type': 'str'},
        'should_use_spark_sas_auth': {'key': 'shouldUseSparkSasAuth', 'type': 'bool'},
        'datasource_id': {'key': 'datasourceId', 'type': 'str'},
        'entity_type': {'key': 'entityType', 'type': 'str'},
        'attributes': {'key': 'attributes', 'type': '[IAttributeMetadata]'},
        'keys': {'key': 'keys', 'type': '[[IAttributeMetadata]]'},
        'relationships': {'key': 'relationships', 'type': '[IRelationshipMetadata]'},
        'timestamp_attribute': {'key': 'timestampAttribute', 'type': 'IAttributeMetadata'},
        'incremental_attribute': {'key': 'incrementalAttribute', 'type': 'IAttributeMetadata'},
        'semantic_type': {'key': 'semanticType', 'type': 'str'},
        'refresh_time': {'key': 'refreshTime', 'type': 'iso-8601'},
        'partitions': {'key': 'partitions', 'type': '[PartitionMetadata]'},
        'incremental_upsert_partitions': {'key': 'incrementalUpsertPartitions', 'type': '[PartitionMetadata]'},
        'incremental_delete_partitions': {'key': 'incrementalDeletePartitions', 'type': '[PartitionMetadata]'},
        'full_partitions_parquet': {'key': 'fullPartitionsParquet', 'type': '[PartitionMetadata]'},
        'incremental_upsert_partitions_parquet': {'key': 'incrementalUpsertPartitionsParquet', 'type': '[PartitionMetadata]'},
        'incremental_delete_partitions_parquet': {'key': 'incrementalDeletePartitionsParquet', 'type': '[PartitionMetadata]'},
        'annotations': {'key': 'annotations', 'type': '[Annotation]'},
    }

    def __init__(self, *, name: str=None, qualified_entity_name: str=None, data_source_name: str=None, dataflow_type=None, should_use_spark_sas_auth: bool=None, datasource_id: str=None, entity_type=None, attributes=None, keys=None, relationships=None, timestamp_attribute=None, incremental_attribute=None, semantic_type=None, refresh_time=None, partitions=None, incremental_upsert_partitions=None, incremental_delete_partitions=None, full_partitions_parquet=None, incremental_upsert_partitions_parquet=None, incremental_delete_partitions_parquet=None, annotations=None, **kwargs) -> None:
        super(IEntityMetadata, self).__init__(**kwargs)
        self.name = name
        self.qualified_entity_name = qualified_entity_name
        self.data_source_name = data_source_name
        self.dataflow_type = dataflow_type
        self.should_use_spark_sas_auth = should_use_spark_sas_auth
        self.datasource_id = datasource_id
        self.entity_type = entity_type
        self.attributes = attributes
        self.keys = keys
        self.relationships = relationships
        self.timestamp_attribute = timestamp_attribute
        self.incremental_attribute = incremental_attribute
        self.semantic_type = semantic_type
        self.refresh_time = refresh_time
        self.partitions = partitions
        self.incremental_upsert_partitions = incremental_upsert_partitions
        self.incremental_delete_partitions = incremental_delete_partitions
        self.full_partitions_parquet = full_partitions_parquet
        self.incremental_upsert_partitions_parquet = incremental_upsert_partitions_parquet
        self.incremental_delete_partitions_parquet = incremental_delete_partitions_parquet
        self.annotations = annotations
