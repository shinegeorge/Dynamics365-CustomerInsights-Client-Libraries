/*
 * Code generated by Microsoft (R) AutoRest Code Generator.
 * Changes may cause incorrect behavior and will be lost if the code is
 * regenerated.
 */

'use strict';

/**
 * Represents metadata for a Account Hierarchy.
 *
 */
class HierarchyMetadata {
  /**
   * Create a HierarchyMetadata.
   * @property {string} [name] Gets the unique name of the hierarchy.
   * @property {string} [displayName] Gets the Display name of the hierarchy.
   * @property {object} [dependency]
   * @property {string} [dependency.sourceEntity] Gets the source entities
   * fully qualified name.
   * @property {string} [dependency.accountIdAttribute] Gets entity account Id.
   * @property {string} [dependency.parentAccountIdAttribute] Gets parent
   * account id.
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
   * Defines the metadata of HierarchyMetadata
   *
   * @returns {object} metadata of HierarchyMetadata
   *
   */
  mapper() {
    return {
      required: false,
      serializedName: 'HierarchyMetadata',
      type: {
        name: 'Composite',
        className: 'HierarchyMetadata',
        modelProperties: {
          name: {
            required: false,
            serializedName: 'name',
            type: {
              name: 'String'
            }
          },
          displayName: {
            required: false,
            serializedName: 'displayName',
            type: {
              name: 'String'
            }
          },
          dependency: {
            required: false,
            serializedName: 'dependency',
            type: {
              name: 'Composite',
              className: 'HierarchyDependency'
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

module.exports = HierarchyMetadata;
