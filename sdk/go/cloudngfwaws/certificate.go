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

// Resource for certificate manipulation.
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
//			_, err = cloudngfwaws.NewCertificate(ctx, "example", &cloudngfwaws.CertificateArgs{
//				Rulestack:    r.Name,
//				Name:         pulumi.String("tf-cert"),
//				Description:  pulumi.String("Also configured by Terraform"),
//				SelfSigned:   pulumi.Bool(true),
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
// import name is <scope>:<rulestack>:<certificate_name>
//
// ```sh
// $ pulumi import cloudngfwaws:index/certificate:Certificate example Local:terraform-rulestack:tf-cert
// ```
type Certificate struct {
	pulumi.CustomResourceState

	// The audit comment.
	AuditComment pulumi.StringPtrOutput `pulumi:"auditComment"`
	// The description.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The name.
	Name pulumi.StringOutput `pulumi:"name"`
	// The rulestack.
	Rulestack pulumi.StringOutput `pulumi:"rulestack"`
	// The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
	Scope pulumi.StringPtrOutput `pulumi:"scope"`
	// Set to true if certificate is self-signed.
	SelfSigned pulumi.BoolPtrOutput `pulumi:"selfSigned"`
	// The certificate signer ARN.
	SignerArn pulumi.StringPtrOutput `pulumi:"signerArn"`
	// The update token.
	UpdateToken pulumi.StringOutput `pulumi:"updateToken"`
}

// NewCertificate registers a new resource with the given unique name, arguments, and options.
func NewCertificate(ctx *pulumi.Context,
	name string, args *CertificateArgs, opts ...pulumi.ResourceOption) (*Certificate, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Rulestack == nil {
		return nil, errors.New("invalid value for required argument 'Rulestack'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Certificate
	err := ctx.RegisterResource("cloudngfwaws:index/certificate:Certificate", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCertificate gets an existing Certificate resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCertificate(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CertificateState, opts ...pulumi.ResourceOption) (*Certificate, error) {
	var resource Certificate
	err := ctx.ReadResource("cloudngfwaws:index/certificate:Certificate", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Certificate resources.
type certificateState struct {
	// The audit comment.
	AuditComment *string `pulumi:"auditComment"`
	// The description.
	Description *string `pulumi:"description"`
	// The name.
	Name *string `pulumi:"name"`
	// The rulestack.
	Rulestack *string `pulumi:"rulestack"`
	// The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
	Scope *string `pulumi:"scope"`
	// Set to true if certificate is self-signed.
	SelfSigned *bool `pulumi:"selfSigned"`
	// The certificate signer ARN.
	SignerArn *string `pulumi:"signerArn"`
	// The update token.
	UpdateToken *string `pulumi:"updateToken"`
}

type CertificateState struct {
	// The audit comment.
	AuditComment pulumi.StringPtrInput
	// The description.
	Description pulumi.StringPtrInput
	// The name.
	Name pulumi.StringPtrInput
	// The rulestack.
	Rulestack pulumi.StringPtrInput
	// The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
	Scope pulumi.StringPtrInput
	// Set to true if certificate is self-signed.
	SelfSigned pulumi.BoolPtrInput
	// The certificate signer ARN.
	SignerArn pulumi.StringPtrInput
	// The update token.
	UpdateToken pulumi.StringPtrInput
}

func (CertificateState) ElementType() reflect.Type {
	return reflect.TypeOf((*certificateState)(nil)).Elem()
}

type certificateArgs struct {
	// The audit comment.
	AuditComment *string `pulumi:"auditComment"`
	// The description.
	Description *string `pulumi:"description"`
	// The name.
	Name *string `pulumi:"name"`
	// The rulestack.
	Rulestack string `pulumi:"rulestack"`
	// The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
	Scope *string `pulumi:"scope"`
	// Set to true if certificate is self-signed.
	SelfSigned *bool `pulumi:"selfSigned"`
	// The certificate signer ARN.
	SignerArn *string `pulumi:"signerArn"`
}

// The set of arguments for constructing a Certificate resource.
type CertificateArgs struct {
	// The audit comment.
	AuditComment pulumi.StringPtrInput
	// The description.
	Description pulumi.StringPtrInput
	// The name.
	Name pulumi.StringPtrInput
	// The rulestack.
	Rulestack pulumi.StringInput
	// The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
	Scope pulumi.StringPtrInput
	// Set to true if certificate is self-signed.
	SelfSigned pulumi.BoolPtrInput
	// The certificate signer ARN.
	SignerArn pulumi.StringPtrInput
}

func (CertificateArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*certificateArgs)(nil)).Elem()
}

type CertificateInput interface {
	pulumi.Input

	ToCertificateOutput() CertificateOutput
	ToCertificateOutputWithContext(ctx context.Context) CertificateOutput
}

func (*Certificate) ElementType() reflect.Type {
	return reflect.TypeOf((**Certificate)(nil)).Elem()
}

func (i *Certificate) ToCertificateOutput() CertificateOutput {
	return i.ToCertificateOutputWithContext(context.Background())
}

func (i *Certificate) ToCertificateOutputWithContext(ctx context.Context) CertificateOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CertificateOutput)
}

// CertificateArrayInput is an input type that accepts CertificateArray and CertificateArrayOutput values.
// You can construct a concrete instance of `CertificateArrayInput` via:
//
//	CertificateArray{ CertificateArgs{...} }
type CertificateArrayInput interface {
	pulumi.Input

	ToCertificateArrayOutput() CertificateArrayOutput
	ToCertificateArrayOutputWithContext(context.Context) CertificateArrayOutput
}

type CertificateArray []CertificateInput

func (CertificateArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Certificate)(nil)).Elem()
}

