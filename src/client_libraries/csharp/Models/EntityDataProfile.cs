// <auto-generated>
// Code generated by Microsoft (R) AutoRest Code Generator.
// Changes may cause incorrect behavior and will be lost if the code is
// regenerated.
// </auto-generated>

namespace Microsoft.Dynamics.CustomerInsights.Api.Models
{
    using Newtonsoft.Json;
    using System.Linq;

    public partial class EntityDataProfile
    {
        /// <summary>
        /// Initializes a new instance of the EntityDataProfile class.
        /// </summary>
        public EntityDataProfile()
        {
            CustomInit();
        }

        /// <summary>
        /// Initializes a new instance of the EntityDataProfile class.
        /// </summary>
        public EntityDataProfile(string qualifiedEntityName = default(string), long? rowCount = default(long?), long? quarantineRowCount = default(long?), System.DateTime? profilingDate = default(System.DateTime?), string profiledAttributes = default(string), string corruptAttributes = default(string))
        {
            QualifiedEntityName = qualifiedEntityName;
            RowCount = rowCount;
            QuarantineRowCount = quarantineRowCount;
            ProfilingDate = profilingDate;
            ProfiledAttributes = profiledAttributes;
            CorruptAttributes = corruptAttributes;
            CustomInit();
        }

        /// <summary>
        /// An initialization method that performs custom operations like setting defaults
        /// </summary>
        partial void CustomInit();

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "qualifiedEntityName")]
        public string QualifiedEntityName { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "rowCount")]
        public long? RowCount { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "quarantineRowCount")]
        public long? QuarantineRowCount { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "profilingDate")]
        public System.DateTime? ProfilingDate { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "profiledAttributes")]
        public string ProfiledAttributes { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "corruptAttributes")]
        public string CorruptAttributes { get; set; }

    }
}
