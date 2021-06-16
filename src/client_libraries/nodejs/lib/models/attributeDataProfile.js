/*
 * Code generated by Microsoft (R) AutoRest Code Generator.
 * Changes may cause incorrect behavior and will be lost if the code is
 * regenerated.
 */

'use strict';

/**
 * Attribute data profile
 *
 */
class AttributeDataProfile {
  /**
   * Create a AttributeDataProfile.
   * @property {array} [valueCounts] Represents Distribution of the top 100
   * values.
   * @property {array} [histogram] Represents histogram information Ordered
   * from smallest to largest bin.
   * @property {string} [qualifiedEntityName] Qualified entity name.
   * @property {string} [attributeName] Attribute name.
   * @property {object} [min] Minimum value.
   * @property {object} [max] Maximum value.
   * @property {number} [count] Total row count.
   * @property {number} [missingCount] Row count of missing values.
   * @property {number} [errorCount] Number of error values.
   * @property {object} [quantiles]
   * @property {number} [quantiles.p0D1] Represents 1% quantile.
   * @property {number} [quantiles.p1] Represents 1% quantile.
   * @property {number} [quantiles.p5] Represents 5% quantile.
   * @property {number} [quantiles.p25] Represents 25% quantile.
   * @property {number} [quantiles.p50] Represents 50% quantile.
   * @property {number} [quantiles.p75] Represents 75% quantile.
   * @property {number} [quantiles.p95] Represents 95% quantile.
   * @property {number} [quantiles.p99] Represents 99% quantile.
   * @property {number} [quantiles.p99D9] Represents 9% quantile.
   * @property {object} [moments]
   * @property {number} [moments.mean] Represents the mean.
   * @property {number} [moments.standardDeviation] Represents standard
   * deviation.
   * @property {number} [moments.variance] Represents variance.
   * @property {number} [moments.skewness] Represents skewness in data.
   * @property {number} [moments.kurtosis] Represents kurtosis.
   * @property {number} [uniqueValueCount] Number of unique values.
   * @property {date} [profilingDate] Profiling date
   * @property {boolean} [isSuggestedPrimaryKey] Represents a value indicating
   * whether this attribute can be used as a primary key of the entity
   * @property {object} [checkIfExactStats] Represents a value indicating
   * whether we calculate exact or approx stats
   */
  constructor() {
  }

  /**
   * Defines the metadata of AttributeDataProfile
   *
   * @returns {object} metadata of AttributeDataProfile
   *
   */
  mapper() {
    return {
      required: false,
      serializedName: 'AttributeDataProfile',
      type: {
        name: 'Composite',
        className: 'AttributeDataProfile',
        modelProperties: {
          valueCounts: {
            required: false,
            serializedName: 'valueCounts',
            type: {
              name: 'Sequence',
              element: {
                  required: false,
                  serializedName: 'ValueCountElementType',
                  type: {
                    name: 'Composite',
                    className: 'ValueCount'
                  }
              }
            }
          },
          histogram: {
            required: false,
            serializedName: 'histogram',
            type: {
              name: 'Sequence',
              element: {
                  required: false,
                  serializedName: 'HistogramBinElementType',
                  type: {
                    name: 'Composite',
                    className: 'HistogramBin'
                  }
              }
            }
          },
          qualifiedEntityName: {
            required: false,
            serializedName: 'qualifiedEntityName',
            type: {
              name: 'String'
            }
          },
          attributeName: {
            required: false,
            serializedName: 'attributeName',
            type: {
              name: 'String'
            }
          },
          min: {
            required: false,
            serializedName: 'min',
            type: {
              name: 'Object'
            }
          },
          max: {
            required: false,
            serializedName: 'max',
            type: {
              name: 'Object'
            }
          },
          count: {
            required: false,
            serializedName: 'count',
            type: {
              name: 'Number'
            }
          },
          missingCount: {
            required: false,
            serializedName: 'missingCount',
            type: {
              name: 'Number'
            }
          },
          errorCount: {
            required: false,
            serializedName: 'errorCount',
            type: {
              name: 'Number'
            }
          },
          quantiles: {
            required: false,
            serializedName: 'quantiles',
            type: {
              name: 'Composite',
              className: 'Quantiles'
            }
          },
          moments: {
            required: false,
            serializedName: 'moments',
            type: {
              name: 'Composite',
              className: 'Moments'
            }
          },
          uniqueValueCount: {
            required: false,
            serializedName: 'uniqueValueCount',
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
          isSuggestedPrimaryKey: {
            required: false,
            serializedName: 'isSuggestedPrimaryKey',
            type: {
              name: 'Boolean'
            }
          },
          checkIfExactStats: {
            required: false,
            serializedName: 'checkIfExactStats',
            type: {
              name: 'Object'
            }
          }
        }
      }
    };
  }
}

module.exports = AttributeDataProfile;
