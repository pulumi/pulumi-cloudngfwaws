// Code generated by pulumi-language-go DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudngfwaws

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-cloudngfwaws/sdk/go/cloudngfwaws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi-aws/sdk/go/aws"
//	"github.com/pulumi/pulumi-cloudngfwaws/sdk/go/cloudngfwaws"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			rs, err := cloudngfwaws.NewCommitRulestack(ctx, "rs", &cloudngfwaws.CommitRulestackArgs{
//				Rulestack: pulumi.String("my-rulestack"),
//			})
//			if err != nil {
//				return err
//			}
//			exampleVpc, err := aws.NewVpc(ctx, "example", &aws.VpcArgs{
//				CidrBlock: "172.16.0.0/16",
//				Tags: map[string]interface{}{
//					"name": "tf-example",
//				},
//			})
//			if err != nil {
//				return err
//			}
//			subnet1, err := aws.NewSubnet(ctx, "subnet1", &aws.SubnetArgs{
//				VpcId:            myVpc.Id,
//				CidrBlock:        "172.16.10.0/24",
//				AvailabilityZone: "us-west-2a",
//				Tags: map[string]interface{}{
//					"name": "tf-example",
//				},
//			})
//			if err != nil {
//				return err
//			}
//			subnet2, err := aws.NewSubnet(ctx, "subnet2", &aws.SubnetArgs{
//				VpcId:            myVpc.Id,
//				CidrBlock:        "172.16.20.0/24",
//				AvailabilityZone: "us-west-2b",
//				Tags: map[string]interface{}{
//					"name": "tf-example",
//				},
//			})
//			if err != nil {
//				return err
//			}
//			_, err = cloudngfwaws.NewNgfw(ctx, "example", &cloudngfwaws.NgfwArgs{
//				Name:         pulumi.String("example-instance"),
//				VpcId:        exampleVpc.Id,
//				AccountId:    pulumi.String("12345678"),
//				Description:  pulumi.String("Example description"),
//				LinkId:       pulumi.String("Link-81e80ccc-357a-4e4e-8325-1ed1d830cba5"),
//				EndpointMode: pulumi.String("ServiceManaged"),
//				SubnetMappings: cloudngfwaws.NgfwSubnetMappingArray{
//					&cloudngfwaws.NgfwSubnetMappingArgs{
//						SubnetId: subnet1.Id,
//					},
//					&cloudngfwaws.NgfwSubnetMappingArgs{
//						SubnetId: subnet2.Id,
//					},
//				},
//				Rulestack: rs.Rulestack,
//				Tags: pulumi.StringMap{
//					"Foo": pulumi.String("bar"),
//				},
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ## Import
//
// import name is <account_id>:<name>
//
// ```sh
// $ pulumi import cloudngfwaws:index/ngfw:Ngfw example 12345678:example-instance
// ```
type Ngfw struct {
	pulumi.CustomResourceState

	// The account ID. This field is mandatory if using multiple accounts.
	AccountId pulumi.StringPtrOutput `pulumi:"accountId"`
	// App-ID version number.
	AppIdVersion pulumi.StringOutput `pulumi:"appIdVersion"`
	// Automatic App-ID upgrade version number. Defaults to `true`.
	AutomaticUpgradeAppIdVersion pulumi.BoolPtrOutput `pulumi:"automaticUpgradeAppIdVersion"`
	// The description.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Set endpoint mode from the following options. Valid values are `ServiceManaged` or `CustomerManaged`.
	EndpointMode pulumi.StringOutput `pulumi:"endpointMode"`
	// The endpoint service name.
	EndpointServiceName pulumi.StringOutput `pulumi:"endpointServiceName"`
	// The Id of the NGFW.
	FirewallId pulumi.StringOutput `pulumi:"firewallId"`
	// The global rulestack for this NGFW.
	GlobalRulestack pulumi.StringPtrOutput `pulumi:"globalRulestack"`
	// A unique identifier for establishing and managing the link between the Cloud NGFW and other AWS resources.
	LinkId pulumi.StringOutput `pulumi:"linkId"`
	// The link status.
	LinkStatus pulumi.StringOutput `pulumi:"linkStatus"`
	// Share NGFW with Multiple VPCs. This feature can be enabled only if the endpointMode is CustomerManaged.
	MultiVpc pulumi.BoolOutput `pulumi:"multiVpc"`
	// The NGFW name.
	Name pulumi.StringOutput `pulumi:"name"`
	// The rulestack for this NGFW.
	Rulestack pulumi.StringPtrOutput `pulumi:"rulestack"`
	Statuses  NgfwStatusArrayOutput  `pulumi:"statuses"`
	// Subnet mappings.
	SubnetMappings NgfwSubnetMappingArrayOutput `pulumi:"subnetMappings"`
	// The tags.
	Tags pulumi.StringMapOutput `pulumi:"tags"`
	// The update token.
	UpdateToken pulumi.StringOutput `pulumi:"updateToken"`
	// The vpc id.
	VpcId pulumi.StringOutput `pulumi:"vpcId"`
}

