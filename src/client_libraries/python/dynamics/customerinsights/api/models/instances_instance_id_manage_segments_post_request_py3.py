# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .segment_metadata_py3 import SegmentMetadata


class InstancesInstanceIdManageSegmentsPostRequest(SegmentMetadata):
    """Represents a base Segment Metadata.

    :param kind: Possible values include: 'default', 'engagement'
    :type kind: str or ~dynamics.customerinsights.api.models.enum
    :param name: Gets the unique name of the segment
    :type name: str
    :param friendly_name: Gets the friendlyName of the segment.
    :type friendly_name: str
    :param description: Gets the description of the segment.
    :type description: str
    :param segment_query_expression:
    :type segment_query_expression:
     ~dynamics.customerinsights.api.models.SegmentationQuery
    :param state: Possible values include: 'inactive', 'active', 'validating',
     'validated', 'invalid', 'validationError'
    :type state: str or ~dynamics.customerinsights.api.models.enum
    :param error_description: Gets the error description when the segment
     metadata has some issues after refresh.
    :type error_description: str
    :param end_date: Gets the end date of the segment.
    :type end_date: datetime
    :param evaluation_status:
    :type evaluation_status:
     ~dynamics.customerinsights.api.models.SegmentationPublishStats
    :param sql_validation_stats:
    :type sql_validation_stats:
     ~dynamics.customerinsights.api.models.SqlValidationStats
    :param evaluation_status_history: Gets the segment evaluation status
     history. (not persisted in store)
    :type evaluation_status_history:
     list[~dynamics.customerinsights.api.models.HistoricalSegmentStats]
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
        'kind': {'key': 'kind', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'segment_query_expression': {'key': 'segmentQueryExpression', 'type': 'SegmentationQuery'},
        'state': {'key': 'state', 'type': 'str'},
        'error_description': {'key': 'errorDescription', 'type': 'str'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'evaluation_status': {'key': 'evaluationStatus', 'type': 'SegmentationPublishStats'},
        'sql_validation_stats': {'key': 'sqlValidationStats', 'type': 'SqlValidationStats'},
        'evaluation_status_history': {'key': 'evaluationStatusHistory', 'type': '[HistoricalSegmentStats]'},
        'version': {'key': 'version', 'type': 'long'},
        'updated_by': {'key': 'updatedBy', 'type': 'str'},
        'updated_utc': {'key': 'updatedUtc', 'type': 'iso-8601'},
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'created_utc': {'key': 'createdUtc', 'type': 'iso-8601'},
        'instance_id': {'key': 'instanceId', 'type': 'str'},
    }

    def __init__(self, *, kind=None, name: str=None, friendly_name: str=None, description: str=None, segment_query_expression=None, state=None, error_description: str=None, end_date=None, evaluation_status=None, sql_validation_stats=None, evaluation_status_history=None, version: int=None, updated_by: str=None, updated_utc=None, created_by: str=None, created_utc=None, instance_id: str=None, **kwargs) -> None:
        super(InstancesInstanceIdManageSegmentsPostRequest, self).__init__(kind=kind, name=name, friendly_name=friendly_name, description=description, segment_query_expression=segment_query_expression, state=state, error_description=error_description, end_date=end_date, evaluation_status=evaluation_status, sql_validation_stats=sql_validation_stats, evaluation_status_history=evaluation_status_history, version=version, updated_by=updated_by, updated_utc=updated_utc, created_by=created_by, created_utc=created_utc, instance_id=instance_id, **kwargs)
