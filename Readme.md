# Rick and Morty API Integration

This project provides a Python integration connector for the Rick and Morty API. It fetches data for characters, episodes, and locations, saves the data to JSON files, and offers functionality to filter episodes by air date.  The project utilizes asynchronous programming for efficient data retrieval.

## Project Structure

# Rick and Morty API Integration

This project provides a Python integration connector for the Rick and Morty API. It fetches data for characters, episodes, and locations, saves the data to JSON files, and offers functionality to filter episodes by air date.The project utilizes asynchronous programming for efficient data retrieval.

## Project Structure

rick_and_morty_python/  
├── src/  
│   ├── rm_client.py        # Rick and Morty API client  
│   └── rm_controller.py    # Rick and Morty Resource handler  
├── config/  
│   └── __init__.py         # Configuration module  
└── main.py             # Main application script  
└── README.md           # This file  

## Usage


1.  **Run the application:**

    By default the script fetches all three resources, as per the task, if you want to fetch only one or two resource, modify the following line in main.py

    ```
    rm_client = RickAndMortyClient(
        config = Config(
            workflows=["character","episode","location"] # Modify this line if you want to exclude one of the resources from the program
        )
    )
    ```

    ```bash
    python main.py
    ```

This will fetch data for the configured resources (character, episode, location by default), save it to JSON files (e.g., `charachter.json`, `episode.json`, `location.json`), and log the progress and any errors to `debug.log` and the console.
