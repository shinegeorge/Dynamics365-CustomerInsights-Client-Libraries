/**
 * Code generated by Microsoft (R) AutoRest Code Generator.
 * Changes may cause incorrect behavior and will be lost if the code is
 * regenerated.
 */

package com.microsoft.dynamics.customerinsights.apiclient.models;

import java.util.List;
import java.util.UUID;
import com.fasterxml.jackson.annotation.JsonProperty;

/**
 * Represents a DAG refresh schedule.
 */
public class WorkflowRefreshSchedule {
    /**
     * Possible values include: 'none', 'ingestion', 'derivedEntity',
     * 'hierarchy', 'dataPreparation', 'map', 'realtimeM3Search', 'match',
     * 'merge', 'profileStore', 'search', 'activity', 'attributeMeasures',
     * 'entityMeasures', 'measures', 'segmentation', 'segmentMembership',
     * 'enrichment', 'intelligence', 'aiBuilder', 'insights', 'export',
     * 'modelManagement', 'relationship', 'roleAssignment', 'analysis', 'all'.
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
     * Gets the identifiers of the schedule.
     */
    @JsonProperty(value = "identifiers")
    private List<String> identifiers;

    /**
     * Possible values include: 'full', 'incremental'.
     */
    @JsonProperty(value = "jobType")
    private String jobType;

    /**
     * Gets a value indicating whether the schedule is active.
     */
    @JsonProperty(value = "isActive")
    private Boolean isActive;

    /**
     * Gets the ID of the timezone.
     */
    @JsonProperty(value = "timezoneId")
    private String timezoneId;

    /**
     * Gets the schedule in CRON format.
     */
    @JsonProperty(value = "cronSchedules")
    private List<String> cronSchedules;

    /**
     * Gets the ID of the schedule.
     */
    @JsonProperty(value = "scheduleId")
    private UUID scheduleId;

    /**
     * Customer Insights instance id associated with this object.
     */
    @JsonProperty(value = "instanceId")
    private UUID instanceId;

    /**
     * Get possible values include: 'none', 'ingestion', 'derivedEntity', 'hierarchy', 'dataPreparation', 'map', 'realtimeM3Search', 'match', 'merge', 'profileStore', 'search', 'activity', 'attributeMeasures', 'entityMeasures', 'measures', 'segmentation', 'segmentMembership', 'enrichment', 'intelligence', 'aiBuilder', 'insights', 'export', 'modelManagement', 'relationship', 'roleAssignment', 'analysis', 'all'.
     *
     * @return the operationType value
     */
    public String operationType() {
        return this.operationType;
    }

    /**
     * Set possible values include: 'none', 'ingestion', 'derivedEntity', 'hierarchy', 'dataPreparation', 'map', 'realtimeM3Search', 'match', 'merge', 'profileStore', 'search', 'activity', 'attributeMeasures', 'entityMeasures', 'measures', 'segmentation', 'segmentMembership', 'enrichment', 'intelligence', 'aiBuilder', 'insights', 'export', 'modelManagement', 'relationship', 'roleAssignment', 'analysis', 'all'.
     *
     * @param operationType the operationType value to set
     * @return the WorkflowRefreshSchedule object itself.
     */
    public WorkflowRefreshSchedule withOperationType(String operationType) {
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
     * @return the WorkflowRefreshSchedule object itself.
     */
    public WorkflowRefreshSchedule withSubType(String subType) {
        this.subType = subType;
        return this;
    }

    /**
     * Get gets the identifiers of the schedule.
     *
     * @return the identifiers value
     */
    public List<String> identifiers() {
        return this.identifiers;
    }

    /**
     * Set gets the identifiers of the schedule.
     *
     * @param identifiers the identifiers value to set
     * @return the WorkflowRefreshSchedule object itself.
     */
    public WorkflowRefreshSchedule withIdentifiers(List<String> identifiers) {
        this.identifiers = identifiers;
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
     * @return the WorkflowRefreshSchedule object itself.
     */
    public WorkflowRefreshSchedule withJobType(String jobType) {
        this.jobType = jobType;
        return this;
    }

    /**
     * Get gets a value indicating whether the schedule is active.
     *
     * @return the isActive value
     */
    public Boolean isActive() {
        return this.isActive;
    }

    /**
     * Set gets a value indicating whether the schedule is active.
     *
     * @param isActive the isActive value to set
     * @return the WorkflowRefreshSchedule object itself.
     */
    public WorkflowRefreshSchedule withIsActive(Boolean isActive) {
        this.isActive = isActive;
        return this;
    }

    /**
     * Get gets the ID of the timezone.
     *
     * @return the timezoneId value
     */
    public String timezoneId() {
        return this.timezoneId;
    }

    /**
     * Set gets the ID of the timezone.
     *
     * @param timezoneId the timezoneId value to set
     * @return the WorkflowRefreshSchedule object itself.
     */
    public WorkflowRefreshSchedule withTimezoneId(String timezoneId) {
        this.timezoneId = timezoneId;
        return this;
    }

    /**
     * Get gets the schedule in CRON format.
     *
     * @return the cronSchedules value
     */
    public List<String> cronSchedules() {
        return this.cronSchedules;
    }

    /**
     * Set gets the schedule in CRON format.
     *
     * @param cronSchedules the cronSchedules value to set
     * @return the WorkflowRefreshSchedule object itself.
     */
    public WorkflowRefreshSchedule withCronSchedules(List<String> cronSchedules) {
        this.cronSchedules = cronSchedules;
        return this;
    }

    /**
     * Get gets the ID of the schedule.
     *
     * @return the scheduleId value
     */
    public UUID scheduleId() {
        return this.scheduleId;
    }

    /**
     * Set gets the ID of the schedule.
     *
     * @param scheduleId the scheduleId value to set
     * @return the WorkflowRefreshSchedule object itself.
     */
    public WorkflowRefreshSchedule withScheduleId(UUID scheduleId) {
        this.scheduleId = scheduleId;
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
     * @return the WorkflowRefreshSchedule object itself.
     */
    public WorkflowRefreshSchedule withInstanceId(UUID instanceId) {
        this.instanceId = instanceId;
        return this;
    }

}
