// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudngfwaws

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-cloudngfwaws/sdk/go/cloudngfwaws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Data source for retrieving a predefined URL category override.
//
// ## Admin Permission Type
//
// * `Rulestack` (for `scope="Local"`)
// * `Global Rulestack` (for `scope="Global"`)
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi-cloudngfwaws/sdk/go/cloudngfwaws"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			r, err := cloudngfwaws.NewRulestack(ctx, "r", &cloudngfwaws.RulestackArgs{
//				Name:        pulumi.String("my-rulestack"),
//				Scope:       pulumi.String("Local"),
//				AccountId:   pulumi.String("12345"),
//				Description: pulumi.String("Made by Pulumi"),
//				ProfileConfig: &cloudngfwaws.RulestackProfileConfigArgs{
//					AntiSpyware: pulumi.String("BestPractice"),
//				},
//			})
//			if err != nil {
//				return err
//			}
//			_ = cloudngfwaws.LookupPredefinedUrlCategoryOverrideOutput(ctx, cloudngfwaws.GetPredefinedUrlCategoryOverrideOutputArgs{
//				Rulestack: r.Name,
//				Name:      pulumi.String("foobar"),
//			}, nil)
//			return nil
//		})
//	}
//
// ```
func LookupPredefinedUrlCategoryOverride(ctx *pulumi.Context, args *LookupPredefinedUrlCategoryOverrideArgs, opts ...pulumi.InvokeOption) (*LookupPredefinedUrlCategoryOverrideResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupPredefinedUrlCategoryOverrideResult
	err := ctx.Invoke("cloudngfwaws:index/getPredefinedUrlCategoryOverride:getPredefinedUrlCategoryOverride", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getPredefinedUrlCategoryOverride.
type LookupPredefinedUrlCategoryOverrideArgs struct {
	// Retrieve either the candidate or running config. Valid values are `candidate` or `running`. Defaults to `candidate`.
	ConfigType *string `pulumi:"configType"`
	// The name.
	Name string `pulumi:"name"`
	// The rulestack.
	Rulestack string `pulumi:"rulestack"`
}

// A collection of values returned by getPredefinedUrlCategoryOverride.
type LookupPredefinedUrlCategoryOverrideResult struct {
	// The action to take. Valid values are `none`, `allow`, `alert`, or `block`.
	Action string `pulumi:"action"`
	// The audit comment.
	AuditComment string `pulumi:"auditComment"`
	// Retrieve either the candidate or running config. Valid values are `candidate` or `running`. Defaults to `candidate`.
	ConfigType *string `pulumi:"configType"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The name.
	Name string `pulumi:"name"`
	// The rulestack.
	Rulestack string `pulumi:"rulestack"`
	// Update token.
	UpdateToken string `pulumi:"updateToken"`
}

func LookupPredefinedUrlCategoryOverrideOutput(ctx *pulumi.Context, args LookupPredefinedUrlCategoryOverrideOutputArgs, opts ...pulumi.InvokeOption) LookupPredefinedUrlCategoryOverrideResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupPredefinedUrlCategoryOverrideResultOutput, error) {
			args := v.(LookupPredefinedUrlCategoryOverrideArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv LookupPredefinedUrlCategoryOverrideResult
			secret, err := ctx.InvokePackageRaw("cloudngfwaws:index/getPredefinedUrlCategoryOverride:getPredefinedUrlCategoryOverride", args, &rv, "", opts...)
			if err != nil {
				return LookupPredefinedUrlCategoryOverrideResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(LookupPredefinedUrlCategoryOverrideResultOutput)
			if secret {
				return pulumi.ToSecret(output).(LookupPredefinedUrlCategoryOverrideResultOutput), nil
			}
			return output, nil
		}).(LookupPredefinedUrlCategoryOverrideResultOutput)
}

// A collection of arguments for invoking getPredefinedUrlCategoryOverride.
type LookupPredefinedUrlCategoryOverrideOutputArgs struct {
	// Retrieve either the candidate or running config. Valid values are `candidate` or `running`. Defaults to `candidate`.
	ConfigType pulumi.StringPtrInput `pulumi:"configType"`
	// The name.
	Name pulumi.StringInput `pulumi:"name"`
	// The rulestack.
	Rulestack pulumi.StringInput `pulumi:"rulestack"`
}

func (LookupPredefinedUrlCategoryOverrideOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPredefinedUrlCategoryOverrideArgs)(nil)).Elem()
}

// A collection of values returned by getPredefinedUrlCategoryOverride.
type LookupPredefinedUrlCategoryOverrideResultOutput struct{ *pulumi.OutputState }

func (LookupPredefinedUrlCategoryOverrideResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPredefinedUrlCategoryOverrideResult)(nil)).Elem()
}

func (o LookupPredefinedUrlCategoryOverrideResultOutput) ToLookupPredefinedUrlCategoryOverrideResultOutput() LookupPredefinedUrlCategoryOverrideResultOutput {
	return o
}

func (o LookupPredefinedUrlCategoryOverrideResultOutput) ToLookupPredefinedUrlCategoryOverrideResultOutputWithContext(ctx context.Context) LookupPredefinedUrlCategoryOverrideResultOutput {
	return o
}

// The action to take. Valid values are `none`, `allow`, `alert`, or `block`.
func (o LookupPredefinedUrlCategoryOverrideResultOutput) Action() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPredefinedUrlCategoryOverrideResult) string { return v.Action }).(pulumi.StringOutput)
}

// The audit comment.
func (o LookupPredefinedUrlCategoryOverrideResultOutput) AuditComment() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPredefinedUrlCategoryOverrideResult) string { return v.AuditComment }).(pulumi.StringOutput)
}

// Retrieve either the candidate or running config. Valid values are `candidate` or `running`. Defaults to `candidate`.
func (o LookupPredefinedUrlCategoryOverrideResultOutput) ConfigType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupPredefinedUrlCategoryOverrideResult) *string { return v.ConfigType }).(pulumi.StringPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupPredefinedUrlCategoryOverrideResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPredefinedUrlCategoryOverrideResult) string { return v.Id }).(pulumi.StringOutput)
}

// The name.
func (o LookupPredefinedUrlCategoryOverrideResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPredefinedUrlCategoryOverrideResult) string { return v.Name }).(pulumi.StringOutput)
}

// The rulestack.
func (o LookupPredefinedUrlCategoryOverrideResultOutput) Rulestack() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPredefinedUrlCategoryOverrideResult) string { return v.Rulestack }).(pulumi.StringOutput)
}

// Update token.
func (o LookupPredefinedUrlCategoryOverrideResultOutput) UpdateToken() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPredefinedUrlCategoryOverrideResult) string { return v.UpdateToken }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupPredefinedUrlCategoryOverrideResultOutput{})
}
