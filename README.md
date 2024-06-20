# This is a Jeopardy! "question" data scraper.

## Introduction
The purpose of this scraper is to scrape the J! Archive website for all J!
categories and answers using selenium. The data will then be sorted and presented
beautifully using Pandas.

## Why?
Well the most recent data dump I've been able to find is from 2015, leaving
nearly 10 years of J! clues unaccounted for in claims of most common this-or-that.
There are two parts to this scraper. Part one is getting all information prior
to this script being written. Part two is a scraper that gathers all information
that has not been collected. So if J! is wrapping up season 42, and you have not
run this scraper since season 41, running the scraper will only collect the new games
rather than _all_ of the games again.

## ETL Overview
CSV with cleaned up data -> S3 -> RDS -> some kind of visualization of the data
