# Reads a PDF from a Google Cloud Storage bucket and outputs its content to the console

from google.api_core.client_options import ClientOptions
from google.cloud import documentai  # type: ignore
from google.cloud import storage

# TODO(developer): Change these variables before running the sample.
project_id = "myprojectid"
location = "us"  # Format is "us" or "eu"
processorid = "projects/XXX/locations/us/processors/X%X%X%"
bucketname = "rto-boms2"
blobname = "example.pdf"


def quickstart(
    project_id: str,
    location: str,
):
    # You must set the `api_endpoint`if you use a location other than "us".
    opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")

    client = documentai.DocumentProcessorServiceClient(client_options=opts)

    # The full resource name of the location, e.g.:
    # `projects/{project_id}/locations/{location}`
    parent = client.common_location_path(project_id, location)

    # trying to read example.pdf from storage
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucketname)
    blob = bucket.blob(blobname)

    # Read the file into memory
    with blob.open("rb") as image:
        image_content = image.read()

    # Load binary data
    raw_document = documentai.RawDocument(
        content=image_content,
        mime_type="application/pdf",  # Refer to https://cloud.google.com/document-ai/docs/file-types for supported file types
    )

    request = documentai.ProcessRequest(name=processorid, raw_document=raw_document)

    result = client.process_document(request=request)

    # For a full list of `Document` object attributes, reference this page:
    # https://cloud.google.com/document-ai/docs/reference/rest/v1/Document
    document = result.document

    # Read the text recognition output from the processor
    print("The document contains the following text:")
    print(document.text)

quickstart(project_id,location)
