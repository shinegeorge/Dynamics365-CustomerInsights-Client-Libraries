/**
 * Code generated by Microsoft (R) AutoRest Code Generator.
 * Changes may cause incorrect behavior and will be lost if the code is
 * regenerated.
 */

package com.microsoft.dynamics.customerinsights.apiclient.models;

import org.joda.time.DateTime;
import java.util.List;
import com.fasterxml.jackson.annotation.JsonProperty;

/**
 * Represents Entity Data Profile information.
 */
public class EntityDataProfile {
    /**
     * Qualified Entity Name.
     */
    @JsonProperty(value = "qualifiedEntityName")
    private String qualifiedEntityName;

    /**
     * Row count.
     */
    @JsonProperty(value = "rowCount")
    private Long rowCount;

    /**
     * Quarentine row count.
     */
    @JsonProperty(value = "quarantineRowCount")
    private Long quarantineRowCount;

    /**
     * Date for Profiling.
     */
    @JsonProperty(value = "profilingDate")
    private DateTime profilingDate;

    /**
     * Profiling attributes.
     */
    @JsonProperty(value = "profiledAttributes")
    private String profiledAttributes;

    /**
     * Respresents currupt attributes.
     */
    @JsonProperty(value = "corruptAttributes")
    private String corruptAttributes;

    /**
     * Contains all the attributes data profiles.
     */
    @JsonProperty(value = "attributeDataProfiles")
    private List<AttributeDataProfile> attributeDataProfiles;

    /**
     * Get qualified Entity Name.
     *
     * @return the qualifiedEntityName value
     */
    public String qualifiedEntityName() {
        return this.qualifiedEntityName;
    }

    /**
     * Set qualified Entity Name.
     *
     * @param qualifiedEntityName the qualifiedEntityName value to set
     * @return the EntityDataProfile object itself.
     */
    public EntityDataProfile withQualifiedEntityName(String qualifiedEntityName) {
        this.qualifiedEntityName = qualifiedEntityName;
        return this;
    }

    /**
     * Get row count.
     *
     * @return the rowCount value
     */
    public Long rowCount() {
        return this.rowCount;
    }

    /**
     * Set row count.
     *
     * @param rowCount the rowCount value to set
     * @return the EntityDataProfile object itself.
     */
    public EntityDataProfile withRowCount(Long rowCount) {
        this.rowCount = rowCount;
        return this;
    }

    /**
     * Get quarentine row count.
     *
     * @return the quarantineRowCount value
     */
    public Long quarantineRowCount() {
        return this.quarantineRowCount;
    }

    /**
     * Set quarentine row count.
     *
     * @param quarantineRowCount the quarantineRowCount value to set
     * @return the EntityDataProfile object itself.
     */
    public EntityDataProfile withQuarantineRowCount(Long quarantineRowCount) {
        this.quarantineRowCount = quarantineRowCount;
        return this;
    }

    /**
     * Get date for Profiling.
     *
     * @return the profilingDate value
     */
    public DateTime profilingDate() {
        return this.profilingDate;
    }

    /**
     * Set date for Profiling.
     *
     * @param profilingDate the profilingDate value to set
     * @return the EntityDataProfile object itself.
     */
    public EntityDataProfile withProfilingDate(DateTime profilingDate) {
        this.profilingDate = profilingDate;
        return this;
    }

    /**
     * Get profiling attributes.
     *
     * @return the profiledAttributes value
     */
    public String profiledAttributes() {
        return this.profiledAttributes;
    }

    /**
     * Set profiling attributes.
     *
     * @param profiledAttributes the profiledAttributes value to set
     * @return the EntityDataProfile object itself.
     */
    public EntityDataProfile withProfiledAttributes(String profiledAttributes) {
        this.profiledAttributes = profiledAttributes;
        return this;
    }

    /**
     * Get respresents currupt attributes.
     *
     * @return the corruptAttributes value
     */
    public String corruptAttributes() {
        return this.corruptAttributes;
    }

    /**
     * Set respresents currupt attributes.
     *
     * @param corruptAttributes the corruptAttributes value to set
     * @return the EntityDataProfile object itself.
     */
    public EntityDataProfile withCorruptAttributes(String corruptAttributes) {
        this.corruptAttributes = corruptAttributes;
        return this;
    }

    /**
     * Get contains all the attributes data profiles.
     *
     * @return the attributeDataProfiles value
     */
    public List<AttributeDataProfile> attributeDataProfiles() {
        return this.attributeDataProfiles;
    }

    /**
     * Set contains all the attributes data profiles.
     *
     * @param attributeDataProfiles the attributeDataProfiles value to set
     * @return the EntityDataProfile object itself.
     */
    public EntityDataProfile withAttributeDataProfiles(List<AttributeDataProfile> attributeDataProfiles) {
        this.attributeDataProfiles = attributeDataProfiles;
        return this;
    }

}
