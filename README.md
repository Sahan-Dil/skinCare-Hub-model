# skinCare-Hub-model

Deploying fuction on GCP
-- gcloud auth login
-- cd gcp
gcloud functions deploy predict_lite --runtime python38 --trigger-http --memory 512 --project project_id
(  gcloud functions deploy predict --runtime python38 --trigger-http --memory 512 --project skin-care-hub  )