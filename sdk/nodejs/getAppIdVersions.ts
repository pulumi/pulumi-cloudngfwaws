// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Data source get a list of AppId versions.
 *
 * ## Admin Permission Type
 *
 * * `Rulestack`
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as cloudngfwaws from "@pulumi/cloudngfwaws";
 *
 * const example = cloudngfwaws.getAppIdVersions({});
 * ```
 */
export function getAppIdVersions(args?: GetAppIdVersionsArgs, opts?: pulumi.InvokeOptions): Promise<GetAppIdVersionsResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("cloudngfwaws:index/getAppIdVersions:getAppIdVersions", {
        "maxResults": args.maxResults,
        "token": args.token,
    }, opts);
}

/**
 * A collection of arguments for invoking getAppIdVersions.
 */
export interface GetAppIdVersionsArgs {
    /**
     * Max number of results. Defaults to `100`.
     */
    maxResults?: number;
    /**
     * Pagination token.
     */
    token?: string;
}

/**
 * A collection of values returned by getAppIdVersions.
 */
export interface GetAppIdVersionsResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * Max number of results. Defaults to `100`.
     */
    readonly maxResults?: number;
    /**
     * Token for the next page of results.
     */
    readonly nextToken: string;
    /**
     * Pagination token.
     */
    readonly token?: string;
    /**
     * List of AppId versions.
     */
    readonly versions: string[];
}
/**
 * Data source get a list of AppId versions.
 *
 * ## Admin Permission Type
 *
 * * `Rulestack`
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as cloudngfwaws from "@pulumi/cloudngfwaws";
 *
 * const example = cloudngfwaws.getAppIdVersions({});
 * ```
 */
export function getAppIdVersionsOutput(args?: GetAppIdVersionsOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetAppIdVersionsResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("cloudngfwaws:index/getAppIdVersions:getAppIdVersions", {
        "maxResults": args.maxResults,
        "token": args.token,
    }, opts);
}

/**
 * A collection of arguments for invoking getAppIdVersions.
 */
export interface GetAppIdVersionsOutputArgs {
    /**
     * Max number of results. Defaults to `100`.
     */
    maxResults?: pulumi.Input<number>;
    /**
     * Pagination token.
     */
    token?: pulumi.Input<string>;
}
