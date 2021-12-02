# Copyright (c) 2020, salesforce.com, inc.
# All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
# For full license text, see the LICENSE file in the repo root
# or https://opensource.org/licenses/BSD-3-Clause

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import intent_pb2 as intent_pb2


class IntentDetectionServiceStub(object):
    """
    Intent Predictor Service definition, accepts a model_id, document, classes with samples and returns class labels with
    probabilities for each.

    """

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self.IntentDetection = channel.unary_unary(
            "/IntentDetectionService/IntentDetection",
            request_serializer=intent_pb2.IntentDetectionRequest.SerializeToString,
            response_deserializer=intent_pb2.IntentDetectionResponse.FromString,
        )


class IntentDetectionServiceServicer(object):
    """
    Intent Predictor Service definition, accepts a model_id, document, classes with samples and returns class labels with
    probabilities for each.

    """

    def IntentDetection(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_IntentDetectionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "IntentDetection": grpc.unary_unary_rpc_method_handler(
            servicer.IntentDetection,
            request_deserializer=intent_pb2.IntentDetectionRequest.FromString,
            response_serializer=intent_pb2.IntentDetectionResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "IntentDetectionService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
