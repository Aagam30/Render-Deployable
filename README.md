# Election Predictor

A simple Flask-based web app that predicts election outcomes using a trained machine‑learning model.

## Local Development

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
export FLASK_APP=app.py
flask run
```

## Deploying to Render

1. Push this repository to GitHub.
2. Log in to [Render](https://render.com) and create a new **Web Service** connected to your repo.
3. Render will detect the `render.yaml` file and pre‑fill build & start commands.
4. Click **Create Web Service** and wait for the deploy to finish.

That's it—your app will be live on a Render URL.

## File Overview

| File/Dir        | Purpose                                   |
|-----------------|-------------------------------------------|
| `app.py`        | Flask application entry‑point             |
| `election_model.pkl` | Serialized trained model              |
| `scaler.pkl`    | `StandardScaler` fitted on training data  |
| `templates/`    | HTML templates for the UI                 |
| `requirements.txt` | Python dependencies                    |
| `Procfile`      | Start command for production (Gunicorn)   |
| `render.yaml`   | Render service configuration              |
