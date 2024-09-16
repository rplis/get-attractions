from google.cloud import secretmanager


def get_secret(secret_id):
    """
    Retrieve the secret value from Google Cloud Secret Manager.

    Args:
        secret_id (str): The ID of the secret to retrieve.

    Returns:
        str: The secret value.
    """
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/436247147198/secrets/{secret_id}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

GOOGLE_MAPS_API_KEY = get_secret("google-maps-api-key")

