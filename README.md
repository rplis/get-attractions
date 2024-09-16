# Get Attractions

An API to find nearby tourist attractions using Google Maps API.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/YOUR_USERNAME/get-attractions.git
   cd get-attractions
   ```

2. Install Poetry (if not already installed):
   ```
   pip install poetry
   ```

3. Install dependencies:
   ```
   poetry install
   ```

4. Set up Google Cloud credentials and Secret Manager (see Configuration section).

## Configuration

1. Set up a Google Cloud project and enable the necessary APIs (Maps JavaScript API, Secret Manager API).
2. Store your Google Maps API key in Secret Manager:
   ```
   echo -n "YOUR_API_KEY" | gcloud secrets create google-maps-api-key --data-file=-
   ```
3. Update the `get_secret` function in `get_attractions/main.py` with your Google Cloud project ID.

## Usage

Run the API locally:

```
poetry run get-attractions
```

The API will be available at `http://localhost:8080`.

## Testing

Run tests using pytest:

```
poetry run pytest
```

## Deployment

See the `cloudbuild.yaml` file for CI/CD configuration with Google Cloud Build.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)