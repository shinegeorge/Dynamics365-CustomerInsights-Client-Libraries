# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EvaluationStats(Model):
    """Represents measure evaluation stats.

    :param last_successful: Gets the last successful evaluation
    :type last_successful: datetime
    :param consecutive_failure_count: Gets the number of consecutive failures
    :type consecutive_failure_count: int
    """

    _attribute_map = {
        'last_successful': {'key': 'lastSuccessful', 'type': 'iso-8601'},
        'consecutive_failure_count': {'key': 'consecutiveFailureCount', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(EvaluationStats, self).__init__(**kwargs)
        self.last_successful = kwargs.get('last_successful', None)
        self.consecutive_failure_count = kwargs.get('consecutive_failure_count', None)
