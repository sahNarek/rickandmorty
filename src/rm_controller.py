"""
Resources class
"""
import requests
import aiohttp
import uuid
import logging

class RickAndMortyResource():
    """
    General class for the resorces in the API
    """
    def __init__(self, api_url: str, api_endpoint: str, name: str):
        self.api_url = api_url
        self.api_endpoint = api_endpoint
        self.name = name
        self.session = aiohttp.ClientSession()

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, *excinfo):
        if self.session:
            await self.session.close()

    def modify_payload(self, payload: dict):
        """
        Modify the payload of the request and add a uuid

        Args:
            payload (dict): Payload of the request

        Returns:
            dict: Modified payload
        """
        return {
            "id": str(uuid.uuid4()),
            "RawData": payload.copy()
        }

    async def get_all_pages(self, url: str):
        """
        Get all pages of a resource

        Args:
            url (str): URL of the resource

        Returns:
            list: List of all the resources
        """
        logging.info(f"Getting all pages of {url}")
        all_resources = []
        next_page_url = url
        current_page = 1
        while next_page_url:
            logging.info(f"Getting page: {current_page}")
            async with self.session.get(next_page_url) as response:
                resources = await response.json()
            all_resources += resources.get("results", [])
            all_resources.extend(resources.get("results", []))
            next_page_url = resources.get("info",{}).get("next", None)
            logging.info(f"Next page: {next_page_url}")
            current_page += 1
        await self.session.close()
        self.session = None
        return self.modify_payload(all_resources)

    async def get_all(self):
        """
        Get all instances of the resource
        """
        try:
            logging.info(f"Getting all {self.name}")
            all_pages = await self.get_all_pages(
                f"{self.api_url}/{self.api_endpoint}"
            )
            return all_pages
        except requests.exceptions.RequestException as request_error:
            logging.error(f"Error getting all {self.name}: {request_error}")
            return None
        