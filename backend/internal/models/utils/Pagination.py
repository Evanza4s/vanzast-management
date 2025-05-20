from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Query
from fastapi import HTTPException, status

def paginate_query(
    query: Query,
    page: int = 1,
    per_page: int = 10,
) -> Dict[str, Union[int, list, Any]]:

    if page < 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Page must be greater than 0"
        )
    if per_page < 1:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Per page must be greater than 0"
        )

    total_items = query.count()
    total_pages = (total_items + per_page - 1) // per_page

    if page > total_pages and total_items > 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Page not found"
        )

    items = query.offset((page - 1) * per_page).limit(per_page).all()

    return {
        "page": page,
        "per_page": per_page,
        "total_items": total_items,
        "total_pages": total_pages,
        "items": items,
        "has_next": page < total_pages,
        "has_previous": page > 1,
    }