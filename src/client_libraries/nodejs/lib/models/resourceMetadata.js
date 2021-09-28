/*
 * Code generated by Microsoft (R) AutoRest Code Generator.
 * Changes may cause incorrect behavior and will be lost if the code is
 * regenerated.
 */

'use strict';

/**
 * Represents a Resource metadata
 *
 */
class ResourceMetadata {
  /**
   * Create a ResourceMetadata.
   * @property {string} [kind] Possible values include:
   * 'bearerAuthenticationConnection', 'sshKeyAuthenticationConnection',
   * 'apiKeyAuthenticationConnection', 'basicAuthenticationConnection',
   * 'firstPartyADConnection', 'amazonS3Connection', 'adlsGen2', 'd365Sales',
   * 'd365Marketing', 'attachCds', 'ftp', 'facebookAds', 'amlWorkspace',
   * 'mlStudioWebservice', 'adRoll', 'rollWorks', 'constantContact',
   * 'campaignMonitor', 'http', 'dotDigital', 'mailchimp', 'linkedIn',
   * 'googleAds', 'marketo', 'microsoftAds', 'omnisend', 'sendGrid',
   * 'sendinblue', 'activeCampaign', 'autopilot', 'klaviyo', 'snapchat',
   * 'powerBI', 'azureSql', 'synapse'
   * @property {uuid} [resourceId] Gets the Id of the resource.
   * @property {uuid} [operationId] Gets the Id of the operation being
   * performed on the resource.
   * @property {string} [name] Gets the Name of the resource.
   * @property {string} [description] Gets the Description of the resource.
   * @property {uuid} [keyVaultMetadataId] MetadataId for Linked
   * KeyVaultMetadata
   * @property {object} [mappedSecrets]
   * @property {string} [mappedSecrets.mappedFieldId] The identifier for field
   * mapping to a keyVault
   * @property {uuid} [mappedSecrets.linkedKeyVaultMetadataId] Gets uniqueId of
   * the KeyVault
   * @property {uuid} [mappedSecrets.mappingEntityId] Gets uniqueId of entity
   * Mapping Secrets
   * @property {object} [mappedSecrets.byoKeyVaultFieldMapping] Gets Secret
   * Names for Fields Mapped in KeyVault
   * @property {uuid} [mappedSecrets.instanceId] Customer Insights instance id
   * associated with this object.
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
   * Defines the metadata of ResourceMetadata
   *
   * @returns {object} metadata of ResourceMetadata
   *
   */
  mapper() {
    return {
      required: false,
      serializedName: 'ResourceMetadata',
      type: {
        name: 'Composite',
        className: 'ResourceMetadata',
        modelProperties: {
          kind: {
            required: false,
            serializedName: 'kind',
            type: {
              name: 'String'
            }
          },
          resourceId: {
            required: false,
            serializedName: 'resourceId',
            type: {
              name: 'String'
            }
          },
          operationId: {
            required: false,
            serializedName: 'operationId',
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
          description: {
            required: false,
            serializedName: 'description',
            type: {
              name: 'String'
            }
          },
          keyVaultMetadataId: {
            required: false,
            serializedName: 'keyVaultMetadataId',
            type: {
              name: 'String'
            }
          },
          mappedSecrets: {
            required: false,
            serializedName: 'mappedSecrets',
            type: {
              name: 'Composite',
              className: 'MappedSecretMetadata'
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

module.exports = ResourceMetadata;
