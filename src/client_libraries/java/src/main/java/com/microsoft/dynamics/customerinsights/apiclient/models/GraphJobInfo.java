/**
 * Code generated by Microsoft (R) AutoRest Code Generator.
 * Changes may cause incorrect behavior and will be lost if the code is
 * regenerated.
 */

package com.microsoft.dynamics.customerinsights.apiclient.models;

import java.util.UUID;
import org.joda.time.DateTime;
import java.util.List;
import com.fasterxml.jackson.annotation.JsonProperty;

/**
 * The GraphJobInfo model.
 */
public class GraphJobInfo {
    /**
     * The jobId property.
     */
    @JsonProperty(value = "jobId")
    private UUID jobId;

    /**
     * Possible values include: 'full', 'incremental'.
     */
    @JsonProperty(value = "jobType")
    private String jobType;

    /**
     * Possible values include: 'onDemand', 'scheduled'.
     */
    @JsonProperty(value = "jobSubmissionKind")
    private String jobSubmissionKind;

    /**
     * Possible values include: 'queued', 'needsUpdate', 'running', 'failed',
     * 'timedOut', 'aborted', 'deleted', 'successful', 'skipped'.
     */
    @JsonProperty(value = "jobStatus")
    private String jobStatus;

    /**
     * Possible values include: 'none', 'ingestion', 'derivedEntity',
     * 'hierarchy', 'dataPreparation', 'map', 'realtimeM3Search', 'match',
     * 'merge', 'profileStore', 'search', 'activity', 'contact',
     * 'attributeMeasures', 'entityMeasures', 'measures', 'segmentation',
     * 'segmentMembership', 'enrichment', 'preEnrichment', 'transform',
     * 'intelligence', 'aiBuilder', 'insights', 'export', 'modelManagement',
     * 'relationship', 'roleAssignment', 'analysis', 'semanticEntity', 'all'.
     */
    @JsonProperty(value = "operationType")
    private String operationType;

    /**
     * Possible values include: 'noSubType', 'templatedMeasures',
     * 'createAnalysisModel', 'linkAnalysisModel', 'singleActivityMapping',
     * 'powerPlatform'.
     */
    @JsonProperty(value = "subType")
    private String subType;

    /**
     * The endTimestamp property.
     */
    @JsonProperty(value = "endTimestamp")
    private DateTime endTimestamp;

    /**
     * The shouldForceRunRequestedNodes property.
     */
    @JsonProperty(value = "shouldForceRunRequestedNodes")
    private Boolean shouldForceRunRequestedNodes;

    /**
     * The tasks property.
     */
    @JsonProperty(value = "tasks")
    private List<GraphTaskInfo> tasks;

    /**
     * The idList property.
     */
    @JsonProperty(value = "idList")
    private List<String> idList;

    /**
     * The options property.
     */
    @JsonProperty(value = "options")
    private GraphJobOptions options;

    /**
     * The submittedTimestamp property.
     */
    @JsonProperty(value = "submittedTimestamp")
    private DateTime submittedTimestamp;

    /**
     * Get the jobId value.
     *
     * @return the jobId value
     */
    public UUID jobId() {
        return this.jobId;
    }

    /**
     * Set the jobId value.
     *
     * @param jobId the jobId value to set
     * @return the GraphJobInfo object itself.
     */
    public GraphJobInfo withJobId(UUID jobId) {
        this.jobId = jobId;
        return this;
    }

    /**
     * Get possible values include: 'full', 'incremental'.
     *
     * @return the jobType value
     */
    public String jobType() {
        return this.jobType;
    }

    /**
     * Set possible values include: 'full', 'incremental'.
     *
     * @param jobType the jobType value to set
     * @return the GraphJobInfo object itself.
     */
    public GraphJobInfo withJobType(String jobType) {
        this.jobType = jobType;
        return this;
    }

    /**
     * Get possible values include: 'onDemand', 'scheduled'.
     *
     * @return the jobSubmissionKind value
     */
    public String jobSubmissionKind() {
        return this.jobSubmissionKind;
    }

    /**
     * Set possible values include: 'onDemand', 'scheduled'.
     *
     * @param jobSubmissionKind the jobSubmissionKind value to set
     * @return the GraphJobInfo object itself.
     */
    public GraphJobInfo withJobSubmissionKind(String jobSubmissionKind) {
        this.jobSubmissionKind = jobSubmissionKind;
        return this;
    }

    /**
     * Get possible values include: 'queued', 'needsUpdate', 'running', 'failed', 'timedOut', 'aborted', 'deleted', 'successful', 'skipped'.
     *
     * @return the jobStatus value
     */
    public String jobStatus() {
        return this.jobStatus;
    }

    /**
     * Set possible values include: 'queued', 'needsUpdate', 'running', 'failed', 'timedOut', 'aborted', 'deleted', 'successful', 'skipped'.
     *
     * @param jobStatus the jobStatus value to set
     * @return the GraphJobInfo object itself.
     */
    public GraphJobInfo withJobStatus(String jobStatus) {
        this.jobStatus = jobStatus;
        return this;
    }

