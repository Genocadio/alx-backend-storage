#!/usr/bin/env python3
"""List all documents in collection"""


def list_all(mongo_collection):
    """List all documents in a collection"""
    return mongo_collection.find()
