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

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class K8sExtensionsOperations(object):
    """K8sExtensionsOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach
    it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The API version to be used with the HTTP request. Constant value: "2020-07-01-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2020-07-01-preview"

        self.config = config

    def get(
            self, resource_group_name, cluster_rp, cluster_resource_name, cluster_name, extension_instance_name,
            custom_headers=None, raw=False, **operation_config):
        """Gets details of the Kubernetes Cluster Extension Instance.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param cluster_rp: The Kubernetes cluster RP - either
         Microsoft.ContainerService (for AKS clusters) or Microsoft.Kubernetes
         (for OnPrem K8S clusters). Possible values include:
         'Microsoft.ContainerService', 'Microsoft.Kubernetes'
        :type cluster_rp: str
        :param cluster_resource_name: The Kubernetes cluster resource name -
         either managedClusters (for AKS clusters) or connectedClusters (for
         OnPrem K8S clusters). Possible values include: 'managedClusters',
         'connectedClusters'
        :type cluster_resource_name: str
        :param cluster_name: The name of the kubernetes cluster.
        :type cluster_name: str
        :param extension_instance_name: Name of an instance of the Extension.
        :type extension_instance_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ExtensionInstance or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.kubernetesconfiguration.models.ExtensionInstance
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.kubernetesconfiguration.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'clusterRp': self._serialize.url("cluster_rp", cluster_rp, 'str'),
            'clusterResourceName': self._serialize.url("cluster_resource_name", cluster_resource_name, 'str'),
            'clusterName': self._serialize.url("cluster_name", cluster_name, 'str'),
            'extensionInstanceName': self._serialize.url("extension_instance_name", extension_instance_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language",
                                                                          self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ExtensionInstance', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/extensions/{extensionInstanceName}'}

    def create(
            self, resource_group_name, cluster_rp, cluster_resource_name, cluster_name, extension_instance_name,
            extension_instance, custom_headers=None, raw=False, **operation_config):
        """Create a new Kubernetes Cluster Extension Instance.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param cluster_rp: The Kubernetes cluster RP - either
         Microsoft.ContainerService (for AKS clusters) or Microsoft.Kubernetes
         (for OnPrem K8S clusters). Possible values include:
         'Microsoft.ContainerService', 'Microsoft.Kubernetes'
        :type cluster_rp: str
        :param cluster_resource_name: The Kubernetes cluster resource name -
         either managedClusters (for AKS clusters) or connectedClusters (for
         OnPrem K8S clusters). Possible values include: 'managedClusters',
         'connectedClusters'
        :type cluster_resource_name: str
        :param cluster_name: The name of the kubernetes cluster.
        :type cluster_name: str
        :param extension_instance_name: Name of an instance of the Extension.
        :type extension_instance_name: str
        :param extension_instance: Properties necessary to Create an Extension
         Instance.
        :type extension_instance:
         ~azure.mgmt.kubernetesconfiguration.models.ExtensionInstanceForCreate
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ExtensionInstance or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.kubernetesconfiguration.models.ExtensionInstance
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.kubernetesconfiguration.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'clusterRp': self._serialize.url("cluster_rp", cluster_rp, 'str'),
            'clusterResourceName': self._serialize.url("cluster_resource_name", cluster_resource_name, 'str'),
            'clusterName': self._serialize.url("cluster_name", cluster_name, 'str'),
            'extensionInstanceName': self._serialize.url("extension_instance_name", extension_instance_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language",
                                                                          self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(extension_instance, 'ExtensionInstanceForCreate')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ExtensionInstance', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/extensions/{extensionInstanceName}'}

    def update(
            self, resource_group_name, cluster_rp, cluster_resource_name, cluster_name, extension_instance_name,
            extension_instance, custom_headers=None, raw=False, **operation_config):
        """Update an existing Kubernetes Cluster Extension Instance.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param cluster_rp: The Kubernetes cluster RP - either
         Microsoft.ContainerService (for AKS clusters) or Microsoft.Kubernetes
         (for OnPrem K8S clusters). Possible values include:
         'Microsoft.ContainerService', 'Microsoft.Kubernetes'
        :type cluster_rp: str
        :param cluster_resource_name: The Kubernetes cluster resource name -
         either managedClusters (for AKS clusters) or connectedClusters (for
         OnPrem K8S clusters). Possible values include: 'managedClusters',
         'connectedClusters'
        :type cluster_resource_name: str
        :param cluster_name: The name of the kubernetes cluster.
        :type cluster_name: str
        :param extension_instance_name: Name of an instance of the Extension.
        :type extension_instance_name: str
        :param extension_instance: Properties to Update in the Extension
         Instance.
        :type extension_instance:
         ~azure.mgmt.kubernetesconfiguration.models.ExtensionInstanceUpdate
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ExtensionInstance or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.kubernetesconfiguration.models.ExtensionInstance
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.kubernetesconfiguration.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.update.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'clusterRp': self._serialize.url("cluster_rp", cluster_rp, 'str'),
            'clusterResourceName': self._serialize.url("cluster_resource_name", cluster_resource_name, 'str'),
            'clusterName': self._serialize.url("cluster_name", cluster_name, 'str'),
            'extensionInstanceName': self._serialize.url("extension_instance_name", extension_instance_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language",
                                                                          self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(extension_instance, 'ExtensionInstanceUpdate')

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ExtensionInstance', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/extensions/{extensionInstanceName}'}

    def delete(
            self, resource_group_name, cluster_rp, cluster_resource_name, cluster_name, extension_instance_name,
            custom_headers=None, raw=False, **operation_config):
        """Delete a Kubernetes Cluster Extension Instance. This will cause the
        Agent to Uninstall the extension instance from the cluster.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param cluster_rp: The Kubernetes cluster RP - either
         Microsoft.ContainerService (for AKS clusters) or Microsoft.Kubernetes
         (for OnPrem K8S clusters). Possible values include:
         'Microsoft.ContainerService', 'Microsoft.Kubernetes'
        :type cluster_rp: str
        :param cluster_resource_name: The Kubernetes cluster resource name -
         either managedClusters (for AKS clusters) or connectedClusters (for
         OnPrem K8S clusters). Possible values include: 'managedClusters',
         'connectedClusters'
        :type cluster_resource_name: str
        :param cluster_name: The name of the kubernetes cluster.
        :type cluster_name: str
        :param extension_instance_name: Name of an instance of the Extension.
        :type extension_instance_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.kubernetesconfiguration.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'clusterRp': self._serialize.url("cluster_rp", cluster_rp, 'str'),
            'clusterResourceName': self._serialize.url("cluster_resource_name", cluster_resource_name, 'str'),
            'clusterName': self._serialize.url("cluster_name", cluster_name, 'str'),
            'extensionInstanceName': self._serialize.url("extension_instance_name", extension_instance_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language",
                                                                          self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 204]:
            raise models.ErrorResponseException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/extensions/{extensionInstanceName}'}

    def list(
            self, resource_group_name, cluster_rp, cluster_resource_name, cluster_name, custom_headers=None, raw=False,
            **operation_config):
        """List all Extension Instances.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param cluster_rp: The Kubernetes cluster RP - either
         Microsoft.ContainerService (for AKS clusters) or Microsoft.Kubernetes
         (for OnPrem K8S clusters). Possible values include:
         'Microsoft.ContainerService', 'Microsoft.Kubernetes'
        :type cluster_rp: str
        :param cluster_resource_name: The Kubernetes cluster resource name -
         either managedClusters (for AKS clusters) or connectedClusters (for
         OnPrem K8S clusters). Possible values include: 'managedClusters',
         'connectedClusters'
        :type cluster_resource_name: str
        :param cluster_name: The name of the kubernetes cluster.
        :type cluster_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of ExtensionInstanceForList
        :rtype:
         ~azure.mgmt.kubernetesconfiguration.models.ExtensionInstanceForListPaged[~azure.mgmt.kubernetesconfiguration.models.ExtensionInstanceForList]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.kubernetesconfiguration.models.ErrorResponseException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id,
                                                          'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'clusterRp': self._serialize.url("cluster_rp", cluster_rp, 'str'),
                    'clusterResourceName': self._serialize.url("cluster_resource_name", cluster_resource_name, 'str'),
                    'clusterName': self._serialize.url("cluster_name", cluster_name, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language",
                                                                              self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.ErrorResponseException(self._deserialize, response)

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.ExtensionInstanceForListPaged(internal_paging, self._deserialize.dependencies,
                                                            header_dict)

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/extensions'}
