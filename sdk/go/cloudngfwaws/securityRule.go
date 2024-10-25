// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudngfwaws

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-cloudngfwaws/sdk/go/cloudngfwaws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource for security rule manipulation.
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
//				Name:        pulumi.String("terraform-rulestack"),
//				Scope:       pulumi.String("Local"),
//				AccountId:   pulumi.String("123456789"),
//				Description: pulumi.String("Made by Pulumi"),
//				ProfileConfig: &cloudngfwaws.RulestackProfileConfigArgs{
//					AntiSpyware: pulumi.String("BestPractice"),
//				},
//			})
//			if err != nil {
//				return err
//			}
//			_, err = cloudngfwaws.NewSecurityRule(ctx, "example", &cloudngfwaws.SecurityRuleArgs{
//				Rulestack:   r.Name,
//				RuleList:    pulumi.String("LocalRule"),
//				Priority:    pulumi.Int(3),
//				Name:        pulumi.String("tf-security-rule"),
//				Description: pulumi.String("Also configured by Terraform"),
//				Source: &cloudngfwaws.SecurityRuleSourceArgs{
//					Cidrs: pulumi.StringArray{
//						pulumi.String("any"),
//					},
//				},
//				Destination: &cloudngfwaws.SecurityRuleDestinationArgs{
//					Cidrs: pulumi.StringArray{
//						pulumi.String("192.168.0.0/16"),
//					},
//				},
//				NegateDestination: pulumi.Bool(true),
//				Applications: pulumi.StringArray{
//					pulumi.String("any"),
//				},
//				Category:     &cloudngfwaws.SecurityRuleCategoryArgs{},
//				Action:       pulumi.String("Allow"),
//				Logging:      pulumi.Bool(true),
//				AuditComment: pulumi.String("initial config"),
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
// import name is <scope>:<rulestack>:<rule_list>:<priority>
//
// ```sh
// $ pulumi import cloudngfwaws:index/securityRule:SecurityRule example Local:terraform-rulestack:LocalRule:3
// ```
type SecurityRule struct {
	pulumi.CustomResourceState

	// The action to take. Valid values are `Allow`, `DenySilent`, `DenyResetServer`, or `DenyResetBoth`.
	Action pulumi.StringOutput `pulumi:"action"`
	// The list of applications.
	Applications pulumi.StringArrayOutput `pulumi:"applications"`
	// The audit comment.
	AuditComment pulumi.StringPtrOutput `pulumi:"auditComment"`
	// The category spec.
	Category SecurityRuleCategoryOutput `pulumi:"category"`
	// Decryption rule type. Valid values are ``or`SSLOutboundInspection`.
	DecryptionRuleType pulumi.StringPtrOutput `pulumi:"decryptionRuleType"`
	// The description.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The destination spec.
	Destination SecurityRuleDestinationOutput `pulumi:"destination"`
	// Set to false to disable this rule. Defaults to `true`.
	Enabled pulumi.BoolPtrOutput `pulumi:"enabled"`
	// Enable logging at end. Defaults to `true`.
	Logging pulumi.BoolPtrOutput `pulumi:"logging"`
	// The name.
	Name pulumi.StringOutput `pulumi:"name"`
	// Negate the destination definition.
	NegateDestination pulumi.BoolPtrOutput `pulumi:"negateDestination"`
	// Negate the source definition.
	NegateSource pulumi.BoolPtrOutput `pulumi:"negateSource"`
	// The rule priority.
	Priority pulumi.IntOutput `pulumi:"priority"`
	// Protocol port list.
	ProtPortLists pulumi.StringArrayOutput `pulumi:"protPortLists"`
	// The protocol.
	Protocol pulumi.StringPtrOutput `pulumi:"protocol"`
	// The rulebase. Valid values are `PreRule`, `PostRule`, or `LocalRule`. Defaults to `PreRule`.
	RuleList pulumi.StringPtrOutput `pulumi:"ruleList"`
	// The rulestack.
	Rulestack pulumi.StringOutput `pulumi:"rulestack"`
	// The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
	Scope pulumi.StringPtrOutput `pulumi:"scope"`
	// The source spec.
	Source SecurityRuleSourceOutput `pulumi:"source"`
	// The tags.
	Tags pulumi.StringMapOutput `pulumi:"tags"`
	// The update token.
	UpdateToken pulumi.StringOutput `pulumi:"updateToken"`
}

