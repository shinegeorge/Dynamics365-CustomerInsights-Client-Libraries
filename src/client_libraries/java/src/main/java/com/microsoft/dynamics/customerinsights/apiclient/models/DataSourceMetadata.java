/**
 * Code generated by Microsoft (R) AutoRest Code Generator.
 * Changes may cause incorrect behavior and will be lost if the code is
 * regenerated.
 */

package com.microsoft.dynamics.customerinsights.apiclient.models;

import java.util.List;
import java.util.UUID;
import org.joda.time.DateTime;
import com.fasterxml.jackson.annotation.JsonProperty;

/**
 * Represents metadata for a Customer Insights data source.
 */
public class DataSourceMetadata {
    /**
     * Possible values include: 'salesforce', 'dynamics365', 'powerQuery',
     * 'attachCdm', 'attachCds', 'powerPlatform', 'datahub', 'cjoData',
     * 'eiData'.
     */
    @JsonProperty(value = "kind")
    private String kind;

    /**
     * Represents if still in active state.
     */
    @JsonProperty(value = "isActive")
    private Boolean isActive;

    /**
     * List of all Entity Names.
     */
    @JsonProperty(value = "entityNames")
    private List<String> entityNames;

    /**
     * The entitiesCount property.
     */
    @JsonProperty(value = "entitiesCount")
    private Integer entitiesCount;

    /**
     * Unique identity for this object.
     */
    @JsonProperty(value = "dataSourceId")
    private UUID dataSourceId;

    /**
     * Unique name of the dataSource.
     */
    @JsonProperty(value = "name")
    private String name;

    /**
     * FriendlyName of the dataSource.
     */
    @JsonProperty(value = "friendlyName")
    private String friendlyName;

    /**
     * Entity information, by entity name.
     */
    @JsonProperty(value = "entityInformation")
    private List<DatasourceEntityInformation> entityInformation;

    /**
     * Possible values include: 'new', 'creating', 'active', 'createFailed',
     * 'updateFailed', 'deleting', 'refreshCredentials',
     * 'resetInstanceInProgress', 'updating', 'quickUpdate', 'deactivated'.
     */
    @JsonProperty(value = "provisioningState")
    private String provisioningState;

    /**
     * Represents the time datasource was last refreshed.
     */
    @JsonProperty(value = "lastRefresh")
    private DateTime lastRefresh;

    /**
     * Possible values include: 'notUpdated', 'updated', 'updating',
     * 'updateFailed', 'updateCancelled'.
     */
    @JsonProperty(value = "refreshState")
    private String refreshState;

    /**
     * Incremental refresh properties for entities.
     */
    @JsonProperty(value = "incrementalRefreshProperties")
    private List<IncrementalRefreshProperties> incrementalRefreshProperties;

    /**
     * Model path for CDM data source.
     */
    @JsonProperty(value = "modelJsonPath")
    private String modelJsonPath;

    /**
     * Version number of this object.
     */
    @JsonProperty(value = "version")
    private Long version;

    /**
     * UPN of the user who last updated this record.
     */
    @JsonProperty(value = "updatedBy")
    private String updatedBy;

    /**
     * Time this object was last updated.
     */
    @JsonProperty(value = "updatedUtc")
    private DateTime updatedUtc;

    /**
     * Email address of the user who created this record.
     */
    @JsonProperty(value = "createdBy")
    private String createdBy;

    /**
     * Time this object was initially created.
     */
    @JsonProperty(value = "createdUtc")
    private DateTime createdUtc;

    /**
     * Customer Insights instance id associated with this object.
     */
    @JsonProperty(value = "instanceId")
    private UUID instanceId;

    /**
     * Get possible values include: 'salesforce', 'dynamics365', 'powerQuery', 'attachCdm', 'attachCds', 'powerPlatform', 'datahub', 'cjoData', 'eiData'.
     *
     * @return the kind value
     */
    public String kind() {
        return this.kind;
    }

    /**
     * Set possible values include: 'salesforce', 'dynamics365', 'powerQuery', 'attachCdm', 'attachCds', 'powerPlatform', 'datahub', 'cjoData', 'eiData'.
     *
     * @param kind the kind value to set
     * @return the DataSourceMetadata object itself.
     */
    public DataSourceMetadata withKind(String kind) {
        this.kind = kind;
        return this;
    }

