#!/bin/sh
git add .
git commit -m "update"
git push heroku master
heroku logs -n 20
