/**
 * Code generated by Microsoft (R) AutoRest Code Generator.
 * Changes may cause incorrect behavior and will be lost if the code is
 * regenerated.
 */

package com.microsoft.dynamics.customerinsights.apiclient.models;

import java.util.List;
import com.fasterxml.jackson.annotation.JsonProperty;

/**
 * Represents the entity info used in API requests (entity level).
 */
public class DatasourceEntityInformation {
    /**
     * Name of the entity.
     */
    @JsonProperty(value = "entityName")
    private String entityName;

    /**
     * Primary key name of the entity. We require the entity to have a single
     * column primary key column.
     */
    @JsonProperty(value = "primaryKey")
    private String primaryKey;

    /**
     * Possible values include: 'unspecified', 'profile', 'conflationMap',
     * 'activity', 'aggregateKpi', 'profileKpi', 'unifiedActivity', 'segment',
     * 'intelligence', 'genericPrediction', 'enrichment', 'insights',
     * 'derivedEntity', 'corrupt', 'selfConflation', 'conflationManualReview',
     * 'selfConflationManualReview', 'semanticActivity', 'segmentMembership'.
     */
    @JsonProperty(value = "entityType")
    private String entityType;

    /**
     * Time stamp field name.
     */
    @JsonProperty(value = "timestampFieldName")
    private String timestampFieldName;

    /**
     * Semantic labels by attribute name.
     */
    @JsonProperty(value = "semanticLabels")
    private List<AttributeSemanticInformation> semanticLabels;

    /**
     * Get name of the entity.
     *
     * @return the entityName value
     */
    public String entityName() {
        return this.entityName;
    }

    /**
     * Set name of the entity.
     *
     * @param entityName the entityName value to set
     * @return the DatasourceEntityInformation object itself.
     */
    public DatasourceEntityInformation withEntityName(String entityName) {
        this.entityName = entityName;
        return this;
    }

    /**
     * Get primary key name of the entity. We require the entity to have a single column primary key column.
     *
     * @return the primaryKey value
     */
    public String primaryKey() {
        return this.primaryKey;
    }

    /**
     * Set primary key name of the entity. We require the entity to have a single column primary key column.
     *
     * @param primaryKey the primaryKey value to set
     * @return the DatasourceEntityInformation object itself.
     */
    public DatasourceEntityInformation withPrimaryKey(String primaryKey) {
        this.primaryKey = primaryKey;
        return this;
    }

    /**
     * Get possible values include: 'unspecified', 'profile', 'conflationMap', 'activity', 'aggregateKpi', 'profileKpi', 'unifiedActivity', 'segment', 'intelligence', 'genericPrediction', 'enrichment', 'insights', 'derivedEntity', 'corrupt', 'selfConflation', 'conflationManualReview', 'selfConflationManualReview', 'semanticActivity', 'segmentMembership'.
     *
     * @return the entityType value
     */
    public String entityType() {
        return this.entityType;
    }

    /**
     * Set possible values include: 'unspecified', 'profile', 'conflationMap', 'activity', 'aggregateKpi', 'profileKpi', 'unifiedActivity', 'segment', 'intelligence', 'genericPrediction', 'enrichment', 'insights', 'derivedEntity', 'corrupt', 'selfConflation', 'conflationManualReview', 'selfConflationManualReview', 'semanticActivity', 'segmentMembership'.
     *
     * @param entityType the entityType value to set
     * @return the DatasourceEntityInformation object itself.
     */
    public DatasourceEntityInformation withEntityType(String entityType) {
        this.entityType = entityType;
        return this;
    }

    /**
     * Get time stamp field name.
     *
     * @return the timestampFieldName value
     */
    public String timestampFieldName() {
        return this.timestampFieldName;
    }

    /**
     * Set time stamp field name.
     *
     * @param timestampFieldName the timestampFieldName value to set
     * @return the DatasourceEntityInformation object itself.
     */
    public DatasourceEntityInformation withTimestampFieldName(String timestampFieldName) {
        this.timestampFieldName = timestampFieldName;
        return this;
    }

    /**
     * Get semantic labels by attribute name.
     *
     * @return the semanticLabels value
     */
    public List<AttributeSemanticInformation> semanticLabels() {
        return this.semanticLabels;
    }

    /**
     * Set semantic labels by attribute name.
     *
     * @param semanticLabels the semanticLabels value to set
     * @return the DatasourceEntityInformation object itself.
     */
    public DatasourceEntityInformation withSemanticLabels(List<AttributeSemanticInformation> semanticLabels) {
        this.semanticLabels = semanticLabels;
        return this;
    }

}
