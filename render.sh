#!/usr/bin/env bash
pip install --upgrade pip
pip install -r requirements.txt --timeout 300 --retries 5
pip install gunicorn
python -c "from mercado import app, db; app.app_context().push(); db.create_all()"