// NewSecurityRule registers a new resource with the given unique name, arguments, and options.
func NewSecurityRule(ctx *pulumi.Context,
	name string, args *SecurityRuleArgs, opts ...pulumi.ResourceOption) (*SecurityRule, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Action == nil {
		return nil, errors.New("invalid value for required argument 'Action'")
	}
	if args.Applications == nil {
		return nil, errors.New("invalid value for required argument 'Applications'")
	}
	if args.Category == nil {
		return nil, errors.New("invalid value for required argument 'Category'")
	}
	if args.Destination == nil {
		return nil, errors.New("invalid value for required argument 'Destination'")
	}
	if args.Priority == nil {
		return nil, errors.New("invalid value for required argument 'Priority'")
	}
	if args.Rulestack == nil {
		return nil, errors.New("invalid value for required argument 'Rulestack'")
	}
	if args.Source == nil {
		return nil, errors.New("invalid value for required argument 'Source'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource SecurityRule
	err := ctx.RegisterResource("cloudngfwaws:index/securityRule:SecurityRule", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSecurityRule gets an existing SecurityRule resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSecurityRule(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SecurityRuleState, opts ...pulumi.ResourceOption) (*SecurityRule, error) {
	var resource SecurityRule
	err := ctx.ReadResource("cloudngfwaws:index/securityRule:SecurityRule", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SecurityRule resources.
type securityRuleState struct {
	// The action to take. Valid values are `Allow`, `DenySilent`, `DenyResetServer`, or `DenyResetBoth`.
	Action *string `pulumi:"action"`
	// The list of applications.
	Applications []string `pulumi:"applications"`
	// The audit comment.
	AuditComment *string `pulumi:"auditComment"`
	// The category spec.
	Category *SecurityRuleCategory `pulumi:"category"`
	// Decryption rule type. Valid values are ``or`SSLOutboundInspection`.
	DecryptionRuleType *string `pulumi:"decryptionRuleType"`
	// The description.
	Description *string `pulumi:"description"`
	// The destination spec.
	Destination *SecurityRuleDestination `pulumi:"destination"`
	// Set to false to disable this rule. Defaults to `true`.
	Enabled *bool `pulumi:"enabled"`
	// Enable logging at end. Defaults to `true`.
	Logging *bool `pulumi:"logging"`
	// The name.
	Name *string `pulumi:"name"`
	// Negate the destination definition.
	NegateDestination *bool `pulumi:"negateDestination"`
	// Negate the source definition.
	NegateSource *bool `pulumi:"negateSource"`
	// The rule priority.
	Priority *int `pulumi:"priority"`
	// Protocol port list.
	ProtPortLists []string `pulumi:"protPortLists"`
	// The protocol.
	Protocol *string `pulumi:"protocol"`
	// The rulebase. Valid values are `PreRule`, `PostRule`, or `LocalRule`. Defaults to `PreRule`.
	RuleList *string `pulumi:"ruleList"`
	// The rulestack.
	Rulestack *string `pulumi:"rulestack"`
	// The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
	Scope *string `pulumi:"scope"`
	// The source spec.
	Source *SecurityRuleSource `pulumi:"source"`
	// The tags.
	Tags map[string]string `pulumi:"tags"`
	// The update token.
	UpdateToken *string `pulumi:"updateToken"`
}

type SecurityRuleState struct {
	// The action to take. Valid values are `Allow`, `DenySilent`, `DenyResetServer`, or `DenyResetBoth`.
	Action pulumi.StringPtrInput
	// The list of applications.
	Applications pulumi.StringArrayInput
	// The audit comment.
	AuditComment pulumi.StringPtrInput
	// The category spec.
	Category SecurityRuleCategoryPtrInput
	// Decryption rule type. Valid values are ``or`SSLOutboundInspection`.
	DecryptionRuleType pulumi.StringPtrInput
	// The description.
	Description pulumi.StringPtrInput
	// The destination spec.
	Destination SecurityRuleDestinationPtrInput
	// Set to false to disable this rule. Defaults to `true`.
	Enabled pulumi.BoolPtrInput
	// Enable logging at end. Defaults to `true`.
	Logging pulumi.BoolPtrInput
	// The name.
	Name pulumi.StringPtrInput
	// Negate the destination definition.
	NegateDestination pulumi.BoolPtrInput
	// Negate the source definition.
	NegateSource pulumi.BoolPtrInput
	// The rule priority.
	Priority pulumi.IntPtrInput
	// Protocol port list.
	ProtPortLists pulumi.StringArrayInput
	// The protocol.
	Protocol pulumi.StringPtrInput
	// The rulebase. Valid values are `PreRule`, `PostRule`, or `LocalRule`. Defaults to `PreRule`.
	RuleList pulumi.StringPtrInput
	// The rulestack.
	Rulestack pulumi.StringPtrInput
	// The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
	Scope pulumi.StringPtrInput
	// The source spec.
	Source SecurityRuleSourcePtrInput
	// The tags.
	Tags pulumi.StringMapInput
	// The update token.
	UpdateToken pulumi.StringPtrInput
}

func (SecurityRuleState) ElementType() reflect.Type {
	return reflect.TypeOf((*securityRuleState)(nil)).Elem()
}

type securityRuleArgs struct {
	// The action to take. Valid values are `Allow`, `DenySilent`, `DenyResetServer`, or `DenyResetBoth`.
	Action string `pulumi:"action"`
	// The list of applications.
	Applications []string `pulumi:"applications"`
	// The audit comment.
	AuditComment *string `pulumi:"auditComment"`
	// The category spec.
	Category SecurityRuleCategory `pulumi:"category"`
	// Decryption rule type. Valid values are ``or`SSLOutboundInspection`.
	DecryptionRuleType *string `pulumi:"decryptionRuleType"`
	// The description.
	Description *string `pulumi:"description"`
	// The destination spec.
	Destination SecurityRuleDestination `pulumi:"destination"`
	// Set to false to disable this rule. Defaults to `true`.
	Enabled *bool `pulumi:"enabled"`
	// Enable logging at end. Defaults to `true`.
	Logging *bool `pulumi:"logging"`
	// The name.
	Name *string `pulumi:"name"`
	// Negate the destination definition.
	NegateDestination *bool `pulumi:"negateDestination"`
	// Negate the source definition.
	NegateSource *bool `pulumi:"negateSource"`
	// The rule priority.
	Priority int `pulumi:"priority"`
	// Protocol port list.
	ProtPortLists []string `pulumi:"protPortLists"`
	// The protocol.
	Protocol *string `pulumi:"protocol"`
	// The rulebase. Valid values are `PreRule`, `PostRule`, or `LocalRule`. Defaults to `PreRule`.
	RuleList *string `pulumi:"ruleList"`
	// The rulestack.
	Rulestack string `pulumi:"rulestack"`
	// The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
	Scope *string `pulumi:"scope"`
	// The source spec.
	Source SecurityRuleSource `pulumi:"source"`
	// The tags.
	Tags map[string]string `pulumi:"tags"`
}

// The set of arguments for constructing a SecurityRule resource.
type SecurityRuleArgs struct {
	// The action to take. Valid values are `Allow`, `DenySilent`, `DenyResetServer`, or `DenyResetBoth`.
	Action pulumi.StringInput
	// The list of applications.
	Applications pulumi.StringArrayInput
	// The audit comment.
	AuditComment pulumi.StringPtrInput
	// The category spec.
	Category SecurityRuleCategoryInput
	// Decryption rule type. Valid values are ``or`SSLOutboundInspection`.
	DecryptionRuleType pulumi.StringPtrInput
	// The description.
	Description pulumi.StringPtrInput
	// The destination spec.
	Destination SecurityRuleDestinationInput
	// Set to false to disable this rule. Defaults to `true`.
	Enabled pulumi.BoolPtrInput
	// Enable logging at end. Defaults to `true`.
	Logging pulumi.BoolPtrInput
	// The name.
	Name pulumi.StringPtrInput
	// Negate the destination definition.
	NegateDestination pulumi.BoolPtrInput
	// Negate the source definition.
	NegateSource pulumi.BoolPtrInput
	// The rule priority.
	Priority pulumi.IntInput
	// Protocol port list.
	ProtPortLists pulumi.StringArrayInput
	// The protocol.
	Protocol pulumi.StringPtrInput
	// The rulebase. Valid values are `PreRule`, `PostRule`, or `LocalRule`. Defaults to `PreRule`.
	RuleList pulumi.StringPtrInput
	// The rulestack.
	Rulestack pulumi.StringInput
	// The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
	Scope pulumi.StringPtrInput
	// The source spec.
	Source SecurityRuleSourceInput
	// The tags.
	Tags pulumi.StringMapInput
}

func (SecurityRuleArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*securityRuleArgs)(nil)).Elem()
}

type SecurityRuleInput interface {
	pulumi.Input

	ToSecurityRuleOutput() SecurityRuleOutput
	ToSecurityRuleOutputWithContext(ctx context.Context) SecurityRuleOutput
}

func (*SecurityRule) ElementType() reflect.Type {
	return reflect.TypeOf((**SecurityRule)(nil)).Elem()
}

func (i *SecurityRule) ToSecurityRuleOutput() SecurityRuleOutput {
	return i.ToSecurityRuleOutputWithContext(context.Background())
}

func (i *SecurityRule) ToSecurityRuleOutputWithContext(ctx context.Context) SecurityRuleOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SecurityRuleOutput)
}

// SecurityRuleArrayInput is an input type that accepts SecurityRuleArray and SecurityRuleArrayOutput values.
// You can construct a concrete instance of `SecurityRuleArrayInput` via:
//
//	SecurityRuleArray{ SecurityRuleArgs{...} }
type SecurityRuleArrayInput interface {
	pulumi.Input

	ToSecurityRuleArrayOutput() SecurityRuleArrayOutput
	ToSecurityRuleArrayOutputWithContext(context.Context) SecurityRuleArrayOutput
}

type SecurityRuleArray []SecurityRuleInput

func (SecurityRuleArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*SecurityRule)(nil)).Elem()
}