// NewNgfw registers a new resource with the given unique name, arguments, and options.
func NewNgfw(ctx *pulumi.Context,
	name string, args *NgfwArgs, opts ...pulumi.ResourceOption) (*Ngfw, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.EndpointMode == nil {
		return nil, errors.New("invalid value for required argument 'EndpointMode'")
	}
	if args.SubnetMappings == nil {
		return nil, errors.New("invalid value for required argument 'SubnetMappings'")
	}
	if args.VpcId == nil {
		return nil, errors.New("invalid value for required argument 'VpcId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Ngfw
	err := ctx.RegisterResource("cloudngfwaws:index/ngfw:Ngfw", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetNgfw gets an existing Ngfw resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNgfw(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *NgfwState, opts ...pulumi.ResourceOption) (*Ngfw, error) {
	var resource Ngfw
	err := ctx.ReadResource("cloudngfwaws:index/ngfw:Ngfw", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Ngfw resources.
type ngfwState struct {
	// The account ID. This field is mandatory if using multiple accounts.
	AccountId *string `pulumi:"accountId"`
	// App-ID version number.
	AppIdVersion *string `pulumi:"appIdVersion"`
	// Automatic App-ID upgrade version number. Defaults to `true`.
	AutomaticUpgradeAppIdVersion *bool `pulumi:"automaticUpgradeAppIdVersion"`
	// The description.
	Description *string `pulumi:"description"`
	// Set endpoint mode from the following options. Valid values are `ServiceManaged` or `CustomerManaged`.
	EndpointMode *string `pulumi:"endpointMode"`
	// The endpoint service name.
	EndpointServiceName *string `pulumi:"endpointServiceName"`
	// The Id of the NGFW.
	FirewallId *string `pulumi:"firewallId"`
	// The global rulestack for this NGFW.
	GlobalRulestack *string `pulumi:"globalRulestack"`
	// A unique identifier for establishing and managing the link between the Cloud NGFW and other AWS resources.
	LinkId *string `pulumi:"linkId"`
	// The link status.
	LinkStatus *string `pulumi:"linkStatus"`
	// Share NGFW with Multiple VPCs. This feature can be enabled only if the endpointMode is CustomerManaged.
	MultiVpc *bool `pulumi:"multiVpc"`
	// The NGFW name.
	Name *string `pulumi:"name"`
	// The rulestack for this NGFW.
	Rulestack *string      `pulumi:"rulestack"`
	Statuses  []NgfwStatus `pulumi:"statuses"`
	// Subnet mappings.
	SubnetMappings []NgfwSubnetMapping `pulumi:"subnetMappings"`
	// The tags.
	Tags map[string]string `pulumi:"tags"`
	// The update token.
	UpdateToken *string `pulumi:"updateToken"`
	// The vpc id.
	VpcId *string `pulumi:"vpcId"`
}

type NgfwState struct {
	// The account ID. This field is mandatory if using multiple accounts.
	AccountId pulumi.StringPtrInput
	// App-ID version number.
	AppIdVersion pulumi.StringPtrInput
	// Automatic App-ID upgrade version number. Defaults to `true`.
	AutomaticUpgradeAppIdVersion pulumi.BoolPtrInput
	// The description.
	Description pulumi.StringPtrInput
	// Set endpoint mode from the following options. Valid values are `ServiceManaged` or `CustomerManaged`.
	EndpointMode pulumi.StringPtrInput
	// The endpoint service name.
	EndpointServiceName pulumi.StringPtrInput
	// The Id of the NGFW.
	FirewallId pulumi.StringPtrInput
	// The global rulestack for this NGFW.
	GlobalRulestack pulumi.StringPtrInput
	// A unique identifier for establishing and managing the link between the Cloud NGFW and other AWS resources.
	LinkId pulumi.StringPtrInput
	// The link status.
	LinkStatus pulumi.StringPtrInput
	// Share NGFW with Multiple VPCs. This feature can be enabled only if the endpointMode is CustomerManaged.
	MultiVpc pulumi.BoolPtrInput
	// The NGFW name.
	Name pulumi.StringPtrInput
	// The rulestack for this NGFW.
	Rulestack pulumi.StringPtrInput
	Statuses  NgfwStatusArrayInput
	// Subnet mappings.
	SubnetMappings NgfwSubnetMappingArrayInput
	// The tags.
	Tags pulumi.StringMapInput
	// The update token.
	UpdateToken pulumi.StringPtrInput
	// The vpc id.
	VpcId pulumi.StringPtrInput
}

func (NgfwState) ElementType() reflect.Type {
	return reflect.TypeOf((*ngfwState)(nil)).Elem()
}

type ngfwArgs struct {
	// The account ID. This field is mandatory if using multiple accounts.
	AccountId *string `pulumi:"accountId"`
	// App-ID version number.
	AppIdVersion *string `pulumi:"appIdVersion"`
	// Automatic App-ID upgrade version number. Defaults to `true`.
	AutomaticUpgradeAppIdVersion *bool `pulumi:"automaticUpgradeAppIdVersion"`
	// The description.
	Description *string `pulumi:"description"`
	// Set endpoint mode from the following options. Valid values are `ServiceManaged` or `CustomerManaged`.
	EndpointMode string `pulumi:"endpointMode"`
	// The global rulestack for this NGFW.
	GlobalRulestack *string `pulumi:"globalRulestack"`
	// A unique identifier for establishing and managing the link between the Cloud NGFW and other AWS resources.
	LinkId *string `pulumi:"linkId"`
	// Share NGFW with Multiple VPCs. This feature can be enabled only if the endpointMode is CustomerManaged.
	MultiVpc *bool `pulumi:"multiVpc"`
	// The NGFW name.
	Name *string `pulumi:"name"`
	// The rulestack for this NGFW.
	Rulestack *string `pulumi:"rulestack"`
	// Subnet mappings.
	SubnetMappings []NgfwSubnetMapping `pulumi:"subnetMappings"`
	// The tags.
	Tags map[string]string `pulumi:"tags"`
	// The vpc id.
	VpcId string `pulumi:"vpcId"`
}

// The set of arguments for constructing a Ngfw resource.
type NgfwArgs struct {
	// The account ID. This field is mandatory if using multiple accounts.
	AccountId pulumi.StringPtrInput
	// App-ID version number.
	AppIdVersion pulumi.StringPtrInput
	// Automatic App-ID upgrade version number. Defaults to `true`.
	AutomaticUpgradeAppIdVersion pulumi.BoolPtrInput
	// The description.
	Description pulumi.StringPtrInput
	// Set endpoint mode from the following options. Valid values are `ServiceManaged` or `CustomerManaged`.
	EndpointMode pulumi.StringInput
	// The global rulestack for this NGFW.
	GlobalRulestack pulumi.StringPtrInput
	// A unique identifier for establishing and managing the link between the Cloud NGFW and other AWS resources.
	LinkId pulumi.StringPtrInput
	// Share NGFW with Multiple VPCs. This feature can be enabled only if the endpointMode is CustomerManaged.
	MultiVpc pulumi.BoolPtrInput
	// The NGFW name.
	Name pulumi.StringPtrInput
	// The rulestack for this NGFW.
	Rulestack pulumi.StringPtrInput
	// Subnet mappings.
	SubnetMappings NgfwSubnetMappingArrayInput
	// The tags.
	Tags pulumi.StringMapInput
	// The vpc id.
	VpcId pulumi.StringInput
}

func (NgfwArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ngfwArgs)(nil)).Elem()
}

type NgfwInput interface {
	pulumi.Input

	ToNgfwOutput() NgfwOutput
	ToNgfwOutputWithContext(ctx context.Context) NgfwOutput
}

func (*Ngfw) ElementType() reflect.Type {
	return reflect.TypeOf((**Ngfw)(nil)).Elem()
}

func (i *Ngfw) ToNgfwOutput() NgfwOutput {
	return i.ToNgfwOutputWithContext(context.Background())
}

func (i *Ngfw) ToNgfwOutputWithContext(ctx context.Context) NgfwOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NgfwOutput)
}

// NgfwArrayInput is an input type that accepts NgfwArray and NgfwArrayOutput values.
// You can construct a concrete instance of `NgfwArrayInput` via:
//
//	NgfwArray{ NgfwArgs{...} }
type NgfwArrayInput interface {
	pulumi.Input

	ToNgfwArrayOutput() NgfwArrayOutput
	ToNgfwArrayOutputWithContext(context.Context) NgfwArrayOutput
}

type NgfwArray []NgfwInput

func (NgfwArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Ngfw)(nil)).Elem()
}

