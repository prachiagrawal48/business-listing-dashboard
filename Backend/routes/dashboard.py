from fastapi import APIRouter
from database import get_connection

router = APIRouter()

# 📊 City-wise count
@router.get("/city-count")
def city_count():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT city, COUNT(*) as count
        FROM listing_master
        GROUP BY city
    """)

    result = cursor.fetchall()
    conn.close()
    return result


# 📊 Category-wise count
@router.get("/category-count")
def category_count():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT category, COUNT(*) as count
        FROM listing_master
        GROUP BY category
    """)

    result = cursor.fetchall()
    conn.close()
    return result


# 📊 Source-wise count
@router.get("/source-count")
def source_count():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT source, COUNT(*) as count
        FROM listing_master
        GROUP BY source
    """)

    result = cursor.fetchall()
    conn.close()
    return result