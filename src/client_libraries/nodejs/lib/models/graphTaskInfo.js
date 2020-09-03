/*
 * Code generated by Microsoft (R) AutoRest Code Generator.
 * Changes may cause incorrect behavior and will be lost if the code is
 * regenerated.
 */

'use strict';

/**
 * Class representing a GraphTaskInfo.
 */
class GraphTaskInfo {
  /**
   * Create a GraphTaskInfo.
   * @property {uuid} [taskId]
   * @property {string} [taskStatus] Possible values include: 'queued',
   * 'needsUpdate', 'running', 'failed', 'timedOut', 'aborted', 'deleted',
   * 'successful', 'skipped'
   * @property {string} [operationType] Possible values include: 'none',
   * 'ingestion', 'derivedEntity', 'dataPreparation', 'map', 'match', 'merge',
   * 'profileStore', 'search', 'activity', 'attributeMeasures',
   * 'entityMeasures', 'measures', 'segmentation', 'enrichment',
   * 'intelligence', 'aiBuilder', 'insights', 'export', 'modelManagement',
   * 'relationship', 'roleAssignment', 'analysis', 'all'
   * @property {string} [subType] Possible values include: 'templatedMeasures',
   * 'createAnalysisModel', 'linkAnalysisModel'
   * @property {array} [jobIds]
   * @property {string} [friendlyName]
   * @property {date} [endTimestamp]
   * @property {object} [ciError]
   * @property {string} [ciError.exceptionCulprit] Possible values include:
   * 'system', 'user', 'external'
   * @property {string} [ciError.errorCode]
   * @property {string} [ciError.resultSeverity] Possible values include:
   * 'error', 'warning'
   * @property {string} [ciError.message]
   * @property {object} [ciError.params]
   * @property {array} [ciError.ciResults]
   * @property {array} [ciErrors]
   * @property {array} [waitingTaskIds]
   * @property {object} [additionalInfo]
   * @property {string} [additionalInfo.kind] Possible values include: 'test',
   * 'segmentation', 'measures', 'export'
   * @property {date} [submittedTimestamp]
   */
  constructor() {
  }

  /**
   * Defines the metadata of GraphTaskInfo
   *
   * @returns {object} metadata of GraphTaskInfo
   *
   */
  mapper() {
    return {
      required: false,
      serializedName: 'GraphTaskInfo',
      type: {
        name: 'Composite',
        className: 'GraphTaskInfo',
        modelProperties: {
          taskId: {
            required: false,
            serializedName: 'taskId',
            type: {
              name: 'String'
            }
          },
          taskStatus: {
            required: false,
            serializedName: 'taskStatus',
            type: {
              name: 'String'
            }
          },
          operationType: {
            required: false,
            serializedName: 'operationType',
            type: {
              name: 'String'
            }
          },
          subType: {
            required: false,
            serializedName: 'subType',
            type: {
              name: 'String'
            }
          },
          jobIds: {
            required: false,
            serializedName: 'jobIds',
            type: {
              name: 'Sequence',
              element: {
                  required: false,
                  serializedName: 'UuidElementType',
                  type: {
                    name: 'String'
                  }
              }
            }
          },
          friendlyName: {
            required: false,
            serializedName: 'friendlyName',
            type: {
              name: 'String'
            }
          },
          endTimestamp: {
            required: false,
            serializedName: 'endTimestamp',
            type: {
              name: 'DateTime'
            }
          },
          ciError: {
            required: false,
            serializedName: 'ciError',
            type: {
              name: 'Composite',
              className: 'CIResult'
            }
          },
          ciErrors: {
            required: false,
            serializedName: 'ciErrors',
            type: {
              name: 'Sequence',
              element: {
                  required: false,
                  serializedName: 'CIResultElementType',
                  type: {
                    name: 'Composite',
                    className: 'CIResult'
                  }
              }
            }
          },
          waitingTaskIds: {
            required: false,
            serializedName: 'waitingTaskIds',
            type: {
              name: 'Sequence',
              element: {
                  required: false,
                  serializedName: 'UuidElementType',
                  type: {
                    name: 'String'
                  }
              }
            }
          },
          additionalInfo: {
            required: false,
            serializedName: 'additionalInfo',
            type: {
              name: 'Composite',
              className: 'CustomTaskInformation'
            }
          },
          submittedTimestamp: {
            required: false,
            serializedName: 'submittedTimestamp',
            type: {
              name: 'DateTime'
            }
          }
        }
      }
    };
  }
}

module.exports = GraphTaskInfo;