func (i NgfwArray) ToNgfwArrayOutput() NgfwArrayOutput {
	return i.ToNgfwArrayOutputWithContext(context.Background())
}

func (i NgfwArray) ToNgfwArrayOutputWithContext(ctx context.Context) NgfwArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NgfwArrayOutput)
}

// NgfwMapInput is an input type that accepts NgfwMap and NgfwMapOutput values.
// You can construct a concrete instance of `NgfwMapInput` via:
//
//	NgfwMap{ "key": NgfwArgs{...} }
type NgfwMapInput interface {
	pulumi.Input

	ToNgfwMapOutput() NgfwMapOutput
	ToNgfwMapOutputWithContext(context.Context) NgfwMapOutput
}

type NgfwMap map[string]NgfwInput

func (NgfwMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Ngfw)(nil)).Elem()
}

func (i NgfwMap) ToNgfwMapOutput() NgfwMapOutput {
	return i.ToNgfwMapOutputWithContext(context.Background())
}

func (i NgfwMap) ToNgfwMapOutputWithContext(ctx context.Context) NgfwMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NgfwMapOutput)
}

type NgfwOutput struct{ *pulumi.OutputState }

func (NgfwOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Ngfw)(nil)).Elem()
}

func (o NgfwOutput) ToNgfwOutput() NgfwOutput {
	return o
}

