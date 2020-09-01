# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class ComplianceStatus(Model):
    """Compliance Status details.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar compliance_state: The compliance state of the configuration.
     Possible values include: 'Pending', 'Compliant', 'Noncompliant',
     'Installed', 'Failed'
    :vartype compliance_state: str or
     ~azure.mgmt.kubernetesconfiguration.models.ComplianceState
    :param last_config_applied: Datetime the configuration was last applied.
    :type last_config_applied: datetime
    :param message: Message from when the configuration was applied.
    :type message: str
    :param message_level: Level of the message. Possible values include:
     'Error', 'Warning', 'Information'
    :type message_level: str or
     ~azure.mgmt.kubernetesconfiguration.models.MessageLevel
    """

    _validation = {
        'compliance_state': {'readonly': True},
    }

    _attribute_map = {
        'compliance_state': {'key': 'complianceState', 'type': 'str'},
        'last_config_applied': {'key': 'lastConfigApplied', 'type': 'iso-8601'},
        'message': {'key': 'message', 'type': 'str'},
        'message_level': {'key': 'messageLevel', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ComplianceStatus, self).__init__(**kwargs)
        self.compliance_state = None
        self.last_config_applied = kwargs.get('last_config_applied', None)
        self.message = kwargs.get('message', None)
        self.message_level = kwargs.get('message_level', None)


class ErrorDefinition(Model):
    """Error definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar code: Service specific error code which serves as the substatus for
     the HTTP error code.
    :vartype code: str
    :ivar message: Description of the error.
    :vartype message: str
    :ivar details: Internal error details.
    :vartype details:
     list[~azure.mgmt.kubernetesconfiguration.models.ErrorDefinition]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'details': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDefinition]'},
    }

    def __init__(self, **kwargs):
        super(ErrorDefinition, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.details = None


class ErrorResponse(Model):
    """Error response.

    :param error: Error definition.
    :type error: ~azure.mgmt.kubernetesconfiguration.models.ErrorDefinition
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDefinition'},
    }

    def __init__(self, **kwargs):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)


class HelmOperatorProperties(Model):
    """Properties for Helm operator.

    :param chart_version: Version of the operator Helm chart.
    :type chart_version: str
    :param chart_values: Values override for the operator Helm chart.
    :type chart_values: str
    """

    _attribute_map = {
        'chart_version': {'key': 'chartVersion', 'type': 'str'},
        'chart_values': {'key': 'chartValues', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(HelmOperatorProperties, self).__init__(**kwargs)
        self.chart_version = kwargs.get('chart_version', None)
        self.chart_values = kwargs.get('chart_values', None)


class Resource(Model):
    """The Resource model definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class ProxyResource(Resource):
    """ARM proxy resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ProxyResource, self).__init__(**kwargs)


class ResourceProviderOperation(Model):
    """Supported operation of this resource provider.

    :param name: Operation name, in format of
     {provider}/{resource}/{operation}
    :type name: str
    :param display: Display metadata associated with the operation.
    :type display:
     ~azure.mgmt.kubernetesconfiguration.models.ResourceProviderOperationDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'ResourceProviderOperationDisplay'},
    }

    def __init__(self, **kwargs):
        super(ResourceProviderOperation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)


class ResourceProviderOperationDisplay(Model):
    """Display metadata associated with the operation.

    :param provider: Resource provider: Microsoft KubernetesConfiguration.
    :type provider: str
    :param resource: Resource on which the operation is performed.
    :type resource: str
    :param operation: Type of operation: get, read, delete, etc.
    :type operation: str
    :param description: Description of this operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ResourceProviderOperationDisplay, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)
        self.description = kwargs.get('description', None)