func (i SecurityRuleArray) ToSecurityRuleArrayOutput() SecurityRuleArrayOutput {
	return i.ToSecurityRuleArrayOutputWithContext(context.Background())
}

func (i SecurityRuleArray) ToSecurityRuleArrayOutputWithContext(ctx context.Context) SecurityRuleArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SecurityRuleArrayOutput)
}

// SecurityRuleMapInput is an input type that accepts SecurityRuleMap and SecurityRuleMapOutput values.
// You can construct a concrete instance of `SecurityRuleMapInput` via:
//
//	SecurityRuleMap{ "key": SecurityRuleArgs{...} }
type SecurityRuleMapInput interface {
	pulumi.Input

	ToSecurityRuleMapOutput() SecurityRuleMapOutput
	ToSecurityRuleMapOutputWithContext(context.Context) SecurityRuleMapOutput
}

type SecurityRuleMap map[string]SecurityRuleInput

func (SecurityRuleMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*SecurityRule)(nil)).Elem()
}

func (i SecurityRuleMap) ToSecurityRuleMapOutput() SecurityRuleMapOutput {
	return i.ToSecurityRuleMapOutputWithContext(context.Background())
}

func (i SecurityRuleMap) ToSecurityRuleMapOutputWithContext(ctx context.Context) SecurityRuleMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SecurityRuleMapOutput)
}

