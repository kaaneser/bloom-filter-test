
#  Bloom Filter and Redis Cache Example

  

This project demonstrates the use of a **Bloom Filter** and **Redis Cache** for data querying and caching mechanisms. The project handles both Cache Hits and False Positive scenerios. Redis allows fast data caching, while Bloom Filter helps in preventing false positives in large datasets.

  

##  Requirements

To run this project, you'll need the following Python libraries

-  **redis**: For Redis database connection

-  **bitarray**: For Bloom Filter bit array operations

-  **mmh3**: For hashing (MurmurHash3)

Install the required libraries with the following command:

    pip install -r requirements.txt


## Usage

Before running the project, ensure that Redis is installed and running. You can start Redis using Docker with the following steps:

### Running Redis via docker-compose
Run redis in Docker with the following command:

    docker-compose up -d

### Running the Application
After Redis is running, execute `main.py` file to test the example queries:

    python main.py

## Project Flow

1.  **Adding Data to Bloom Filter**: When data is queried for the first time, it is checked against the Bloom Filter. If not present, the data is fetched from the database and cached in Redis. The item is then added to the Bloom Filter.
2.  **Cache Lookup**: If the data is found in the Bloom Filter, a cache lookup is performed. If the data is present in the Redis cache, it is returned directly. Otherwise, it is fetched from the database and cached for future queries.
3.  **False Positive Scenario**: If the Bloom Filter incorrectly marks an item as present (false positive), the application will still query the database and cache the result.

## Contributing

Feel free to open an issue or create a pull request if you'd like to contribute to the project. Any suggestions for improving the Bloom Filter implementation or optimizing the cache lookup are welcome.