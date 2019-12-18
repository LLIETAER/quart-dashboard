# -*- coding: utf-8 -*-
import unittest

import pytest

from endpoints.pages.functions import call_api


class Test(unittest.TestCase):
    def test_call_api(self):
        # with pytest.raises(Exception):
        result = call_api()
        assert len(result) != 0

    def test_call_api_error(self):
        # with pytest.raises(Exception):
        #     assert call_api()
        with pytest.raises(Exception):
            result = call_api()
            assert result is None
