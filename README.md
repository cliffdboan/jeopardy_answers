# This is a Jeopardy! "question" data scraper.

## Introduction
The purpose of this scraper is to scrape the J! Archive website for all J!
categories and answers using selenium. The data will then be sorted and presented
beautifully using Pandas.

## Why?
Well the most recent data dump I've been able to find is from 2015, leaving
nearly 10 years of J! clues unaccounted for in claims of most common this-or-that.
I want to be able to find out the most up-to-date info whenever I run the script,
just by updating the database rather than scraping the entire archives again.

## Process
Scrape the J! Archive website (www.j-archive.com) using Selenium to grab all answer data from each season.

1. Write a selenium script to get the initial data from the time of the script being written (as in, all
data from prior to the current season (40)). Clean up the answers that may have some inflection on them, removing 'a's, 'the's,
quotation marks, and any HTML tags that the site may have added for flair.
Finally, save to a CSV.

2.

X. Write another script to get all data that is new. That means, if J! is wrapping up season 42, and you have not
run this scraper since season 41, running this scraper will only collect the new games
rather than _all_ of the games again.

## ETL Overview
CSV with cleaned up data -> S3 -> RDS -> some kind of visualization of the data

## How to use this thing
