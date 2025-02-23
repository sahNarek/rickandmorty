"""
RickAndMorty API client
"""
import asyncio
from config import Config
from src.rm_controller import RickAndMortyResource
import json
import logging
from datetime import datetime


class RickAndMortyClient():
    """
    Client Class
    """

    def __init__(self, config: Config):
        self.config = config
        self.api_url = config.api_url
        self.workflows = config.workflows
        for workflow in self.workflows:
            setattr(self, f"{workflow}_payload", {})

    def dump_to_json(self, data: list, workflow: str):
        """
        Dump the data to a JSON file
        """
        logging.info(f"Dumping data for {workflow} to {workflow}.json")
        with open(f"{workflow}.json","w",encoding="utf-8") as file:
            setattr(self, f"{workflow}_payload", data)
            json.dump(data, file, indent=4)

    async def fetch_all(self, resource: RickAndMortyResource):
        """
        Fetch all data for a given resource and handle potential errors.
        """
        logging.info(f"Fetching data for {resource.name}")
        try:
            data = await resource.get_all()
            self.dump_to_json(data, f"{resource.name}")
            return True
        except Exception as e:
            logging.error(f"Error fetching data for {resource.name}: {e}")
            return False

    async def get_all_data(self):
        """
        Execute the workflows asynchronously and handle results/errors.
        """
        tasks = []
        for workflow in self.workflows:
            rm_resource = RickAndMortyResource(
                self.api_url,
                getattr(self.config, f"{workflow}_endpoint"),
                workflow
            )
            tasks.append(self.fetch_all(rm_resource))

        results = await asyncio.gather(*tasks, return_exceptions=True)

        for i, result in enumerate(results):
            workflow_name = self.workflows[i]
            if isinstance(result, Exception):
                logging.error(f"Workflow {workflow_name} raised an exception: {result}")
            elif result:
                logging.info(f"Workflow {workflow_name} completed successfully.")
            else:
                logging.error(f"Workflow {workflow_name} failed.")


    def filter_episodes(self, from_date: datetime, to_date: datetime):
        """
        Filter episodes by air date
        """
        episodes_payload = getattr(self, "episode_payload", {})
        episodes = episodes_payload.get("RawData", [])
        filtered_episodes = []
        for episode in episodes:
            air_date = datetime.strptime(
                episode.get("air_date",""),
                "%B %d, %Y"
            )
            if from_date <= air_date <= to_date:
                filtered_episodes.append(episode)
        return filtered_episodes