type SecurityRuleOutput struct{ *pulumi.OutputState }

func (SecurityRuleOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SecurityRule)(nil)).Elem()
}

func (o SecurityRuleOutput) ToSecurityRuleOutput() SecurityRuleOutput {
	return o
}

func (o SecurityRuleOutput) ToSecurityRuleOutputWithContext(ctx context.Context) SecurityRuleOutput {
	return o
}

// The action to take. Valid values are `Allow`, `DenySilent`, `DenyResetServer`, or `DenyResetBoth`.
func (o SecurityRuleOutput) Action() pulumi.StringOutput {
	return o.ApplyT(func(v *SecurityRule) pulumi.StringOutput { return v.Action }).(pulumi.StringOutput)
}

// The list of applications.
func (o SecurityRuleOutput) Applications() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *SecurityRule) pulumi.StringArrayOutput { return v.Applications }).(pulumi.StringArrayOutput)
}

// The audit comment.
func (o SecurityRuleOutput) AuditComment() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SecurityRule) pulumi.StringPtrOutput { return v.AuditComment }).(pulumi.StringPtrOutput)
}

// The category spec.
func (o SecurityRuleOutput) Category() SecurityRuleCategoryOutput {
	return o.ApplyT(func(v *SecurityRule) SecurityRuleCategoryOutput { return v.Category }).(SecurityRuleCategoryOutput)
}

// Decryption rule type. Valid values are “or`SSLOutboundInspection`.
func (o SecurityRuleOutput) DecryptionRuleType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SecurityRule) pulumi.StringPtrOutput { return v.DecryptionRuleType }).(pulumi.StringPtrOutput)
}

// The description.
func (o SecurityRuleOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SecurityRule) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// The destination spec.
func (o SecurityRuleOutput) Destination() SecurityRuleDestinationOutput {
	return o.ApplyT(func(v *SecurityRule) SecurityRuleDestinationOutput { return v.Destination }).(SecurityRuleDestinationOutput)
}

// Set to false to disable this rule. Defaults to `true`.
func (o SecurityRuleOutput) Enabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *SecurityRule) pulumi.BoolPtrOutput { return v.Enabled }).(pulumi.BoolPtrOutput)
}

// Enable logging at end. Defaults to `true`.
func (o SecurityRuleOutput) Logging() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *SecurityRule) pulumi.BoolPtrOutput { return v.Logging }).(pulumi.BoolPtrOutput)
}

