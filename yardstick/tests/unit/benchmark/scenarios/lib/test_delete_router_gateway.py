##############################################################################
# Copyright (c) 2017 Huawei Technologies Co.,Ltd and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################
import unittest
import mock

from yardstick.benchmark.scenarios.lib.delete_router_gateway import DeleteRouterGateway


class DeleteRouterGatewayTestCase(unittest.TestCase):

    @mock.patch('yardstick.common.openstack_utils.get_neutron_client')
    @mock.patch('yardstick.common.openstack_utils.remove_gateway_router')
    def test_delete_router_gateway(self, mock_get_neutron_client, mock_remove_gateway_router):
        options = {
            'router_id': '123-123-123'
        }
        args = {"options": options}
        obj = DeleteRouterGateway(args, {})
        obj.run({})
        mock_get_neutron_client.assert_called_once()
        mock_remove_gateway_router.assert_called_once()