func (o NgfwOutput) ToNgfwOutputWithContext(ctx context.Context) NgfwOutput {
	return o
}

// The account ID. This field is mandatory if using multiple accounts.
func (o NgfwOutput) AccountId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Ngfw) pulumi.StringPtrOutput { return v.AccountId }).(pulumi.StringPtrOutput)
}

// App-ID version number.
func (o NgfwOutput) AppIdVersion() pulumi.StringOutput {
	return o.ApplyT(func(v *Ngfw) pulumi.StringOutput { return v.AppIdVersion }).(pulumi.StringOutput)
}

// Automatic App-ID upgrade version number. Defaults to `true`.
func (o NgfwOutput) AutomaticUpgradeAppIdVersion() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Ngfw) pulumi.BoolPtrOutput { return v.AutomaticUpgradeAppIdVersion }).(pulumi.BoolPtrOutput)
}

// The description.
func (o NgfwOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Ngfw) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// Set endpoint mode from the following options. Valid values are `ServiceManaged` or `CustomerManaged`.
func (o NgfwOutput) EndpointMode() pulumi.StringOutput {
	return o.ApplyT(func(v *Ngfw) pulumi.StringOutput { return v.EndpointMode }).(pulumi.StringOutput)
}

// The endpoint service name.
func (o NgfwOutput) EndpointServiceName() pulumi.StringOutput {
	return o.ApplyT(func(v *Ngfw) pulumi.StringOutput { return v.EndpointServiceName }).(pulumi.StringOutput)
}

// The Id of the NGFW.
func (o NgfwOutput) FirewallId() pulumi.StringOutput {
	return o.ApplyT(func(v *Ngfw) pulumi.StringOutput { return v.FirewallId }).(pulumi.StringOutput)
}

