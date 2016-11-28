# Popularity Ranking

## Introduction

One of our goals is to show buyers products they want to order. An important part of this is having good rankings/ relevancy in our search results.

One type of ranking we use is "most popular". The definition of "popular" and the implementation of the ranking is what we'll be looking at in this assignment.

## Data model

We have a very basic data model with:

- `Seller` - a seller of items in our system
- `Item` - an item which is sold by a `Seller`
- `ItemView` - a record of when an item has been viewed
- `WishList` - a list that people can add items to
- `WishListEntry` - links an `Item` to a given `WishList`

## The webapp

The current webapp has no ranking implemented (it just lists all the items alphabetically). 

It uses Django Rest Framework to provide a JSON endpoing and the front-end uses AngularJS. 

For this task you shouldn't need to worry about the Javascript side of things but you can have a look if you're interested.
 
## The task

The task is to implement a very basic "most popular" ranking:

```
item_popularity_score = total_item_views + (2 * total_wish_list_entries)
```

This means:

- modify `ranker.data.item_ranker.rank_all_items` to do the ranking
- add some simple tests

## Time

Please don't spend more than 30 to 45 minutes on this, we just want you to be familiar with the problem and get the project set up. 
   
# Set-up

This is a really standard Django app using a SQLite database. That means the set-up should be:

```
pip install -r requirements.txt
python manage.py migrate
python manage.py populate
```

## Client-side

You shouldn't need to touch the client side, however, to set things up you need to run:

```
cd ranker/client
npm install 
grunt default
```