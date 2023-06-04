# Diagnese API
Welcome to our Diagnese API

## What you need
1. Cloud Environment: Google Cloud Platform (Cloud Run & IAM Service Account)
2. Programming Language: Python
3. Web Server: Flask API (Restx)
4. Serverless: Cloud Run

# How to setup Locally
1. Clone repository following this command
    ```
    git clone https://github.com/arik147/diagnese-api-flask.git
    ```
2. Install python3 (>3.9 or latest)
3. Install pip (>18.1 or latest)
4. Install requirements.txt
    ```
    pip install -r requirements.txt
    ```
6. Run app
    ```
    python main.py
    ```
    or
    ```
    flask run
    ```
8. Test the API using `Postman` with `POST` Method, route `/predict` and request body JSON : 
    ```
    {
        "muntah": 1,
        "sakit_kepala": 1,
        "mual": 1,
        "kaku_saat_ingin_bergerak": 1,
        "sensasi_berputar": 1,
        "kehilangan_keseimbangan": 1
    }
    ```
    
# How to setup with Google Cloud Platform using Cloud Run
1. Open cloud shell and set the project id
    ```
    gcloud config set project PROJECT_ID
    ```
2. Clone repository following this command
    ```
    git clone https://github.com/arik147/diagnese-api-flask.git
    ```
3. Open the app folder  
    ```
    cd diagnese-api-flask/
    ```
4. Build and submit a Docker image to Google Cloud Build
    ```
    gcloud builds submit --tag gcr.io/PROJECT_ID/diagnese-api-flask
    ```
5. Deploy a container image to Google Cloud Run
    ```
    gcloud run deploy --image gcr.io/PROJECT_ID/diagnese-api-flask
    ```
