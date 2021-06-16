/*
 * Code generated by Microsoft (R) AutoRest Code Generator.
 * Changes may cause incorrect behavior and will be lost if the code is
 * regenerated.
 */

'use strict';

/**
 * The instance metadata.
 *
 */
class InstanceMetadata {
  /**
   * Create a InstanceMetadata.
   * @property {string} [name] Gets the user defined instance name.
   * @property {string} [provisioningState] Possible values include: 'new',
   * 'creating', 'active', 'createFailed', 'updateFailed', 'deleting',
   * 'refreshCredentials', 'resetInstanceInProgress', 'updating',
   * 'quickUpdate', 'deactivated'
   * @property {string} [instanceType] Possible values include: 'trial',
   * 'sandbox', 'production', 'pitchDemo', 'pov'
   * @property {object} [refreshSchedule]
   * @property {boolean} [refreshSchedule.isActive] Gets a value indicating
   * whether the schedule is active.
   * @property {string} [refreshSchedule.timezoneId] Gets the ID of the
   * timezone
   * @property {array} [refreshSchedule.cronSchedules] Gets the schedule in
   * CRON format
   * @property {uuid} [refreshSchedule.scheduleId] Gets the ID of the schedule
   * @property {uuid} [refreshSchedule.instanceId] Customer Insights instance
   * id associated with this object.
   * @property {date} [expiryTimeUtc] Gets the time the instance is set to
   * expire.
   * @property {string} [region] Gets the Azure region where the instance
   * lives.
   * @property {object} [cdsOrgInfo]
   * @property {string} [cdsOrgInfo.friendlyName] Gets the Cds Organization
   * Friendly Name
   * @property {string} [cdsOrgInfo.url] Gets the Cds Organization Url
   * @property {string} [cdsOrgInfo.state] Gets the Cds Organization State
   * @property {string} [cdsOrgInfo.location] Gets region location of Cds
   * Organization
   * @property {string} [cdsOrgInfo.environmentSku] Gets SKU of Cds
   * Organization
   * @property {date} [cdsOrgInfo.expirationTime] Gets the expiration time of
   * CDS Organization if the SKU is Trial
   * @property {date} [cdsOrgInfo.maxAllowedExpirationTime] Gets the max
   * allowed expiration time of CDS Organization if the SKU is Trial
   * @property {object} [cdsMdlInfo]
   * @property {object} [cdsMdlInfo.privateWorkSpace]
   * @property {string} [cdsMdlInfo.privateWorkSpace.name] Gets the datalake
   * folder Friendly Name
   * @property {string} [cdsMdlInfo.privateWorkSpace.uniqueName] Gets the Cds
   * datalake folder unique Name
   * @property {object} [cdsMdlInfo.publicWorkSpace]
   * @property {string} [cdsMdlInfo.publicWorkSpace.name] Gets the datalake
   * folder Friendly Name
   * @property {string} [cdsMdlInfo.publicWorkSpace.uniqueName] Gets the Cds
   * datalake folder unique Name
   * @property {number} [maxTrialExtensionsAllowed] Gets the total number of
   * extensions allowed if this is trial instance
   * @property {string} [trialExtensionHistory] Stores the details of trial
   * extensions done if this is a trial instance
   * @property {boolean} [isRefreshCredentialRequired] Gets a value indicating
   * if credential  is required to refresh any of the datasources
   * @property {array} [trialExtensionDetails] Stores the details of trial
   * extensions done if this is a trial instance
   * @property {number} [version] Version number of this object.
   * @property {string} [updatedBy] UPN of the user who last updated this
   * record.
   * @property {date} [updatedUtc] Time this object was last updated.
   * @property {string} [createdBy] Email address of the user who created this
   * record.
   * @property {date} [createdUtc] Time this object was initially created.
   * @property {uuid} [instanceId] Customer Insights instance id associated
   * with this object.
   */
  constructor() {
  }

  /**
   * Defines the metadata of InstanceMetadata
   *
   * @returns {object} metadata of InstanceMetadata
   *
   */
  mapper() {
    return {
      required: false,
      serializedName: 'InstanceMetadata',
      type: {
        name: 'Composite',
        className: 'InstanceMetadata',
        modelProperties: {
          name: {
            required: false,
            serializedName: 'name',
            type: {
              name: 'String'
            }
          },
          provisioningState: {
            required: false,
            serializedName: 'provisioningState',
            type: {
              name: 'String'
            }
          },
          instanceType: {
            required: false,
            serializedName: 'instanceType',
            type: {
              name: 'String'
            }
          },
          refreshSchedule: {
            required: false,
            serializedName: 'refreshSchedule',
            type: {
              name: 'Composite',
              className: 'DataRefreshSchedule'
            }
          },
          expiryTimeUtc: {
            required: false,
            serializedName: 'expiryTimeUtc',
            type: {
              name: 'DateTime'
            }
          },
          region: {
            required: false,
            serializedName: 'region',
            type: {
              name: 'String'
            }
          },
          cdsOrgInfo: {
            required: false,
            serializedName: 'cdsOrgInfo',
            type: {
              name: 'Composite',
              className: 'CdsOrgInfo'
            }
          },
          cdsMdlInfo: {
            required: false,
            serializedName: 'cdsMdlInfo',
            type: {
              name: 'Composite',
              className: 'CdsMdlInfo'
            }
          },
          maxTrialExtensionsAllowed: {
            required: false,
            serializedName: 'maxTrialExtensionsAllowed',
            type: {
              name: 'Number'
            }
          },
          trialExtensionHistory: {
            required: false,
            serializedName: 'trialExtensionHistory',
            type: {
              name: 'String'
            }
          },
          isRefreshCredentialRequired: {
            required: false,
            serializedName: 'isRefreshCredentialRequired',
            type: {
              name: 'Boolean'
            }
          },
          trialExtensionDetails: {
            required: false,
            serializedName: 'trialExtensionDetails',
            type: {
              name: 'Sequence',
              element: {
                  required: false,
                  serializedName: 'TrialExtensionDetailsElementType',
                  type: {
                    name: 'Composite',
                    className: 'TrialExtensionDetails'
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

module.exports = InstanceMetadata;
