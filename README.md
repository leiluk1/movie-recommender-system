# Movie Recommender System

*Name*: Leila Khaertdinova

*Email*: l.khaertdinova@innopolis.university

*Group number*: BS21 DS-02 

This project is intended for the second assignment in the Practical Machine Learning and Deep Learning course at Innopolis University.

## Task description

A recommender system is a type of information filtering system that suggests items or content to users based on their interests, preferences, or past behavior. These systems are commonly used in various domains, such as e-commerce, entertainment, social media, and online content platforms.

The objective of this assignment is to create a recommender system of movies for users.

## Dataset Description

The main dataset used is *MovieLens 100K dataset*, consisting user ratings to movies. It is already downloaded from [here](https://grouplens.org/datasets/movielens/100k/), you can find it in `data/raw` folder in the repo.

**Overview about the dataset:**

* It consists of 100,000 ratings from 943 users on 1682 movies;
* Ratings are ranged from 1 to 5;
* Each user has rated at least 20 movies;
* It contains simple demographic info for the users (age, gender, occupation, zip code).

## Getting started

To run this project, run the following commands in the repo root directory:
1. Create the virtual environment
    ```
    python3 -m venv .venv
    source .venv/bin/activate
    ```
2. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Make sure you have a compatible version of Python 3.9.13 before running the code
4. To check the data exploration and analysis, please check the notebook `1.0-initial-data-exploration` in the `notebooks` directory
5. To check the model training process and results, please see the notebook `2.0-final-solution-train-and-eval` in the `notebooks` directory
6. The evaluation function is placed in `benchmark/evaluate.py` script
7. To read the final report, check the `reports`
