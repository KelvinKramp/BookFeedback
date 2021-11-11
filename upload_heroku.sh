#!/bin/sh
pip freeze > requirements.txt
git add .
git commit -m "update"
git push heroku master
git push https://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@github.com/KelvinKramp/BookFeedback.git
heroku logs -n 20