    /**
     * Get represents if still in active state.
     *
     * @return the isActive value
     */
    public Boolean isActive() {
        return this.isActive;
    }

    /**
     * Set represents if still in active state.
     *
     * @param isActive the isActive value to set
     * @return the DataSourceMetadata object itself.
     */
    public DataSourceMetadata withIsActive(Boolean isActive) {
        this.isActive = isActive;
        return this;
    }

    /**
     * Get list of all Entity Names.
     *
     * @return the entityNames value
     */
    public List<String> entityNames() {
        return this.entityNames;
    }

    /**
     * Set list of all Entity Names.
     *
     * @param entityNames the entityNames value to set
     * @return the DataSourceMetadata object itself.
     */
    public DataSourceMetadata withEntityNames(List<String> entityNames) {
        this.entityNames = entityNames;
        return this;
    }

    /**
     * Get the entitiesCount value.
     *
     * @return the entitiesCount value
     */
    public Integer entitiesCount() {
        return this.entitiesCount;
    }

    /**
     * Set the entitiesCount value.
     *
     * @param entitiesCount the entitiesCount value to set
     * @return the DataSourceMetadata object itself.
     */
    public DataSourceMetadata withEntitiesCount(Integer entitiesCount) {
        this.entitiesCount = entitiesCount;
        return this;
    }

    /**
     * Get unique identity for this object.
     *
     * @return the dataSourceId value
     */
    public UUID dataSourceId() {
        return this.dataSourceId;
    }

    /**
     * Set unique identity for this object.
     *
     * @param dataSourceId the dataSourceId value to set
     * @return the DataSourceMetadata object itself.
     */
    public DataSourceMetadata withDataSourceId(UUID dataSourceId) {
        this.dataSourceId = dataSourceId;
        return this;
    }

    /**
     * Get unique name of the dataSource.
     *
     * @return the name value
     */
    public String name() {
        return this.name;
    }

    /**
     * Set unique name of the dataSource.
     *
     * @param name the name value to set
     * @return the DataSourceMetadata object itself.
     */
    public DataSourceMetadata withName(String name) {
        this.name = name;
        return this;
    }

    /**
     * Get friendlyName of the dataSource.
     *
     * @return the friendlyName value
     */
    public String friendlyName() {
        return this.friendlyName;
    }

    /**
     * Set friendlyName of the dataSource.
     *
     * @param friendlyName the friendlyName value to set
     * @return the DataSourceMetadata object itself.
     */
    public DataSourceMetadata withFriendlyName(String friendlyName) {
        this.friendlyName = friendlyName;
        return this;
    }

    /**
     * Get entity information, by entity name.
     *
     * @return the entityInformation value
     */
    public List<DatasourceEntityInformation> entityInformation() {
        return this.entityInformation;
    }

    /**
     * Set entity information, by entity name.
     *
     * @param entityInformation the entityInformation value to set
     * @return the DataSourceMetadata object itself.
     */
    public DataSourceMetadata withEntityInformation(List<DatasourceEntityInformation> entityInformation) {
        this.entityInformation = entityInformation;
        return this;
    }

    /**
     * Get possible values include: 'new', 'creating', 'active', 'createFailed', 'updateFailed', 'deleting', 'refreshCredentials', 'resetInstanceInProgress', 'updating', 'quickUpdate', 'deactivated'.
     *
     * @return the provisioningState value
     */
    public String provisioningState() {
        return this.provisioningState;
    }

    /**
     * Set possible values include: 'new', 'creating', 'active', 'createFailed', 'updateFailed', 'deleting', 'refreshCredentials', 'resetInstanceInProgress', 'updating', 'quickUpdate', 'deactivated'.
     *
     * @param provisioningState the provisioningState value to set
     * @return the DataSourceMetadata object itself.
     */
    public DataSourceMetadata withProvisioningState(String provisioningState) {
        this.provisioningState = provisioningState;
        return this;
    }

    /**
     * Get represents the time datasource was last refreshed.
     *
     * @return the lastRefresh value
     */
    public DateTime lastRefresh() {
        return this.lastRefresh;
    }

    /**
     * Set represents the time datasource was last refreshed.
     *
     * @param lastRefresh the lastRefresh value to set
     * @return the DataSourceMetadata object itself.
     */
    public DataSourceMetadata withLastRefresh(DateTime lastRefresh) {
        this.lastRefresh = lastRefresh;
        return this;
    }

