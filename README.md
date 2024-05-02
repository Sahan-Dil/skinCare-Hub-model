# SkinCare Hub Model Deployment on GCP

This repository contains code for deploying the SkinCare Hub model on Google Cloud Platform (GCP). The deployed function allows for predictions using the model via HTTP requests.

## Getting Started

To deploy the model on GCP, follow these steps:

1. **Authentication**: 
   gcloud auth login

2. **Navigate to Deployment Directory**:
   cd gcp

3. **Deploy Function**:
   gcloud functions deploy predict_lite --runtime python38 --trigger-http --memory 512 --project project_id

   Note: Replace 'project_id' with your GCP project ID.

## Additional Repositories

For related repositories, check out:

- **Backend Repository**: [SkinCare Hub Backend](https://github.com/Sahan-Dil/skinCare-hub-backend)
- **Frontend Repository**: [SkinCare Hub Frontend](https://github.com/Sahan-Dil/SkinCare-Hub)

## Usage

Once the function is deployed, you can make HTTP requests to it to get predictions from the SkinCare Hub model.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.
