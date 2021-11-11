#!/bin/sh
pip freeze > requirements.txt
git add .
git commit -m "update"
git push https://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@github.com/KelvinKramp/BookFeedback.git
#git push heroku master
#heroku logs -n 20