    /**
     * Get possible values include: 'notUpdated', 'updated', 'updating', 'updateFailed', 'updateCancelled'.
     *
     * @return the refreshState value
     */
    public String refreshState() {
        return this.refreshState;
    }

    /**
     * Set possible values include: 'notUpdated', 'updated', 'updating', 'updateFailed', 'updateCancelled'.
     *
     * @param refreshState the refreshState value to set
     * @return the DataSourceMetadata object itself.
     */
    public DataSourceMetadata withRefreshState(String refreshState) {
        this.refreshState = refreshState;
        return this;
    }

    /**
     * Get incremental refresh properties for entities.
     *
     * @return the incrementalRefreshProperties value
     */
    public List<IncrementalRefreshProperties> incrementalRefreshProperties() {
        return this.incrementalRefreshProperties;
    }

    /**
     * Set incremental refresh properties for entities.
     *
     * @param incrementalRefreshProperties the incrementalRefreshProperties value to set
     * @return the DataSourceMetadata object itself.
     */
    public DataSourceMetadata withIncrementalRefreshProperties(List<IncrementalRefreshProperties> incrementalRefreshProperties) {
        this.incrementalRefreshProperties = incrementalRefreshProperties;
        return this;
    }

    /**
     * Get model path for CDM data source.
     *
     * @return the modelJsonPath value
     */
    public String modelJsonPath() {
        return this.modelJsonPath;
    }

    /**
     * Set model path for CDM data source.
     *
     * @param modelJsonPath the modelJsonPath value to set
     * @return the DataSourceMetadata object itself.
     */
    public DataSourceMetadata withModelJsonPath(String modelJsonPath) {
        this.modelJsonPath = modelJsonPath;
        return this;
    }

    /**
     * Get version number of this object.
     *
     * @return the version value
     */
    public Long version() {
        return this.version;
    }

    /**
     * Set version number of this object.
     *
     * @param version the version value to set
     * @return the DataSourceMetadata object itself.
     */
    public DataSourceMetadata withVersion(Long version) {
        this.version = version;
        return this;
    }

    /**
     * Get uPN of the user who last updated this record.
     *
     * @return the updatedBy value
     */
    public String updatedBy() {
        return this.updatedBy;
    }

    /**
     * Set uPN of the user who last updated this record.
     *
     * @param updatedBy the updatedBy value to set
     * @return the DataSourceMetadata object itself.
     */
    public DataSourceMetadata withUpdatedBy(String updatedBy) {
        this.updatedBy = updatedBy;
        return this;
    }

    /**
     * Get time this object was last updated.
     *
     * @return the updatedUtc value
     */
    public DateTime updatedUtc() {
        return this.updatedUtc;
    }

    /**
     * Set time this object was last updated.
     *
     * @param updatedUtc the updatedUtc value to set
     * @return the DataSourceMetadata object itself.
     */
    public DataSourceMetadata withUpdatedUtc(DateTime updatedUtc) {
        this.updatedUtc = updatedUtc;
        return this;
    }

    /**
     * Get email address of the user who created this record.
     *
     * @return the createdBy value
     */
    public String createdBy() {
        return this.createdBy;
    }

    /**
     * Set email address of the user who created this record.
     *
     * @param createdBy the createdBy value to set
     * @return the DataSourceMetadata object itself.
     */
    public DataSourceMetadata withCreatedBy(String createdBy) {
        this.createdBy = createdBy;
        return this;
    }

    /**
     * Get time this object was initially created.
     *
     * @return the createdUtc value
     */
    public DateTime createdUtc() {
        return this.createdUtc;
    }

    /**
     * Set time this object was initially created.
     *
     * @param createdUtc the createdUtc value to set
     * @return the DataSourceMetadata object itself.
     */
    public DataSourceMetadata withCreatedUtc(DateTime createdUtc) {
        this.createdUtc = createdUtc;
        return this;
    }

    /**
     * Get customer Insights instance id associated with this object.
     *
     * @return the instanceId value
     */
    public UUID instanceId() {
        return this.instanceId;
    }

    /**
     * Set customer Insights instance id associated with this object.
     *
     * @param instanceId the instanceId value to set
     * @return the DataSourceMetadata object itself.
     */
    public DataSourceMetadata withInstanceId(UUID instanceId) {
        this.instanceId = instanceId;
        return this;
    }

}