// The global rulestack for this NGFW.
func (o NgfwOutput) GlobalRulestack() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Ngfw) pulumi.StringPtrOutput { return v.GlobalRulestack }).(pulumi.StringPtrOutput)
}

// A unique identifier for establishing and managing the link between the Cloud NGFW and other AWS resources.
func (o NgfwOutput) LinkId() pulumi.StringOutput {
	return o.ApplyT(func(v *Ngfw) pulumi.StringOutput { return v.LinkId }).(pulumi.StringOutput)
}

// The link status.
func (o NgfwOutput) LinkStatus() pulumi.StringOutput {
	return o.ApplyT(func(v *Ngfw) pulumi.StringOutput { return v.LinkStatus }).(pulumi.StringOutput)
}

// Share NGFW with Multiple VPCs. This feature can be enabled only if the endpointMode is CustomerManaged.
func (o NgfwOutput) MultiVpc() pulumi.BoolOutput {
	return o.ApplyT(func(v *Ngfw) pulumi.BoolOutput { return v.MultiVpc }).(pulumi.BoolOutput)
}

// The NGFW name.
func (o NgfwOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Ngfw) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The rulestack for this NGFW.
func (o NgfwOutput) Rulestack() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Ngfw) pulumi.StringPtrOutput { return v.Rulestack }).(pulumi.StringPtrOutput)
}

func (o NgfwOutput) Statuses() NgfwStatusArrayOutput {
	return o.ApplyT(func(v *Ngfw) NgfwStatusArrayOutput { return v.Statuses }).(NgfwStatusArrayOutput)
}

// Subnet mappings.
func (o NgfwOutput) SubnetMappings() NgfwSubnetMappingArrayOutput {
	return o.ApplyT(func(v *Ngfw) NgfwSubnetMappingArrayOutput { return v.SubnetMappings }).(NgfwSubnetMappingArrayOutput)
}

// The tags.
func (o NgfwOutput) Tags() pulumi.StringMapOutput {
	return o.ApplyT(func(v *Ngfw) pulumi.StringMapOutput { return v.Tags }).(pulumi.StringMapOutput)
}

// The update token.
func (o NgfwOutput) UpdateToken() pulumi.StringOutput {
	return o.ApplyT(func(v *Ngfw) pulumi.StringOutput { return v.UpdateToken }).(pulumi.StringOutput)
}

// The vpc id.
func (o NgfwOutput) VpcId() pulumi.StringOutput {
	return o.ApplyT(func(v *Ngfw) pulumi.StringOutput { return v.VpcId }).(pulumi.StringOutput)
}

type NgfwArrayOutput struct{ *pulumi.OutputState }

func (NgfwArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Ngfw)(nil)).Elem()
}

func (o NgfwArrayOutput) ToNgfwArrayOutput() NgfwArrayOutput {
	return o
}

func (o NgfwArrayOutput) ToNgfwArrayOutputWithContext(ctx context.Context) NgfwArrayOutput {
	return o
}

func (o NgfwArrayOutput) Index(i pulumi.IntInput) NgfwOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Ngfw {
		return vs[0].([]*Ngfw)[vs[1].(int)]
	}).(NgfwOutput)
}

type NgfwMapOutput struct{ *pulumi.OutputState }

func (NgfwMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Ngfw)(nil)).Elem()
}

func (o NgfwMapOutput) ToNgfwMapOutput() NgfwMapOutput {
	return o
}

func (o NgfwMapOutput) ToNgfwMapOutputWithContext(ctx context.Context) NgfwMapOutput {
	return o
}

func (o NgfwMapOutput) MapIndex(k pulumi.StringInput) NgfwOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Ngfw {
		return vs[0].(map[string]*Ngfw)[vs[1].(string)]
	}).(NgfwOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*NgfwInput)(nil)).Elem(), &Ngfw{})
	pulumi.RegisterInputType(reflect.TypeOf((*NgfwArrayInput)(nil)).Elem(), NgfwArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*NgfwMapInput)(nil)).Elem(), NgfwMap{})
	pulumi.RegisterOutputType(NgfwOutput{})
	pulumi.RegisterOutputType(NgfwArrayOutput{})
	pulumi.RegisterOutputType(NgfwMapOutput{})
}
