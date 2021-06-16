// <auto-generated>
// Code generated by Microsoft (R) AutoRest Code Generator.
// Changes may cause incorrect behavior and will be lost if the code is
// regenerated.
// </auto-generated>

namespace Microsoft.Dynamics.CustomerInsights.Api.Models
{
    using Newtonsoft.Json;
    using System.Linq;

    public partial class InstanceCreationRequest
    {
        /// <summary>
        /// Initializes a new instance of the InstanceCreationRequest class.
        /// </summary>
        public InstanceCreationRequest()
        {
            CustomInit();
        }

        /// <summary>
        /// Initializes a new instance of the InstanceCreationRequest class.
        /// </summary>
        /// <param name="bapProvisioningType">Possible values include: 'skip',
        /// 'create', 'attach'</param>
        public InstanceCreationRequest(InstanceMetadata instanceMetadata = default(InstanceMetadata), ResourceMetadata byosaResourceMetadata = default(ResourceMetadata), ResourceMetadata cdsResourceMetadata = default(ResourceMetadata), ByoPbiProvisioningInfo byoPbiProvisioningInfo = default(ByoPbiProvisioningInfo), bool? isCdsMdlStorageEnabled = default(bool?), bool? isCiToByosaMigrationEnabled = default(bool?), string bapProvisioningType = default(string), bool? isPbiProvisioningRequired = default(bool?))
        {
            InstanceMetadata = instanceMetadata;
            ByosaResourceMetadata = byosaResourceMetadata;
            CdsResourceMetadata = cdsResourceMetadata;
            ByoPbiProvisioningInfo = byoPbiProvisioningInfo;
            IsCdsMdlStorageEnabled = isCdsMdlStorageEnabled;
            IsCiToByosaMigrationEnabled = isCiToByosaMigrationEnabled;
            BapProvisioningType = bapProvisioningType;
            IsPbiProvisioningRequired = isPbiProvisioningRequired;
            CustomInit();
        }

        /// <summary>
        /// An initialization method that performs custom operations like setting defaults
        /// </summary>
        partial void CustomInit();

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "instanceMetadata")]
        public InstanceMetadata InstanceMetadata { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "byosaResourceMetadata")]
        public ResourceMetadata ByosaResourceMetadata { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "cdsResourceMetadata")]
        public ResourceMetadata CdsResourceMetadata { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "byoPbiProvisioningInfo")]
        public ByoPbiProvisioningInfo ByoPbiProvisioningInfo { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "isCdsMdlStorageEnabled")]
        public bool? IsCdsMdlStorageEnabled { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "isCiToByosaMigrationEnabled")]
        public bool? IsCiToByosaMigrationEnabled { get; set; }

        /// <summary>
        /// Gets or sets possible values include: 'skip', 'create', 'attach'
        /// </summary>
        [JsonProperty(PropertyName = "bapProvisioningType")]
        public string BapProvisioningType { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "isPbiProvisioningRequired")]
        public bool? IsPbiProvisioningRequired { get; set; }

    }
}
