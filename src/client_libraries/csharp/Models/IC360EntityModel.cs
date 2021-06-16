// <auto-generated>
// Code generated by Microsoft (R) AutoRest Code Generator.
// Changes may cause incorrect behavior and will be lost if the code is
// regenerated.
// </auto-generated>

namespace Microsoft.Dynamics.CustomerInsights.Api.Models
{
    using Newtonsoft.Json;
    using System.Collections;
    using System.Collections.Generic;
    using System.Linq;

    /// <summary>
    /// Represents Entity Model.
    /// </summary>
    public partial class IC360EntityModel
    {
        /// <summary>
        /// Initializes a new instance of the IC360EntityModel class.
        /// </summary>
        public IC360EntityModel()
        {
            CustomInit();
        }

        /// <summary>
        /// Initializes a new instance of the IC360EntityModel class.
        /// </summary>
        /// <param name="instanceId">Gets the instance ID associated with the
        /// model.</param>
        /// <param name="dataflowId">Gets the dataflow ID associated with the
        /// model.</param>
        /// <param name="datasourceId">Gets the datasource ID associated with
        /// the model.</param>
        /// <param name="dataflowType">Possible values include: 'dynamics365',
        /// 'salesforce', 'conflationSortAndRefine', 'conflationDeduplication',
        /// 'conflationMatchPairs', 'conflationResolveConflicts', 'enriched',
        /// 'kpi', 'powerQuery', 'dataPreparation', 'intelligence',
        /// 'unifiedActivity', 'segmentation', 'ingestion', 'attachCdm',
        /// 'genericPrediction', 'attachCds', 'unknown', 'powerPlatform',
        /// 'datahub', 'insights', 'derivedEntity', 'powerPlatformSource',
        /// 'powerPlatformBYDL', 'powerPlatformBYDLSource', 'semanticActivity',
        /// 'segmentMembership', 'cjoData', 'eiData', 'hierarchy'</param>
        /// <param name="entities">Gets entities in the model.</param>
        public IC360EntityModel(System.Guid? instanceId = default(System.Guid?), System.Guid? dataflowId = default(System.Guid?), System.Guid? datasourceId = default(System.Guid?), string dataflowType = default(string), IList<IEntityMetadata> entities = default(IList<IEntityMetadata>))
        {
            InstanceId = instanceId;
            DataflowId = dataflowId;
            DatasourceId = datasourceId;
            DataflowType = dataflowType;
            Entities = entities;
            CustomInit();
        }

        /// <summary>
        /// An initialization method that performs custom operations like setting defaults
        /// </summary>
        partial void CustomInit();

        /// <summary>
        /// Gets the instance ID associated with the model.
        /// </summary>
        [JsonProperty(PropertyName = "instanceId")]
        public System.Guid? InstanceId { get; set; }

        /// <summary>
        /// Gets the dataflow ID associated with the model.
        /// </summary>
        [JsonProperty(PropertyName = "dataflowId")]
        public System.Guid? DataflowId { get; set; }

        /// <summary>
        /// Gets the datasource ID associated with the model.
        /// </summary>
        [JsonProperty(PropertyName = "datasourceId")]
        public System.Guid? DatasourceId { get; set; }

        /// <summary>
        /// Gets or sets possible values include: 'dynamics365', 'salesforce',
        /// 'conflationSortAndRefine', 'conflationDeduplication',
        /// 'conflationMatchPairs', 'conflationResolveConflicts', 'enriched',
        /// 'kpi', 'powerQuery', 'dataPreparation', 'intelligence',
        /// 'unifiedActivity', 'segmentation', 'ingestion', 'attachCdm',
        /// 'genericPrediction', 'attachCds', 'unknown', 'powerPlatform',
        /// 'datahub', 'insights', 'derivedEntity', 'powerPlatformSource',
        /// 'powerPlatformBYDL', 'powerPlatformBYDLSource', 'semanticActivity',
        /// 'segmentMembership', 'cjoData', 'eiData', 'hierarchy'
        /// </summary>
        [JsonProperty(PropertyName = "dataflowType")]
        public string DataflowType { get; set; }

        /// <summary>
        /// Gets entities in the model.
        /// </summary>
        [JsonProperty(PropertyName = "entities")]
        public IList<IEntityMetadata> Entities { get; set; }

    }
}