// The name.
func (o SecurityRuleOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *SecurityRule) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Negate the destination definition.
func (o SecurityRuleOutput) NegateDestination() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *SecurityRule) pulumi.BoolPtrOutput { return v.NegateDestination }).(pulumi.BoolPtrOutput)
}

// Negate the source definition.
func (o SecurityRuleOutput) NegateSource() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *SecurityRule) pulumi.BoolPtrOutput { return v.NegateSource }).(pulumi.BoolPtrOutput)
}

// The rule priority.
func (o SecurityRuleOutput) Priority() pulumi.IntOutput {
	return o.ApplyT(func(v *SecurityRule) pulumi.IntOutput { return v.Priority }).(pulumi.IntOutput)
}

// Protocol port list.
func (o SecurityRuleOutput) ProtPortLists() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *SecurityRule) pulumi.StringArrayOutput { return v.ProtPortLists }).(pulumi.StringArrayOutput)
}

// The protocol.
func (o SecurityRuleOutput) Protocol() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SecurityRule) pulumi.StringPtrOutput { return v.Protocol }).(pulumi.StringPtrOutput)
}

// The rulebase. Valid values are `PreRule`, `PostRule`, or `LocalRule`. Defaults to `PreRule`.
func (o SecurityRuleOutput) RuleList() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SecurityRule) pulumi.StringPtrOutput { return v.RuleList }).(pulumi.StringPtrOutput)
}

// The rulestack.
func (o SecurityRuleOutput) Rulestack() pulumi.StringOutput {
	return o.ApplyT(func(v *SecurityRule) pulumi.StringOutput { return v.Rulestack }).(pulumi.StringOutput)
}

// The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
func (o SecurityRuleOutput) Scope() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SecurityRule) pulumi.StringPtrOutput { return v.Scope }).(pulumi.StringPtrOutput)
}

// The source spec.
func (o SecurityRuleOutput) Source() SecurityRuleSourceOutput {
	return o.ApplyT(func(v *SecurityRule) SecurityRuleSourceOutput { return v.Source }).(SecurityRuleSourceOutput)
}

// The tags.
func (o SecurityRuleOutput) Tags() pulumi.StringMapOutput {
	return o.ApplyT(func(v *SecurityRule) pulumi.StringMapOutput { return v.Tags }).(pulumi.StringMapOutput)
}

// The update token.
func (o SecurityRuleOutput) UpdateToken() pulumi.StringOutput {
	return o.ApplyT(func(v *SecurityRule) pulumi.StringOutput { return v.UpdateToken }).(pulumi.StringOutput)
}

type SecurityRuleArrayOutput struct{ *pulumi.OutputState }

func (SecurityRuleArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*SecurityRule)(nil)).Elem()
}

func (o SecurityRuleArrayOutput) ToSecurityRuleArrayOutput() SecurityRuleArrayOutput {
	return o
}

func (o SecurityRuleArrayOutput) ToSecurityRuleArrayOutputWithContext(ctx context.Context) SecurityRuleArrayOutput {
	return o
}

func (o SecurityRuleArrayOutput) Index(i pulumi.IntInput) SecurityRuleOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *SecurityRule {
		return vs[0].([]*SecurityRule)[vs[1].(int)]
	}).(SecurityRuleOutput)
}

type SecurityRuleMapOutput struct{ *pulumi.OutputState }

func (SecurityRuleMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*SecurityRule)(nil)).Elem()
}

func (o SecurityRuleMapOutput) ToSecurityRuleMapOutput() SecurityRuleMapOutput {
	return o
}

func (o SecurityRuleMapOutput) ToSecurityRuleMapOutputWithContext(ctx context.Context) SecurityRuleMapOutput {
	return o
}

func (o SecurityRuleMapOutput) MapIndex(k pulumi.StringInput) SecurityRuleOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *SecurityRule {
		return vs[0].(map[string]*SecurityRule)[vs[1].(string)]
	}).(SecurityRuleOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SecurityRuleInput)(nil)).Elem(), &SecurityRule{})
	pulumi.RegisterInputType(reflect.TypeOf((*SecurityRuleArrayInput)(nil)).Elem(), SecurityRuleArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*SecurityRuleMapInput)(nil)).Elem(), SecurityRuleMap{})
	pulumi.RegisterOutputType(SecurityRuleOutput{})
	pulumi.RegisterOutputType(SecurityRuleArrayOutput{})
	pulumi.RegisterOutputType(SecurityRuleMapOutput{})
}