    /**
     * Get possible values include: 'none', 'ingestion', 'derivedEntity', 'hierarchy', 'dataPreparation', 'map', 'realtimeM3Search', 'match', 'merge', 'profileStore', 'search', 'activity', 'contact', 'attributeMeasures', 'entityMeasures', 'measures', 'segmentation', 'segmentMembership', 'enrichment', 'preEnrichment', 'transform', 'intelligence', 'aiBuilder', 'insights', 'export', 'modelManagement', 'relationship', 'roleAssignment', 'analysis', 'semanticEntity', 'all'.
     *
     * @return the operationType value
     */
    public String operationType() {
        return this.operationType;
    }

    /**
     * Set possible values include: 'none', 'ingestion', 'derivedEntity', 'hierarchy', 'dataPreparation', 'map', 'realtimeM3Search', 'match', 'merge', 'profileStore', 'search', 'activity', 'contact', 'attributeMeasures', 'entityMeasures', 'measures', 'segmentation', 'segmentMembership', 'enrichment', 'preEnrichment', 'transform', 'intelligence', 'aiBuilder', 'insights', 'export', 'modelManagement', 'relationship', 'roleAssignment', 'analysis', 'semanticEntity', 'all'.
     *
     * @param operationType the operationType value to set
     * @return the GraphJobInfo object itself.
     */
    public GraphJobInfo withOperationType(String operationType) {
        this.operationType = operationType;
        return this;
    }

    /**
     * Get possible values include: 'noSubType', 'templatedMeasures', 'createAnalysisModel', 'linkAnalysisModel', 'singleActivityMapping', 'powerPlatform'.
     *
     * @return the subType value
     */
    public String subType() {
        return this.subType;
    }

    /**
     * Set possible values include: 'noSubType', 'templatedMeasures', 'createAnalysisModel', 'linkAnalysisModel', 'singleActivityMapping', 'powerPlatform'.
     *
     * @param subType the subType value to set
     * @return the GraphJobInfo object itself.
     */
    public GraphJobInfo withSubType(String subType) {
        this.subType = subType;
        return this;
    }

    /**
     * Get the endTimestamp value.
     *
     * @return the endTimestamp value
     */
    public DateTime endTimestamp() {
        return this.endTimestamp;
    }

    /**
     * Set the endTimestamp value.
     *
     * @param endTimestamp the endTimestamp value to set
     * @return the GraphJobInfo object itself.
     */
    public GraphJobInfo withEndTimestamp(DateTime endTimestamp) {
        this.endTimestamp = endTimestamp;
        return this;
    }

    /**
     * Get the shouldForceRunRequestedNodes value.
     *
     * @return the shouldForceRunRequestedNodes value
     */
    public Boolean shouldForceRunRequestedNodes() {
        return this.shouldForceRunRequestedNodes;
    }

    /**
     * Set the shouldForceRunRequestedNodes value.
     *
     * @param shouldForceRunRequestedNodes the shouldForceRunRequestedNodes value to set
     * @return the GraphJobInfo object itself.
     */
    public GraphJobInfo withShouldForceRunRequestedNodes(Boolean shouldForceRunRequestedNodes) {
        this.shouldForceRunRequestedNodes = shouldForceRunRequestedNodes;
        return this;
    }

    /**
     * Get the tasks value.
     *
     * @return the tasks value
     */
    public List<GraphTaskInfo> tasks() {
        return this.tasks;
    }

    /**
     * Set the tasks value.
     *
     * @param tasks the tasks value to set
     * @return the GraphJobInfo object itself.
     */
    public GraphJobInfo withTasks(List<GraphTaskInfo> tasks) {
        this.tasks = tasks;
        return this;
    }

    /**
     * Get the idList value.
     *
     * @return the idList value
     */
    public List<String> idList() {
        return this.idList;
    }

    /**
     * Set the idList value.
     *
     * @param idList the idList value to set
     * @return the GraphJobInfo object itself.
     */
    public GraphJobInfo withIdList(List<String> idList) {
        this.idList = idList;
        return this;
    }

    /**
     * Get the options value.
     *
     * @return the options value
     */
    public GraphJobOptions options() {
        return this.options;
    }

    /**
     * Set the options value.
     *
     * @param options the options value to set
     * @return the GraphJobInfo object itself.
     */
    public GraphJobInfo withOptions(GraphJobOptions options) {
        this.options = options;
        return this;
    }

    /**
     * Get the submittedTimestamp value.
     *
     * @return the submittedTimestamp value
     */
    public DateTime submittedTimestamp() {
        return this.submittedTimestamp;
    }

    /**
     * Set the submittedTimestamp value.
     *
     * @param submittedTimestamp the submittedTimestamp value to set
     * @return the GraphJobInfo object itself.
     */
    public GraphJobInfo withSubmittedTimestamp(DateTime submittedTimestamp) {
        this.submittedTimestamp = submittedTimestamp;
        return this;
    }

}
