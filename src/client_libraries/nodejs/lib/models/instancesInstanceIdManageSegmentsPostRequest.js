/*
 * Code generated by Microsoft (R) AutoRest Code Generator.
 * Changes may cause incorrect behavior and will be lost if the code is
 * regenerated.
 */

'use strict';

const models = require('./index');

/**
 * Represents a base Segment Metadata.
 *
 * @extends models['SegmentMetadata']
 */
class InstancesInstanceIdManageSegmentsPostRequest extends models['SegmentMetadata'] {
  /**
   * Create a InstancesInstanceIdManageSegmentsPostRequest.
   */
  constructor() {
    super();
  }

  /**
   * Defines the metadata of InstancesInstanceIdManageSegmentsPostRequest
   *
   * @returns {object} metadata of InstancesInstanceIdManageSegmentsPostRequest
   *
   */
  mapper() {
    return {
      required: false,
      serializedName: 'Instances-instanceId-ManageSegmentsPostRequest',
      type: {
        name: 'Composite',
        className: 'InstancesInstanceIdManageSegmentsPostRequest',
        modelProperties: {
          kind: {
            required: false,
            serializedName: 'kind',
            type: {
              name: 'String'
            }
          },
          name: {
            required: false,
            serializedName: 'name',
            type: {
              name: 'String'
            }
          },
          friendlyName: {
            required: false,
            serializedName: 'friendlyName',
            type: {
              name: 'String'
            }
          },
          description: {
            required: false,
            serializedName: 'description',
            type: {
              name: 'String'
            }
          },
          segmentQueryExpression: {
            required: false,
            serializedName: 'segmentQueryExpression',
            type: {
              name: 'Composite',
              className: 'SegmentationQuery'
            }
          },
          state: {
            required: false,
            serializedName: 'state',
            type: {
              name: 'String'
            }
          },
          errorDescription: {
            required: false,
            serializedName: 'errorDescription',
            type: {
              name: 'String'
            }
          },
          endDate: {
            required: false,
            serializedName: 'endDate',
            type: {
              name: 'DateTime'
            }
          },
          evaluationStatus: {
            required: false,
            serializedName: 'evaluationStatus',
            type: {
              name: 'Composite',
              className: 'SegmentationPublishStats'
            }
          },
          sqlValidationStats: {
            required: false,
            serializedName: 'sqlValidationStats',
            type: {
              name: 'Composite',
              className: 'SqlValidationStats'
            }
          },
          evaluationStatusHistory: {
            required: false,
            serializedName: 'evaluationStatusHistory',
            type: {
              name: 'Sequence',
              element: {
                  required: false,
                  serializedName: 'HistoricalSegmentStatsElementType',
                  type: {
                    name: 'Composite',
                    className: 'HistoricalSegmentStats'
                  }
              }
            }
          },
          version: {
            required: false,
            serializedName: 'version',
            type: {
              name: 'Number'
            }
          },
          updatedBy: {
            required: false,
            serializedName: 'updatedBy',
            type: {
              name: 'String'
            }
          },
          updatedUtc: {
            required: false,
            serializedName: 'updatedUtc',
            type: {
              name: 'DateTime'
            }
          },
          createdBy: {
            required: false,
            serializedName: 'createdBy',
            type: {
              name: 'String'
            }
          },
          createdUtc: {
            required: false,
            serializedName: 'createdUtc',
            type: {
              name: 'DateTime'
            }
          },
          instanceId: {
            required: false,
            serializedName: 'instanceId',
            type: {
              name: 'String'
            }
          }
        }
      }
    };
  }
}

module.exports = InstancesInstanceIdManageSegmentsPostRequest;
