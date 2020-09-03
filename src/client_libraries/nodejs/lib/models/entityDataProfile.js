/*
 * Code generated by Microsoft (R) AutoRest Code Generator.
 * Changes may cause incorrect behavior and will be lost if the code is
 * regenerated.
 */

'use strict';

/**
 * Class representing a EntityDataProfile.
 */
class EntityDataProfile {
  /**
   * Create a EntityDataProfile.
   * @property {string} [qualifiedEntityName]
   * @property {number} [rowCount]
   * @property {number} [quarantineRowCount]
   * @property {date} [profilingDate]
   * @property {string} [profiledAttributes]
   * @property {string} [corruptAttributes]
   */
  constructor() {
  }

  /**
   * Defines the metadata of EntityDataProfile
   *
   * @returns {object} metadata of EntityDataProfile
   *
   */
  mapper() {
    return {
      required: false,
      serializedName: 'EntityDataProfile',
      type: {
        name: 'Composite',
        className: 'EntityDataProfile',
        modelProperties: {
          qualifiedEntityName: {
            required: false,
            serializedName: 'qualifiedEntityName',
            type: {
              name: 'String'
            }
          },
          rowCount: {
            required: false,
            serializedName: 'rowCount',
            type: {
              name: 'Number'
            }
          },
          quarantineRowCount: {
            required: false,
            serializedName: 'quarantineRowCount',
            type: {
              name: 'Number'
            }
          },
          profilingDate: {
            required: false,
            serializedName: 'profilingDate',
            type: {
              name: 'DateTime'
            }
          },
          profiledAttributes: {
            required: false,
            serializedName: 'profiledAttributes',
            type: {
              name: 'String'
            }
          },
          corruptAttributes: {
            required: false,
            serializedName: 'corruptAttributes',
            type: {
              name: 'String'
            }
          }
        }
      }
    };
  }
}

module.exports = EntityDataProfile;
