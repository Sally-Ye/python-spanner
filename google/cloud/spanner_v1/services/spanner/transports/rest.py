# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.auth.transport.requests import AuthorizedSession  # type: ignore
import json  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.api_core import rest_helpers
from google.api_core import rest_streaming
from google.api_core import gapic_v1

from google.protobuf import json_format

from requests import __version__ as requests_version
import dataclasses
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings


from google.cloud.spanner_v1.types import commit_response
from google.cloud.spanner_v1.types import result_set
from google.cloud.spanner_v1.types import spanner
from google.cloud.spanner_v1.types import transaction
from google.protobuf import empty_pb2  # type: ignore


from .rest_base import _BaseSpannerRestTransport
from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=f"requests@{requests_version}",
)


class SpannerRestInterceptor:
    """Interceptor for Spanner.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the SpannerRestTransport.

    .. code-block:: python
        class MyCustomSpannerInterceptor(SpannerRestInterceptor):
            def pre_batch_create_sessions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_sessions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_write(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_write(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_begin_transaction(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_begin_transaction(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_commit(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_commit(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_session(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_session(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_session(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_execute_batch_dml(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_execute_batch_dml(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_execute_sql(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_execute_sql(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_execute_streaming_sql(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_execute_streaming_sql(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_session(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_session(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_sessions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_sessions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_partition_query(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_partition_query(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_partition_read(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_partition_read(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_read(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_read(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_rollback(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_streaming_read(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_streaming_read(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = SpannerRestTransport(interceptor=MyCustomSpannerInterceptor())
        client = SpannerClient(transport=transport)


    """

    def pre_batch_create_sessions(
        self,
        request: spanner.BatchCreateSessionsRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[spanner.BatchCreateSessionsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for batch_create_sessions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Spanner server.
        """
        return request, metadata

    def post_batch_create_sessions(
        self, response: spanner.BatchCreateSessionsResponse
    ) -> spanner.BatchCreateSessionsResponse:
        """Post-rpc interceptor for batch_create_sessions

        Override in a subclass to manipulate the response
        after it is returned by the Spanner server but before
        it is returned to user code.
        """
        return response

    def pre_batch_write(
        self, request: spanner.BatchWriteRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[spanner.BatchWriteRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for batch_write

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Spanner server.
        """
        return request, metadata

    def post_batch_write(
        self, response: rest_streaming.ResponseIterator
    ) -> rest_streaming.ResponseIterator:
        """Post-rpc interceptor for batch_write

        Override in a subclass to manipulate the response
        after it is returned by the Spanner server but before
        it is returned to user code.
        """
        return response

    def pre_begin_transaction(
        self,
        request: spanner.BeginTransactionRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[spanner.BeginTransactionRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for begin_transaction

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Spanner server.
        """
        return request, metadata

    def post_begin_transaction(
        self, response: transaction.Transaction
    ) -> transaction.Transaction:
        """Post-rpc interceptor for begin_transaction

        Override in a subclass to manipulate the response
        after it is returned by the Spanner server but before
        it is returned to user code.
        """
        return response

    def pre_commit(
        self, request: spanner.CommitRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[spanner.CommitRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for commit

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Spanner server.
        """
        return request, metadata

    def post_commit(
        self, response: commit_response.CommitResponse
    ) -> commit_response.CommitResponse:
        """Post-rpc interceptor for commit

        Override in a subclass to manipulate the response
        after it is returned by the Spanner server but before
        it is returned to user code.
        """
        return response

    def pre_create_session(
        self, request: spanner.CreateSessionRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[spanner.CreateSessionRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_session

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Spanner server.
        """
        return request, metadata

    def post_create_session(self, response: spanner.Session) -> spanner.Session:
        """Post-rpc interceptor for create_session

        Override in a subclass to manipulate the response
        after it is returned by the Spanner server but before
        it is returned to user code.
        """
        return response

    def pre_delete_session(
        self, request: spanner.DeleteSessionRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[spanner.DeleteSessionRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_session

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Spanner server.
        """
        return request, metadata

    def pre_execute_batch_dml(
        self,
        request: spanner.ExecuteBatchDmlRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[spanner.ExecuteBatchDmlRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for execute_batch_dml

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Spanner server.
        """
        return request, metadata

    def post_execute_batch_dml(
        self, response: spanner.ExecuteBatchDmlResponse
    ) -> spanner.ExecuteBatchDmlResponse:
        """Post-rpc interceptor for execute_batch_dml

        Override in a subclass to manipulate the response
        after it is returned by the Spanner server but before
        it is returned to user code.
        """
        return response

    def pre_execute_sql(
        self, request: spanner.ExecuteSqlRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[spanner.ExecuteSqlRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for execute_sql

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Spanner server.
        """
        return request, metadata

    def post_execute_sql(self, response: result_set.ResultSet) -> result_set.ResultSet:
        """Post-rpc interceptor for execute_sql

        Override in a subclass to manipulate the response
        after it is returned by the Spanner server but before
        it is returned to user code.
        """
        return response

    def pre_execute_streaming_sql(
        self, request: spanner.ExecuteSqlRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[spanner.ExecuteSqlRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for execute_streaming_sql

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Spanner server.
        """
        return request, metadata

    def post_execute_streaming_sql(
        self, response: rest_streaming.ResponseIterator
    ) -> rest_streaming.ResponseIterator:
        """Post-rpc interceptor for execute_streaming_sql

        Override in a subclass to manipulate the response
        after it is returned by the Spanner server but before
        it is returned to user code.
        """
        return response

    def pre_get_session(
        self, request: spanner.GetSessionRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[spanner.GetSessionRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_session

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Spanner server.
        """
        return request, metadata

    def post_get_session(self, response: spanner.Session) -> spanner.Session:
        """Post-rpc interceptor for get_session

        Override in a subclass to manipulate the response
        after it is returned by the Spanner server but before
        it is returned to user code.
        """
        return response

    def pre_list_sessions(
        self, request: spanner.ListSessionsRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[spanner.ListSessionsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_sessions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Spanner server.
        """
        return request, metadata

    def post_list_sessions(
        self, response: spanner.ListSessionsResponse
    ) -> spanner.ListSessionsResponse:
        """Post-rpc interceptor for list_sessions

        Override in a subclass to manipulate the response
        after it is returned by the Spanner server but before
        it is returned to user code.
        """
        return response

    def pre_partition_query(
        self,
        request: spanner.PartitionQueryRequest,
        metadata: Sequence[Tuple[str, str]],
    ) -> Tuple[spanner.PartitionQueryRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for partition_query

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Spanner server.
        """
        return request, metadata

    def post_partition_query(
        self, response: spanner.PartitionResponse
    ) -> spanner.PartitionResponse:
        """Post-rpc interceptor for partition_query

        Override in a subclass to manipulate the response
        after it is returned by the Spanner server but before
        it is returned to user code.
        """
        return response

    def pre_partition_read(
        self, request: spanner.PartitionReadRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[spanner.PartitionReadRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for partition_read

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Spanner server.
        """
        return request, metadata

    def post_partition_read(
        self, response: spanner.PartitionResponse
    ) -> spanner.PartitionResponse:
        """Post-rpc interceptor for partition_read

        Override in a subclass to manipulate the response
        after it is returned by the Spanner server but before
        it is returned to user code.
        """
        return response

    def pre_read(
        self, request: spanner.ReadRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[spanner.ReadRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for read

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Spanner server.
        """
        return request, metadata

    def post_read(self, response: result_set.ResultSet) -> result_set.ResultSet:
        """Post-rpc interceptor for read

        Override in a subclass to manipulate the response
        after it is returned by the Spanner server but before
        it is returned to user code.
        """
        return response

    def pre_rollback(
        self, request: spanner.RollbackRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[spanner.RollbackRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for rollback

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Spanner server.
        """
        return request, metadata

    def pre_streaming_read(
        self, request: spanner.ReadRequest, metadata: Sequence[Tuple[str, str]]
    ) -> Tuple[spanner.ReadRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for streaming_read

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Spanner server.
        """
        return request, metadata

    def post_streaming_read(
        self, response: rest_streaming.ResponseIterator
    ) -> rest_streaming.ResponseIterator:
        """Post-rpc interceptor for streaming_read

        Override in a subclass to manipulate the response
        after it is returned by the Spanner server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class SpannerRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: SpannerRestInterceptor


class SpannerRestTransport(_BaseSpannerRestTransport):
    """REST backend synchronous transport for Spanner.

    Cloud Spanner API

    The Cloud Spanner API can be used to manage sessions and execute
    transactions on data stored in Cloud Spanner databases.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "spanner.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[SpannerRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'spanner.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.

            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            url_scheme=url_scheme,
            api_audience=api_audience,
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST
        )
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or SpannerRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchCreateSessions(
        _BaseSpannerRestTransport._BaseBatchCreateSessions, SpannerRestStub
    ):
        def __hash__(self):
            return hash("SpannerRestTransport.BatchCreateSessions")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: spanner.BatchCreateSessionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> spanner.BatchCreateSessionsResponse:
            r"""Call the batch create sessions method over HTTP.

            Args:
                request (~.spanner.BatchCreateSessionsRequest):
                    The request object. The request for
                [BatchCreateSessions][google.spanner.v1.Spanner.BatchCreateSessions].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.spanner.BatchCreateSessionsResponse:
                    The response for
                [BatchCreateSessions][google.spanner.v1.Spanner.BatchCreateSessions].

            """

            http_options = (
                _BaseSpannerRestTransport._BaseBatchCreateSessions._get_http_options()
            )
            request, metadata = self._interceptor.pre_batch_create_sessions(
                request, metadata
            )
            transcoded_request = _BaseSpannerRestTransport._BaseBatchCreateSessions._get_transcoded_request(
                http_options, request
            )

            body = _BaseSpannerRestTransport._BaseBatchCreateSessions._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseSpannerRestTransport._BaseBatchCreateSessions._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = SpannerRestTransport._BatchCreateSessions._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = spanner.BatchCreateSessionsResponse()
            pb_resp = spanner.BatchCreateSessionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_batch_create_sessions(resp)
            return resp

    class _BatchWrite(_BaseSpannerRestTransport._BaseBatchWrite, SpannerRestStub):
        def __hash__(self):
            return hash("SpannerRestTransport.BatchWrite")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                stream=True,
            )
            return response

        def __call__(
            self,
            request: spanner.BatchWriteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> rest_streaming.ResponseIterator:
            r"""Call the batch write method over HTTP.

            Args:
                request (~.spanner.BatchWriteRequest):
                    The request object. The request for
                [BatchWrite][google.spanner.v1.Spanner.BatchWrite].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.spanner.BatchWriteResponse:
                    The result of applying a batch of
                mutations.

            """

            http_options = _BaseSpannerRestTransport._BaseBatchWrite._get_http_options()
            request, metadata = self._interceptor.pre_batch_write(request, metadata)
            transcoded_request = (
                _BaseSpannerRestTransport._BaseBatchWrite._get_transcoded_request(
                    http_options, request
                )
            )

            body = _BaseSpannerRestTransport._BaseBatchWrite._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = (
                _BaseSpannerRestTransport._BaseBatchWrite._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = SpannerRestTransport._BatchWrite._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = rest_streaming.ResponseIterator(response, spanner.BatchWriteResponse)
            resp = self._interceptor.post_batch_write(resp)
            return resp

    class _BeginTransaction(
        _BaseSpannerRestTransport._BaseBeginTransaction, SpannerRestStub
    ):
        def __hash__(self):
            return hash("SpannerRestTransport.BeginTransaction")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: spanner.BeginTransactionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> transaction.Transaction:
            r"""Call the begin transaction method over HTTP.

            Args:
                request (~.spanner.BeginTransactionRequest):
                    The request object. The request for
                [BeginTransaction][google.spanner.v1.Spanner.BeginTransaction].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.transaction.Transaction:
                    A transaction.
            """

            http_options = (
                _BaseSpannerRestTransport._BaseBeginTransaction._get_http_options()
            )
            request, metadata = self._interceptor.pre_begin_transaction(
                request, metadata
            )
            transcoded_request = (
                _BaseSpannerRestTransport._BaseBeginTransaction._get_transcoded_request(
                    http_options, request
                )
            )

            body = (
                _BaseSpannerRestTransport._BaseBeginTransaction._get_request_body_json(
                    transcoded_request
                )
            )

            # Jsonify the query params
            query_params = (
                _BaseSpannerRestTransport._BaseBeginTransaction._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = SpannerRestTransport._BeginTransaction._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = transaction.Transaction()
            pb_resp = transaction.Transaction.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_begin_transaction(resp)
            return resp

    class _Commit(_BaseSpannerRestTransport._BaseCommit, SpannerRestStub):
        def __hash__(self):
            return hash("SpannerRestTransport.Commit")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: spanner.CommitRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> commit_response.CommitResponse:
            r"""Call the commit method over HTTP.

            Args:
                request (~.spanner.CommitRequest):
                    The request object. The request for
                [Commit][google.spanner.v1.Spanner.Commit].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.commit_response.CommitResponse:
                    The response for
                [Commit][google.spanner.v1.Spanner.Commit].

            """

            http_options = _BaseSpannerRestTransport._BaseCommit._get_http_options()
            request, metadata = self._interceptor.pre_commit(request, metadata)
            transcoded_request = (
                _BaseSpannerRestTransport._BaseCommit._get_transcoded_request(
                    http_options, request
                )
            )

            body = _BaseSpannerRestTransport._BaseCommit._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseSpannerRestTransport._BaseCommit._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = SpannerRestTransport._Commit._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = commit_response.CommitResponse()
            pb_resp = commit_response.CommitResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_commit(resp)
            return resp

    class _CreateSession(_BaseSpannerRestTransport._BaseCreateSession, SpannerRestStub):
        def __hash__(self):
            return hash("SpannerRestTransport.CreateSession")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: spanner.CreateSessionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> spanner.Session:
            r"""Call the create session method over HTTP.

            Args:
                request (~.spanner.CreateSessionRequest):
                    The request object. The request for
                [CreateSession][google.spanner.v1.Spanner.CreateSession].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.spanner.Session:
                    A session in the Cloud Spanner API.
            """

            http_options = (
                _BaseSpannerRestTransport._BaseCreateSession._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_session(request, metadata)
            transcoded_request = (
                _BaseSpannerRestTransport._BaseCreateSession._get_transcoded_request(
                    http_options, request
                )
            )

            body = _BaseSpannerRestTransport._BaseCreateSession._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = (
                _BaseSpannerRestTransport._BaseCreateSession._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = SpannerRestTransport._CreateSession._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = spanner.Session()
            pb_resp = spanner.Session.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_session(resp)
            return resp

    class _DeleteSession(_BaseSpannerRestTransport._BaseDeleteSession, SpannerRestStub):
        def __hash__(self):
            return hash("SpannerRestTransport.DeleteSession")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: spanner.DeleteSessionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ):
            r"""Call the delete session method over HTTP.

            Args:
                request (~.spanner.DeleteSessionRequest):
                    The request object. The request for
                [DeleteSession][google.spanner.v1.Spanner.DeleteSession].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options = (
                _BaseSpannerRestTransport._BaseDeleteSession._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_session(request, metadata)
            transcoded_request = (
                _BaseSpannerRestTransport._BaseDeleteSession._get_transcoded_request(
                    http_options, request
                )
            )

            # Jsonify the query params
            query_params = (
                _BaseSpannerRestTransport._BaseDeleteSession._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = SpannerRestTransport._DeleteSession._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _ExecuteBatchDml(
        _BaseSpannerRestTransport._BaseExecuteBatchDml, SpannerRestStub
    ):
        def __hash__(self):
            return hash("SpannerRestTransport.ExecuteBatchDml")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: spanner.ExecuteBatchDmlRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> spanner.ExecuteBatchDmlResponse:
            r"""Call the execute batch dml method over HTTP.

            Args:
                request (~.spanner.ExecuteBatchDmlRequest):
                    The request object. The request for
                [ExecuteBatchDml][google.spanner.v1.Spanner.ExecuteBatchDml].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.spanner.ExecuteBatchDmlResponse:
                    The response for
                [ExecuteBatchDml][google.spanner.v1.Spanner.ExecuteBatchDml].
                Contains a list of
                [ResultSet][google.spanner.v1.ResultSet] messages, one
                for each DML statement that has successfully executed,
                in the same order as the statements in the request. If a
                statement fails, the status in the response body
                identifies the cause of the failure.

                To check for DML statements that failed, use the
                following approach:

                1. Check the status in the response message. The
                   [google.rpc.Code][google.rpc.Code] enum value ``OK``
                   indicates that all statements were executed
                   successfully.
                2. If the status was not ``OK``, check the number of
                   result sets in the response. If the response contains
                   ``N`` [ResultSet][google.spanner.v1.ResultSet]
                   messages, then statement ``N+1`` in the request
                   failed.

                Example 1:

                -  Request: 5 DML statements, all executed successfully.
                -  Response: 5 [ResultSet][google.spanner.v1.ResultSet]
                   messages, with the status ``OK``.

                Example 2:

                -  Request: 5 DML statements. The third statement has a
                   syntax error.
                -  Response: 2 [ResultSet][google.spanner.v1.ResultSet]
                   messages, and a syntax error (``INVALID_ARGUMENT``)
                   status. The number of
                   [ResultSet][google.spanner.v1.ResultSet] messages
                   indicates that the third statement failed, and the
                   fourth and fifth statements were not executed.

            """

            http_options = (
                _BaseSpannerRestTransport._BaseExecuteBatchDml._get_http_options()
            )
            request, metadata = self._interceptor.pre_execute_batch_dml(
                request, metadata
            )
            transcoded_request = (
                _BaseSpannerRestTransport._BaseExecuteBatchDml._get_transcoded_request(
                    http_options, request
                )
            )

            body = (
                _BaseSpannerRestTransport._BaseExecuteBatchDml._get_request_body_json(
                    transcoded_request
                )
            )

            # Jsonify the query params
            query_params = (
                _BaseSpannerRestTransport._BaseExecuteBatchDml._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = SpannerRestTransport._ExecuteBatchDml._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = spanner.ExecuteBatchDmlResponse()
            pb_resp = spanner.ExecuteBatchDmlResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_execute_batch_dml(resp)
            return resp

    class _ExecuteSql(_BaseSpannerRestTransport._BaseExecuteSql, SpannerRestStub):
        def __hash__(self):
            return hash("SpannerRestTransport.ExecuteSql")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: spanner.ExecuteSqlRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> result_set.ResultSet:
            r"""Call the execute sql method over HTTP.

            Args:
                request (~.spanner.ExecuteSqlRequest):
                    The request object. The request for
                [ExecuteSql][google.spanner.v1.Spanner.ExecuteSql] and
                [ExecuteStreamingSql][google.spanner.v1.Spanner.ExecuteStreamingSql].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.result_set.ResultSet:
                    Results from [Read][google.spanner.v1.Spanner.Read] or
                [ExecuteSql][google.spanner.v1.Spanner.ExecuteSql].

            """

            http_options = _BaseSpannerRestTransport._BaseExecuteSql._get_http_options()
            request, metadata = self._interceptor.pre_execute_sql(request, metadata)
            transcoded_request = (
                _BaseSpannerRestTransport._BaseExecuteSql._get_transcoded_request(
                    http_options, request
                )
            )

            body = _BaseSpannerRestTransport._BaseExecuteSql._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = (
                _BaseSpannerRestTransport._BaseExecuteSql._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = SpannerRestTransport._ExecuteSql._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = result_set.ResultSet()
            pb_resp = result_set.ResultSet.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_execute_sql(resp)
            return resp

    class _ExecuteStreamingSql(
        _BaseSpannerRestTransport._BaseExecuteStreamingSql, SpannerRestStub
    ):
        def __hash__(self):
            return hash("SpannerRestTransport.ExecuteStreamingSql")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                stream=True,
            )
            return response

        def __call__(
            self,
            request: spanner.ExecuteSqlRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> rest_streaming.ResponseIterator:
            r"""Call the execute streaming sql method over HTTP.

            Args:
                request (~.spanner.ExecuteSqlRequest):
                    The request object. The request for
                [ExecuteSql][google.spanner.v1.Spanner.ExecuteSql] and
                [ExecuteStreamingSql][google.spanner.v1.Spanner.ExecuteStreamingSql].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.result_set.PartialResultSet:
                    Partial results from a streaming read
                or SQL query. Streaming reads and SQL
                queries better tolerate large result
                sets, large rows, and large values, but
                are a little trickier to consume.

            """

            http_options = (
                _BaseSpannerRestTransport._BaseExecuteStreamingSql._get_http_options()
            )
            request, metadata = self._interceptor.pre_execute_streaming_sql(
                request, metadata
            )
            transcoded_request = _BaseSpannerRestTransport._BaseExecuteStreamingSql._get_transcoded_request(
                http_options, request
            )

            body = _BaseSpannerRestTransport._BaseExecuteStreamingSql._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseSpannerRestTransport._BaseExecuteStreamingSql._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = SpannerRestTransport._ExecuteStreamingSql._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = rest_streaming.ResponseIterator(
                response, result_set.PartialResultSet
            )
            resp = self._interceptor.post_execute_streaming_sql(resp)
            return resp

    class _GetSession(_BaseSpannerRestTransport._BaseGetSession, SpannerRestStub):
        def __hash__(self):
            return hash("SpannerRestTransport.GetSession")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: spanner.GetSessionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> spanner.Session:
            r"""Call the get session method over HTTP.

            Args:
                request (~.spanner.GetSessionRequest):
                    The request object. The request for
                [GetSession][google.spanner.v1.Spanner.GetSession].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.spanner.Session:
                    A session in the Cloud Spanner API.
            """

            http_options = _BaseSpannerRestTransport._BaseGetSession._get_http_options()
            request, metadata = self._interceptor.pre_get_session(request, metadata)
            transcoded_request = (
                _BaseSpannerRestTransport._BaseGetSession._get_transcoded_request(
                    http_options, request
                )
            )

            # Jsonify the query params
            query_params = (
                _BaseSpannerRestTransport._BaseGetSession._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = SpannerRestTransport._GetSession._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = spanner.Session()
            pb_resp = spanner.Session.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_session(resp)
            return resp

    class _ListSessions(_BaseSpannerRestTransport._BaseListSessions, SpannerRestStub):
        def __hash__(self):
            return hash("SpannerRestTransport.ListSessions")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: spanner.ListSessionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> spanner.ListSessionsResponse:
            r"""Call the list sessions method over HTTP.

            Args:
                request (~.spanner.ListSessionsRequest):
                    The request object. The request for
                [ListSessions][google.spanner.v1.Spanner.ListSessions].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.spanner.ListSessionsResponse:
                    The response for
                [ListSessions][google.spanner.v1.Spanner.ListSessions].

            """

            http_options = (
                _BaseSpannerRestTransport._BaseListSessions._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_sessions(request, metadata)
            transcoded_request = (
                _BaseSpannerRestTransport._BaseListSessions._get_transcoded_request(
                    http_options, request
                )
            )

            # Jsonify the query params
            query_params = (
                _BaseSpannerRestTransport._BaseListSessions._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = SpannerRestTransport._ListSessions._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = spanner.ListSessionsResponse()
            pb_resp = spanner.ListSessionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_sessions(resp)
            return resp

    class _PartitionQuery(
        _BaseSpannerRestTransport._BasePartitionQuery, SpannerRestStub
    ):
        def __hash__(self):
            return hash("SpannerRestTransport.PartitionQuery")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: spanner.PartitionQueryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> spanner.PartitionResponse:
            r"""Call the partition query method over HTTP.

            Args:
                request (~.spanner.PartitionQueryRequest):
                    The request object. The request for
                [PartitionQuery][google.spanner.v1.Spanner.PartitionQuery]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.spanner.PartitionResponse:
                    The response for
                [PartitionQuery][google.spanner.v1.Spanner.PartitionQuery]
                or
                [PartitionRead][google.spanner.v1.Spanner.PartitionRead]

            """

            http_options = (
                _BaseSpannerRestTransport._BasePartitionQuery._get_http_options()
            )
            request, metadata = self._interceptor.pre_partition_query(request, metadata)
            transcoded_request = (
                _BaseSpannerRestTransport._BasePartitionQuery._get_transcoded_request(
                    http_options, request
                )
            )

            body = _BaseSpannerRestTransport._BasePartitionQuery._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = (
                _BaseSpannerRestTransport._BasePartitionQuery._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = SpannerRestTransport._PartitionQuery._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = spanner.PartitionResponse()
            pb_resp = spanner.PartitionResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_partition_query(resp)
            return resp

    class _PartitionRead(_BaseSpannerRestTransport._BasePartitionRead, SpannerRestStub):
        def __hash__(self):
            return hash("SpannerRestTransport.PartitionRead")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: spanner.PartitionReadRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> spanner.PartitionResponse:
            r"""Call the partition read method over HTTP.

            Args:
                request (~.spanner.PartitionReadRequest):
                    The request object. The request for
                [PartitionRead][google.spanner.v1.Spanner.PartitionRead]
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.spanner.PartitionResponse:
                    The response for
                [PartitionQuery][google.spanner.v1.Spanner.PartitionQuery]
                or
                [PartitionRead][google.spanner.v1.Spanner.PartitionRead]

            """

            http_options = (
                _BaseSpannerRestTransport._BasePartitionRead._get_http_options()
            )
            request, metadata = self._interceptor.pre_partition_read(request, metadata)
            transcoded_request = (
                _BaseSpannerRestTransport._BasePartitionRead._get_transcoded_request(
                    http_options, request
                )
            )

            body = _BaseSpannerRestTransport._BasePartitionRead._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = (
                _BaseSpannerRestTransport._BasePartitionRead._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = SpannerRestTransport._PartitionRead._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = spanner.PartitionResponse()
            pb_resp = spanner.PartitionResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_partition_read(resp)
            return resp

    class _Read(_BaseSpannerRestTransport._BaseRead, SpannerRestStub):
        def __hash__(self):
            return hash("SpannerRestTransport.Read")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: spanner.ReadRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> result_set.ResultSet:
            r"""Call the read method over HTTP.

            Args:
                request (~.spanner.ReadRequest):
                    The request object. The request for [Read][google.spanner.v1.Spanner.Read]
                and
                [StreamingRead][google.spanner.v1.Spanner.StreamingRead].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.result_set.ResultSet:
                    Results from [Read][google.spanner.v1.Spanner.Read] or
                [ExecuteSql][google.spanner.v1.Spanner.ExecuteSql].

            """

            http_options = _BaseSpannerRestTransport._BaseRead._get_http_options()
            request, metadata = self._interceptor.pre_read(request, metadata)
            transcoded_request = (
                _BaseSpannerRestTransport._BaseRead._get_transcoded_request(
                    http_options, request
                )
            )

            body = _BaseSpannerRestTransport._BaseRead._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = _BaseSpannerRestTransport._BaseRead._get_query_params_json(
                transcoded_request
            )

            # Send the request
            response = SpannerRestTransport._Read._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = result_set.ResultSet()
            pb_resp = result_set.ResultSet.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_read(resp)
            return resp

    class _Rollback(_BaseSpannerRestTransport._BaseRollback, SpannerRestStub):
        def __hash__(self):
            return hash("SpannerRestTransport.Rollback")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: spanner.RollbackRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ):
            r"""Call the rollback method over HTTP.

            Args:
                request (~.spanner.RollbackRequest):
                    The request object. The request for
                [Rollback][google.spanner.v1.Spanner.Rollback].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options = _BaseSpannerRestTransport._BaseRollback._get_http_options()
            request, metadata = self._interceptor.pre_rollback(request, metadata)
            transcoded_request = (
                _BaseSpannerRestTransport._BaseRollback._get_transcoded_request(
                    http_options, request
                )
            )

            body = _BaseSpannerRestTransport._BaseRollback._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = (
                _BaseSpannerRestTransport._BaseRollback._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = SpannerRestTransport._Rollback._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _StreamingRead(_BaseSpannerRestTransport._BaseStreamingRead, SpannerRestStub):
        def __hash__(self):
            return hash("SpannerRestTransport.StreamingRead")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
                stream=True,
            )
            return response

        def __call__(
            self,
            request: spanner.ReadRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, str]] = (),
        ) -> rest_streaming.ResponseIterator:
            r"""Call the streaming read method over HTTP.

            Args:
                request (~.spanner.ReadRequest):
                    The request object. The request for [Read][google.spanner.v1.Spanner.Read]
                and
                [StreamingRead][google.spanner.v1.Spanner.StreamingRead].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.result_set.PartialResultSet:
                    Partial results from a streaming read
                or SQL query. Streaming reads and SQL
                queries better tolerate large result
                sets, large rows, and large values, but
                are a little trickier to consume.

            """

            http_options = (
                _BaseSpannerRestTransport._BaseStreamingRead._get_http_options()
            )
            request, metadata = self._interceptor.pre_streaming_read(request, metadata)
            transcoded_request = (
                _BaseSpannerRestTransport._BaseStreamingRead._get_transcoded_request(
                    http_options, request
                )
            )

            body = _BaseSpannerRestTransport._BaseStreamingRead._get_request_body_json(
                transcoded_request
            )

            # Jsonify the query params
            query_params = (
                _BaseSpannerRestTransport._BaseStreamingRead._get_query_params_json(
                    transcoded_request
                )
            )

            # Send the request
            response = SpannerRestTransport._StreamingRead._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = rest_streaming.ResponseIterator(
                response, result_set.PartialResultSet
            )
            resp = self._interceptor.post_streaming_read(resp)
            return resp

    @property
    def batch_create_sessions(
        self,
    ) -> Callable[
        [spanner.BatchCreateSessionsRequest], spanner.BatchCreateSessionsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateSessions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_write(
        self,
    ) -> Callable[[spanner.BatchWriteRequest], spanner.BatchWriteResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchWrite(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def begin_transaction(
        self,
    ) -> Callable[[spanner.BeginTransactionRequest], transaction.Transaction]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BeginTransaction(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def commit(
        self,
    ) -> Callable[[spanner.CommitRequest], commit_response.CommitResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Commit(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_session(
        self,
    ) -> Callable[[spanner.CreateSessionRequest], spanner.Session]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSession(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_session(
        self,
    ) -> Callable[[spanner.DeleteSessionRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteSession(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def execute_batch_dml(
        self,
    ) -> Callable[[spanner.ExecuteBatchDmlRequest], spanner.ExecuteBatchDmlResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExecuteBatchDml(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def execute_sql(
        self,
    ) -> Callable[[spanner.ExecuteSqlRequest], result_set.ResultSet]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExecuteSql(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def execute_streaming_sql(
        self,
    ) -> Callable[[spanner.ExecuteSqlRequest], result_set.PartialResultSet]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExecuteStreamingSql(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_session(self) -> Callable[[spanner.GetSessionRequest], spanner.Session]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSession(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_sessions(
        self,
    ) -> Callable[[spanner.ListSessionsRequest], spanner.ListSessionsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSessions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def partition_query(
        self,
    ) -> Callable[[spanner.PartitionQueryRequest], spanner.PartitionResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PartitionQuery(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def partition_read(
        self,
    ) -> Callable[[spanner.PartitionReadRequest], spanner.PartitionResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PartitionRead(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def read(self) -> Callable[[spanner.ReadRequest], result_set.ResultSet]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Read(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def rollback(self) -> Callable[[spanner.RollbackRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Rollback(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def streaming_read(
        self,
    ) -> Callable[[spanner.ReadRequest], result_set.PartialResultSet]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StreamingRead(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("SpannerRestTransport",)
