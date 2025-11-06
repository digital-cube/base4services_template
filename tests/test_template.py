import os
import time

import requests

current_file_path = os.path.abspath(os.path.dirname(__file__))
from .test_base import TestBase


class TestSVC(TestBase):
	services = ['tenants', '__SERVICE_NAME__']
	
	async def setup(self):
		await super().setup()
	
	async def test_is___SERVICE_NAME___healthy(self):
		response = await self.api(_method='get', _endpoint="/api/v4/__SERVICE_NAME__/healthy")
		assert response.status_code == 200
