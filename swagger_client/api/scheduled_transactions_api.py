# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ScheduledTransactionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_scheduled_transaction_by_id(self, budget_id, scheduled_transaction_id, **kwargs):  # noqa: E501
        """Single scheduled transaction  # noqa: E501

        Returns a single scheduled transaction  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scheduled_transaction_by_id(budget_id, scheduled_transaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str budget_id: The id of the budget (\"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget) (required)
        :param str scheduled_transaction_id: The id of the scheduled transaction (required)
        :return: ScheduledTransactionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_scheduled_transaction_by_id_with_http_info(budget_id, scheduled_transaction_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_scheduled_transaction_by_id_with_http_info(budget_id, scheduled_transaction_id, **kwargs)  # noqa: E501
            return data

    def get_scheduled_transaction_by_id_with_http_info(self, budget_id, scheduled_transaction_id, **kwargs):  # noqa: E501
        """Single scheduled transaction  # noqa: E501

        Returns a single scheduled transaction  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scheduled_transaction_by_id_with_http_info(budget_id, scheduled_transaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str budget_id: The id of the budget (\"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget) (required)
        :param str scheduled_transaction_id: The id of the scheduled transaction (required)
        :return: ScheduledTransactionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['budget_id', 'scheduled_transaction_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_scheduled_transaction_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'budget_id' is set
        if ('budget_id' not in params or
                params['budget_id'] is None):
            raise ValueError("Missing the required parameter `budget_id` when calling `get_scheduled_transaction_by_id`")  # noqa: E501
        # verify the required parameter 'scheduled_transaction_id' is set
        if ('scheduled_transaction_id' not in params or
                params['scheduled_transaction_id'] is None):
            raise ValueError("Missing the required parameter `scheduled_transaction_id` when calling `get_scheduled_transaction_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'budget_id' in params:
            path_params['budget_id'] = params['budget_id']  # noqa: E501
        if 'scheduled_transaction_id' in params:
            path_params['scheduled_transaction_id'] = params['scheduled_transaction_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/budgets/{budget_id}/scheduled_transactions/{scheduled_transaction_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ScheduledTransactionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_scheduled_transactions(self, budget_id, **kwargs):  # noqa: E501
        """List scheduled transactions  # noqa: E501

        Returns all scheduled transactions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scheduled_transactions(budget_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str budget_id: The id of the budget (\"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget) (required)
        :param int last_knowledge_of_server: The starting server knowledge.  If provided, only entities that have changed since last_knowledge_of_server will be included.
        :return: ScheduledTransactionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_scheduled_transactions_with_http_info(budget_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_scheduled_transactions_with_http_info(budget_id, **kwargs)  # noqa: E501
            return data

    def get_scheduled_transactions_with_http_info(self, budget_id, **kwargs):  # noqa: E501
        """List scheduled transactions  # noqa: E501

        Returns all scheduled transactions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_scheduled_transactions_with_http_info(budget_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str budget_id: The id of the budget (\"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.youneedabudget.com/#oauth-default-budget) (required)
        :param int last_knowledge_of_server: The starting server knowledge.  If provided, only entities that have changed since last_knowledge_of_server will be included.
        :return: ScheduledTransactionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['budget_id', 'last_knowledge_of_server']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_scheduled_transactions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'budget_id' is set
        if ('budget_id' not in params or
                params['budget_id'] is None):
            raise ValueError("Missing the required parameter `budget_id` when calling `get_scheduled_transactions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'budget_id' in params:
            path_params['budget_id'] = params['budget_id']  # noqa: E501

        query_params = []
        if 'last_knowledge_of_server' in params:
            query_params.append(('last_knowledge_of_server', params['last_knowledge_of_server']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/budgets/{budget_id}/scheduled_transactions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ScheduledTransactionsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