func (i CertificateArray) ToCertificateArrayOutput() CertificateArrayOutput {
	return i.ToCertificateArrayOutputWithContext(context.Background())
}

func (i CertificateArray) ToCertificateArrayOutputWithContext(ctx context.Context) CertificateArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CertificateArrayOutput)
}

// CertificateMapInput is an input type that accepts CertificateMap and CertificateMapOutput values.
// You can construct a concrete instance of `CertificateMapInput` via:
//
//	CertificateMap{ "key": CertificateArgs{...} }
type CertificateMapInput interface {
	pulumi.Input

	ToCertificateMapOutput() CertificateMapOutput
	ToCertificateMapOutputWithContext(context.Context) CertificateMapOutput
}

type CertificateMap map[string]CertificateInput

func (CertificateMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Certificate)(nil)).Elem()
}

func (i CertificateMap) ToCertificateMapOutput() CertificateMapOutput {
	return i.ToCertificateMapOutputWithContext(context.Background())
}

func (i CertificateMap) ToCertificateMapOutputWithContext(ctx context.Context) CertificateMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CertificateMapOutput)
}

type CertificateOutput struct{ *pulumi.OutputState }

func (CertificateOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Certificate)(nil)).Elem()
}

func (o CertificateOutput) ToCertificateOutput() CertificateOutput {
	return o
}

func (o CertificateOutput) ToCertificateOutputWithContext(ctx context.Context) CertificateOutput {
	return o
}

// The audit comment.
func (o CertificateOutput) AuditComment() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Certificate) pulumi.StringPtrOutput { return v.AuditComment }).(pulumi.StringPtrOutput)
}

// The description.
func (o CertificateOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Certificate) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// The name.
func (o CertificateOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Certificate) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The rulestack.
func (o CertificateOutput) Rulestack() pulumi.StringOutput {
	return o.ApplyT(func(v *Certificate) pulumi.StringOutput { return v.Rulestack }).(pulumi.StringOutput)
}

// The rulestack's scope. A local rulestack will require that you've retrieved a LRA JWT. A global rulestack will require that you've retrieved a GRA JWT. Valid values are `Local` or `Global`. Defaults to `Local`.
func (o CertificateOutput) Scope() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Certificate) pulumi.StringPtrOutput { return v.Scope }).(pulumi.StringPtrOutput)
}

// Set to true if certificate is self-signed.
func (o CertificateOutput) SelfSigned() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Certificate) pulumi.BoolPtrOutput { return v.SelfSigned }).(pulumi.BoolPtrOutput)
}

// The certificate signer ARN.
func (o CertificateOutput) SignerArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Certificate) pulumi.StringPtrOutput { return v.SignerArn }).(pulumi.StringPtrOutput)
}

// The update token.
func (o CertificateOutput) UpdateToken() pulumi.StringOutput {
	return o.ApplyT(func(v *Certificate) pulumi.StringOutput { return v.UpdateToken }).(pulumi.StringOutput)
}

type CertificateArrayOutput struct{ *pulumi.OutputState }

func (CertificateArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Certificate)(nil)).Elem()
}

func (o CertificateArrayOutput) ToCertificateArrayOutput() CertificateArrayOutput {
	return o
}

func (o CertificateArrayOutput) ToCertificateArrayOutputWithContext(ctx context.Context) CertificateArrayOutput {
	return o
}

func (o CertificateArrayOutput) Index(i pulumi.IntInput) CertificateOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Certificate {
		return vs[0].([]*Certificate)[vs[1].(int)]
	}).(CertificateOutput)
}

type CertificateMapOutput struct{ *pulumi.OutputState }

func (CertificateMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Certificate)(nil)).Elem()
}

func (o CertificateMapOutput) ToCertificateMapOutput() CertificateMapOutput {
	return o
}

func (o CertificateMapOutput) ToCertificateMapOutputWithContext(ctx context.Context) CertificateMapOutput {
	return o
}

func (o CertificateMapOutput) MapIndex(k pulumi.StringInput) CertificateOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Certificate {
		return vs[0].(map[string]*Certificate)[vs[1].(string)]
	}).(CertificateOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CertificateInput)(nil)).Elem(), &Certificate{})
	pulumi.RegisterInputType(reflect.TypeOf((*CertificateArrayInput)(nil)).Elem(), CertificateArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*CertificateMapInput)(nil)).Elem(), CertificateMap{})
	pulumi.RegisterOutputType(CertificateOutput{})
	pulumi.RegisterOutputType(CertificateArrayOutput{})
	pulumi.RegisterOutputType(CertificateMapOutput{})
}
