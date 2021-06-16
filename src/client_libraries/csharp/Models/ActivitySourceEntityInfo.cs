// <auto-generated>
// Code generated by Microsoft (R) AutoRest Code Generator.
// Changes may cause incorrect behavior and will be lost if the code is
// regenerated.
// </auto-generated>

namespace Microsoft.Dynamics.CustomerInsights.Api.Models
{
    using Newtonsoft.Json;
    using System.Linq;

    /// <summary>
    /// Collection of the entity name and other info of the source activity
    /// entity ingested by user.
    /// </summary>
    public partial class ActivitySourceEntityInfo
    {
        /// <summary>
        /// Initializes a new instance of the ActivitySourceEntityInfo class.
        /// </summary>
        public ActivitySourceEntityInfo()
        {
            CustomInit();
        }

        /// <summary>
        /// Initializes a new instance of the ActivitySourceEntityInfo class.
        /// </summary>
        /// <param name="entityName">Gets the qualified entity name of the
        /// activity source entity.</param>
        public ActivitySourceEntityInfo(string entityName = default(string))
        {
            EntityName = entityName;
            CustomInit();
        }

        /// <summary>
        /// An initialization method that performs custom operations like setting defaults
        /// </summary>
        partial void CustomInit();

        /// <summary>
        /// Gets the qualified entity name of the activity source entity.
        /// </summary>
        [JsonProperty(PropertyName = "entityName")]
        public string EntityName { get; set; }

    }
}
