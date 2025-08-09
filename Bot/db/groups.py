# Bot/db/groups.py

from Bot.db import SESSION, BASE
from sqlalchemy import Column, Integer, UnicodeText, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from Bot.mongo import db  

GROUPS_COLLECTION = db["groups"]


async def save_group_for_drop(group_id: int, title: str = None):
    """
    Save or update group in MongoDB so the bot knows
    which groups are active for waifu drops.
    """
    await GROUPS_COLLECTION.update_one(
        {"group_id": group_id},
        {
            "$set": {
                "group_id": group_id,
                "title": title or "Unknown Group",
            }
        },
        upsert=True
    )


async def get_all_groups() -> list:
    """Return a list of all saved groups."""
    return await GROUPS_COLLECTION.find().to_list(length=None)


async def remove_group(group_id: int):
    """Remove a group from the database."""
    await GROUPS_COLLECTION.delete_one({"group_id": group_id})


async def is_group_registered(group_id: int) -> bool:
    """Check if a group is already saved."""
    return await GROUPS_COLLECTION.find_one({"group_id": group_id}) is not None