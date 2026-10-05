from datetime import datetime, timedelta


def scan_storage():
    now = datetime.now()

    storage_items = [
        {
            "name": "Vacation_2024.mp4",
            "type": "video",
            "size": 8 * 1024 * 1024 * 1024,
            "created_at": now - timedelta(days=400),
            "last_accessed": now - timedelta(days=300),
        },
        {
            "name": "IMG_1023.jpg",
            "type": "photo",
            "size": 8 * 1024 * 1024,
            "created_at": now - timedelta(days=500),
            "last_accessed": now - timedelta(days=200),
        },
        {
            "name": "IMG_1024.jpg",
            "type": "photo",
            "size": 8 * 1024 * 1024,
            "created_at": now - timedelta(days=500),
            "last_accessed": now - timedelta(days=200),
        },
        {
            "name": "Old_Project.pdf",
            "type": "document",
            "size": 25 * 1024 * 1024,
            "created_at": now - timedelta(days=800),
            "last_accessed": now - timedelta(days=700),
        },
        {
            "name": "Screenshot_2024.png",
            "type": "photo",
            "size": 3 * 1024 * 1024,
            "created_at": now - timedelta(days=600),
            "last_accessed": now - timedelta(days=550),
        },
    ]
# sas
    return storage_items