#!/bin/sh
pip freeze > requirements.txt
git add .
git commit -m "update"
git push heroku master
heroku logs -n 20