class Result(Model):
    """Sample result definition.

    :param sample_property: Sample property of type string
    :type sample_property: str
    """

    _attribute_map = {
        'sample_property': {'key': 'sampleProperty', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Result, self).__init__(**kwargs)
        self.sample_property = kwargs.get('sample_property', None)


class SourceControlConfiguration(ProxyResource):
    """The SourceControl Configuration object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param repository_url: Url of the SourceControl Repository.
    :type repository_url: str
    :param operator_namespace: The namespace to which this operator is
     installed to. Maximum of 253 lower case alphanumeric characters, hyphen
     and period only. Default value: "default" .
    :type operator_namespace: str
    :param operator_instance_name: Instance name of the operator - identifying
     the specific configuration.
    :type operator_instance_name: str
    :param operator_type: Type of the operator. Possible values include:
     'Flux'
    :type operator_type: str or ~kubernetesconfiguration.models.OperatorType
    :param operator_params: Any Parameters for the Operator instance in string
     format.
    :type operator_params: str
    :param configuration_protected_settings: Any Secrets the User would like to create on
     the cluster.
    :type configuration_protected_settings: str
    :param operator_scope: Scope at which the operator will be installed.
     Possible values include: 'cluster', 'namespace'. Default value: "cluster"
     .
    :type operator_scope: str or ~kubernetesconfiguration.models.OperatorScope
    :ivar repository_public_key: Public Key associated with this SourceControl
     configuration (either generated within the cluster or provided by the
     user).
    :vartype repository_public_key: str
    :param enable_helm_operator: Option to enable Helm Operator for this git
     configuration. Possible values include: 'true', 'false'
    :type enable_helm_operator: str or
     ~kubernetesconfiguration.models.EnableHelmOperator
    :param helm_operator_properties: Properties for Helm operator.
    :type helm_operator_properties:
     ~kubernetesconfiguration.models.HelmOperatorProperties
    :ivar provisioning_state: The provisioning state of the resource provider.
     Possible values include: 'Accepted', 'Deleting', 'Running', 'Succeeded',
     'Failed'
    :vartype provisioning_state: str or
     ~kubernetesconfiguration.models.ProvisioningState
    :ivar compliance_status: Compliance Status of the Configuration
    :vartype compliance_status:
     ~kubernetesconfiguration.models.ComplianceStatus
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'repository_public_key': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'compliance_status': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'repository_url': {'key': 'properties.repositoryUrl', 'type': 'str'},
        'operator_namespace': {'key': 'properties.operatorNamespace', 'type': 'str'},
        'operator_instance_name': {'key': 'properties.operatorInstanceName', 'type': 'str'},
        'operator_type': {'key': 'properties.operatorType', 'type': 'str'},
        'operator_params': {'key': 'properties.operatorParams', 'type': 'str'},
        'configuration_protected_settings': {'key': 'properties.configurationProtectedSettings', 'type': 'str'},
        'operator_scope': {'key': 'properties.operatorScope', 'type': 'str'},
        'repository_public_key': {'key': 'properties.repositoryPublicKey', 'type': 'str'},
        'enable_helm_operator': {'key': 'properties.enableHelmOperator', 'type': 'str'},
        'helm_operator_properties': {'key': 'properties.helmOperatorProperties', 'type': 'HelmOperatorProperties'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'compliance_status': {'key': 'properties.complianceStatus', 'type': 'ComplianceStatus'},
    }

    def __init__(self, **kwargs):
        super(SourceControlConfiguration, self).__init__(**kwargs)
        self.repository_url = kwargs.get('repository_url', None)
        self.operator_namespace = kwargs.get('operator_namespace', "default")
        self.operator_instance_name = kwargs.get('operator_instance_name', None)
        self.operator_type = kwargs.get('operator_type', None)
        self.operator_params = kwargs.get('operator_params', None)
        self.configuration_protected_settings = kwargs.get('configuration_protected_settings', None)
        self.operator_scope = kwargs.get('operator_scope', "cluster")
        self.repository_public_key = None
        self.enable_helm_operator = kwargs.get('enable_helm_operator', None)
        self.helm_operator_properties = kwargs.get('helm_operator_properties', None)
        self.provisioning_state = None
        self.compliance_status = None

