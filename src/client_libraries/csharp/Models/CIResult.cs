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
    /// Represents response result type
    /// </summary>
    public partial class CIResult
    {
        /// <summary>
        /// Initializes a new instance of the CIResult class.
        /// </summary>
        public CIResult()
        {
            CustomInit();
        }

        /// <summary>
        /// Initializes a new instance of the CIResult class.
        /// </summary>
        /// <param name="exceptionCulprit">Possible values include: 'system',
        /// 'user', 'external'</param>
        /// <param name="resultSeverity">Possible values include: 'error',
        /// 'warning', 'recommendation'</param>
        /// <param name="message">Message providing more information about the
        /// event.</param>
        /// <param name="name">Message providing more information about the
        /// event.</param>
        /// <param name="ciResults">List of CiResult contining CI result error
        /// code and information (if any).</param>
        public CIResult(string exceptionCulprit = default(string), string errorCode = default(string), string resultSeverity = default(string), string message = default(string), string name = default(string), IDictionary<string, object> paramsProperty = default(IDictionary<string, object>), IList<CIResult> ciResults = default(IList<CIResult>))
        {
            ExceptionCulprit = exceptionCulprit;
            ErrorCode = errorCode;
            ResultSeverity = resultSeverity;
            Message = message;
            Name = name;
            ParamsProperty = paramsProperty;
            CiResults = ciResults;
            CustomInit();
        }

        /// <summary>
        /// An initialization method that performs custom operations like setting defaults
        /// </summary>
        partial void CustomInit();

        /// <summary>
        /// Gets or sets possible values include: 'system', 'user', 'external'
        /// </summary>
        [JsonProperty(PropertyName = "exceptionCulprit")]
        public string ExceptionCulprit { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "errorCode")]
        public string ErrorCode { get; set; }

        /// <summary>
        /// Gets or sets possible values include: 'error', 'warning',
        /// 'recommendation'
        /// </summary>
        [JsonProperty(PropertyName = "resultSeverity")]
        public string ResultSeverity { get; set; }

        /// <summary>
        /// Gets or sets message providing more information about the event.
        /// </summary>
        [JsonProperty(PropertyName = "message")]
        public string Message { get; set; }

        /// <summary>
        /// Gets or sets message providing more information about the event.
        /// </summary>
        [JsonProperty(PropertyName = "name")]
        public string Name { get; set; }

        /// <summary>
        /// </summary>
        [JsonProperty(PropertyName = "params")]
        public IDictionary<string, object> ParamsProperty { get; set; }

        /// <summary>
        /// Gets or sets list of CiResult contining CI result error code and
        /// information (if any).
        /// </summary>
        [JsonProperty(PropertyName = "ciResults")]
        public IList<CIResult> CiResults { get; set; }

    }
}
