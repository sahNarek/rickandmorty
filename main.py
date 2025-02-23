import logging
import sys
from src.rm_client import RickAndMortyClient
from config import Config
import asyncio
import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

async def main():
    """
    Main method
    """
    rm_client = RickAndMortyClient(
        config = Config(
            workflows=["character","episode","location"]
        )
    )
    await rm_client.get_all_data()
    logging.info("Printing the filtered episodes")
    print(rm_client.filter_episodes(
        from_date = datetime.datetime(2017,1,1),
        to_date = datetime.datetime(2020,12,31)
    ))

if __name__ == "__main__":
    asyncio.run(main())
