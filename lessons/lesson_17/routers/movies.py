from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from models import Movie
from schemas import MovieRequest, MovieResponse
from services.movies import (
    create_movie_service,
    delete_movie_service,
    update_movie_service,
    list_movies_service,
    get_movie_service
)

router = APIRouter(
    prefix="/movies",
    tags=["movies"]
)
@router.get("/", response_model=list[MovieResponse])
async def get_movies(db: AsyncSession = Depends(get_db)) -> list[Movie]:
    return await list_movies_service(db)

@router.post("/", response_model=MovieResponse)
async def add_movie(movie: MovieRequest, db:AsyncSession = Depends(get_db)) -> Movie:
    return await create_movie_service(movie, db)

@router.get("/{movie_id}", response_model=MovieResponse)
async def get_movie(movie_id: str, db:AsyncSession = Depends(get_db)) -> Movie:
    return await get_movie_service(movie_id, db)


@router.put("/{movie_id}", response_model=MovieResponse)
async def update_movie(
    movie_id:str,
    movie_update: MovieRequest,
    db:AsyncSession = Depends(get_db)
) -> Movie:
    return await update_movie_service(movie_id, movie_update, db)

@router.delete("/{movie_id}", response_model=MovieResponse)
async def delete_movie(movie_id:str, db:AsyncSession = Depends(get_db)) -> Movie:
    return await delete_movie_service(movie_id, db)