#!/usr/bin/env python3
'''a Python function that changes all topics of a school document by their name
'''


def update_topics(mongo_collection, name, topics):
    '''Changes all topics of a collection's document based on the name.
    '''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
