/**
 * Code generated by Microsoft (R) AutoRest Code Generator.
 * Changes may cause incorrect behavior and will be lost if the code is
 * regenerated.
 */

package com.microsoft.dynamics.customerinsights.apiclient.models;

import com.fasterxml.jackson.annotation.JsonProperty;

/**
 * Defines headers for Create-a-hierarchy operation.
 */
public class CreateAHierarchyHeaders {
    /**
     * Bearer.
     */
    @JsonProperty(value = "WWW-Authenticate")
    private String wWWAuthenticate;

    /**
     * Get bearer.
     *
     * @return the wWWAuthenticate value
     */
    public String wWWAuthenticate() {
        return this.wWWAuthenticate;
    }

    /**
     * Set bearer.
     *
     * @param wWWAuthenticate the wWWAuthenticate value to set
     * @return the CreateAHierarchyHeaders object itself.
     */
    public CreateAHierarchyHeaders withWWWAuthenticate(String wWWAuthenticate) {
        this.wWWAuthenticate = wWWAuthenticate;
        return this;
    }

}
