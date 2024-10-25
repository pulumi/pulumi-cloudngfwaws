// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudngfwaws

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-cloudngfwaws/sdk/go/cloudngfwaws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Data source to retrieve information on a given AppId version.
//
// ## Admin Permission Type
//
// * `Rulestack`
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
//			_, err := cloudngfwaws.GetAppIdVersion(ctx, &cloudngfwaws.GetAppIdVersionArgs{
//				Version: "123-456",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func GetAppIdVersion(ctx *pulumi.Context, args *GetAppIdVersionArgs, opts ...pulumi.InvokeOption) (*GetAppIdVersionResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetAppIdVersionResult
	err := ctx.Invoke("cloudngfwaws:index/getAppIdVersion:getAppIdVersion", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getAppIdVersion.
type GetAppIdVersionArgs struct {
	// Max results. Defaults to `100`.
	MaxResults *int `pulumi:"maxResults"`
	// Pagination token.
	Token *string `pulumi:"token"`
	// The AppId version.
	Version string `pulumi:"version"`
}

// A collection of values returned by getAppIdVersion.
type GetAppIdVersionResult struct {
	// List of applications.
	Applications []string `pulumi:"applications"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// Max results. Defaults to `100`.
	MaxResults *int `pulumi:"maxResults"`
	// Token for the next page of results.
	NextToken string `pulumi:"nextToken"`
	// Pagination token.
	Token *string `pulumi:"token"`
	// The AppId version.
	Version string `pulumi:"version"`
}

func GetAppIdVersionOutput(ctx *pulumi.Context, args GetAppIdVersionOutputArgs, opts ...pulumi.InvokeOption) GetAppIdVersionResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetAppIdVersionResultOutput, error) {
			args := v.(GetAppIdVersionArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv GetAppIdVersionResult
			secret, err := ctx.InvokePackageRaw("cloudngfwaws:index/getAppIdVersion:getAppIdVersion", args, &rv, "", opts...)
			if err != nil {
				return GetAppIdVersionResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(GetAppIdVersionResultOutput)
			if secret {
				return pulumi.ToSecret(output).(GetAppIdVersionResultOutput), nil
			}
			return output, nil
		}).(GetAppIdVersionResultOutput)
}

// A collection of arguments for invoking getAppIdVersion.
type GetAppIdVersionOutputArgs struct {
	// Max results. Defaults to `100`.
	MaxResults pulumi.IntPtrInput `pulumi:"maxResults"`
	// Pagination token.
	Token pulumi.StringPtrInput `pulumi:"token"`
	// The AppId version.
	Version pulumi.StringInput `pulumi:"version"`
}

func (GetAppIdVersionOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetAppIdVersionArgs)(nil)).Elem()
}

// A collection of values returned by getAppIdVersion.
type GetAppIdVersionResultOutput struct{ *pulumi.OutputState }

func (GetAppIdVersionResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetAppIdVersionResult)(nil)).Elem()
}

func (o GetAppIdVersionResultOutput) ToGetAppIdVersionResultOutput() GetAppIdVersionResultOutput {
	return o
}

func (o GetAppIdVersionResultOutput) ToGetAppIdVersionResultOutputWithContext(ctx context.Context) GetAppIdVersionResultOutput {
	return o
}

// List of applications.
func (o GetAppIdVersionResultOutput) Applications() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetAppIdVersionResult) []string { return v.Applications }).(pulumi.StringArrayOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetAppIdVersionResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetAppIdVersionResult) string { return v.Id }).(pulumi.StringOutput)
}

// Max results. Defaults to `100`.
func (o GetAppIdVersionResultOutput) MaxResults() pulumi.IntPtrOutput {
	return o.ApplyT(func(v GetAppIdVersionResult) *int { return v.MaxResults }).(pulumi.IntPtrOutput)
}

// Token for the next page of results.
func (o GetAppIdVersionResultOutput) NextToken() pulumi.StringOutput {
	return o.ApplyT(func(v GetAppIdVersionResult) string { return v.NextToken }).(pulumi.StringOutput)
}

// Pagination token.
func (o GetAppIdVersionResultOutput) Token() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetAppIdVersionResult) *string { return v.Token }).(pulumi.StringPtrOutput)
}

// The AppId version.
func (o GetAppIdVersionResultOutput) Version() pulumi.StringOutput {
	return o.ApplyT(func(v GetAppIdVersionResult) string { return v.Version }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetAppIdVersionResultOutput{})
}
