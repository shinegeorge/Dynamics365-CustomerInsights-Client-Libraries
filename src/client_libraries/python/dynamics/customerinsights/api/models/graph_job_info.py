# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GraphJobInfo(Model):
    """GraphJobInfo.

    :param job_id:
    :type job_id: str
    :param job_type: Possible values include: 'full', 'incremental'
    :type job_type: str or ~dynamics.customerinsights.api.models.enum
    :param job_submission_kind: Possible values include: 'onDemand',
     'scheduled'
    :type job_submission_kind: str or
     ~dynamics.customerinsights.api.models.enum
    :param job_status: Possible values include: 'queued', 'needsUpdate',
     'running', 'failed', 'timedOut', 'aborted', 'deleted', 'successful',
     'skipped'
    :type job_status: str or ~dynamics.customerinsights.api.models.enum
    :param operation_type: Possible values include: 'none', 'ingestion',
     'derivedEntity', 'hierarchy', 'dataPreparation', 'map',
     'realtimeM3Search', 'match', 'merge', 'profileStore', 'search',
     'activity', 'contact', 'attributeMeasures', 'entityMeasures', 'measures',
     'segmentation', 'segmentMembership', 'enrichment', 'preEnrichment',
     'transform', 'intelligence', 'aiBuilder', 'insights', 'export',
     'modelManagement', 'relationship', 'roleAssignment', 'analysis',
     'semanticEntity', 'all'
    :type operation_type: str or ~dynamics.customerinsights.api.models.enum
    :param sub_type: Possible values include: 'noSubType',
     'templatedMeasures', 'createAnalysisModel', 'linkAnalysisModel',
     'singleActivityMapping', 'powerPlatform'
    :type sub_type: str or ~dynamics.customerinsights.api.models.enum
    :param end_timestamp:
    :type end_timestamp: datetime
    :param should_force_run_requested_nodes:
    :type should_force_run_requested_nodes: bool
    :param tasks:
    :type tasks: list[~dynamics.customerinsights.api.models.GraphTaskInfo]
    :param id_list:
    :type id_list: list[str]
    :param options:
    :type options: ~dynamics.customerinsights.api.models.GraphJobOptions
    :param submitted_timestamp:
    :type submitted_timestamp: datetime
    """

    _attribute_map = {
        'job_id': {'key': 'jobId', 'type': 'str'},
        'job_type': {'key': 'jobType', 'type': 'str'},
        'job_submission_kind': {'key': 'jobSubmissionKind', 'type': 'str'},
        'job_status': {'key': 'jobStatus', 'type': 'str'},
        'operation_type': {'key': 'operationType', 'type': 'str'},
        'sub_type': {'key': 'subType', 'type': 'str'},
        'end_timestamp': {'key': 'endTimestamp', 'type': 'iso-8601'},
        'should_force_run_requested_nodes': {'key': 'shouldForceRunRequestedNodes', 'type': 'bool'},
        'tasks': {'key': 'tasks', 'type': '[GraphTaskInfo]'},
        'id_list': {'key': 'idList', 'type': '[str]'},
        'options': {'key': 'options', 'type': 'GraphJobOptions'},
        'submitted_timestamp': {'key': 'submittedTimestamp', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(GraphJobInfo, self).__init__(**kwargs)
        self.job_id = kwargs.get('job_id', None)
        self.job_type = kwargs.get('job_type', None)
        self.job_submission_kind = kwargs.get('job_submission_kind', None)
        self.job_status = kwargs.get('job_status', None)
        self.operation_type = kwargs.get('operation_type', None)
        self.sub_type = kwargs.get('sub_type', None)
        self.end_timestamp = kwargs.get('end_timestamp', None)
        self.should_force_run_requested_nodes = kwargs.get('should_force_run_requested_nodes', None)
        self.tasks = kwargs.get('tasks', None)
        self.id_list = kwargs.get('id_list', None)
        self.options = kwargs.get('options', None)
        self.submitted_timestamp = kwargs.get('submitted_timestamp', None)
