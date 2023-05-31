from aiohttp import ClientSession
import asyncio
import datetime
from more_itertools import chunked
from model import People, engine, Session, Base

from config import DB_URL

MAX_SIZE = 10


async def paste_to_db(people_list):
    async with Session() as session:
        people_list = [People(
            name=item.get('name'),
            birth_year=item.get('birth_year'),
            eye_color=item.get('eye_color'),
            films=item.get('films'),
            gender=item.get('gender'),
            hair_color=item.get('hair_color'),
            height=item.get('height'),
            homeworld=item.get('homeworld'),
            mass=item.get('mass'),
            skin_color=item.get('skin_color'),
            species=item.get('species'),
            starships=item.get('starships'),
            vehicles=item.get('vehicles'),
        ) for item in people_list]
        session.add_all(people_list)
        await session.commit()
        return people_list


async def get_film(url: str, client: ClientSession):
    async with client.get(url) as response:
        json_data = await response.json()
        film = json_data.get('title')
        return film


async def get_species(url: str, client: ClientSession):
    async with client.get(url) as response:
        json_data = await response.json()
        species = json_data.get('name')
        return species


async def get_starships(url: str, client: ClientSession):
    async with client.get(url) as response:
        json_data = await response.json()
        starships = json_data.get('name')
        return starships


async def get_vehicles(url: str, client: ClientSession):
    async with client.get(url) as response:
        json_data = await response.json()
        vehicles = json_data.get('name')
        return vehicles


async def get_people(people_id: int, client: ClientSession):
    url = f'{DB_URL}/people/{people_id}'
    async with client.get(url) as response:
        json_data = await response.json()

        if json_data.get('name'):
            url_films = json_data.get('films')
            coros_f = [get_film(url, client) for url in url_films]
            film_list = await asyncio.gather(*coros_f)

            url_species = json_data.get('species')
            coros_s = [get_species(url, client) for url in url_species]
            species_list = await asyncio.gather(*coros_s)

            url_vehicles = json_data.get('vehicles')
            coros_v = [get_vehicles(url, client) for url in url_vehicles]
            vehicles_list = await asyncio.gather(*coros_v)

            url_starships = json_data.get('starships')
            coros_st = [get_starships(url, client) for url in url_starships]
            starships_list = await asyncio.gather(*coros_st)

            json_data['films'] = ", ".join(film_list)
            json_data['species'] = ", ".join(species_list)
            json_data['vehicles'] = ", ".join(vehicles_list)
            json_data['starships'] = ", ".join(starships_list)

        print(json_data)
        return json_data


async def main():
    tasks = []
    async with ClientSession() as session:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
        for id_chunk in chunked(range(1, 100), MAX_SIZE):
            coros = [get_people(people_id=id, client=session) for id in id_chunk]
            people_list = await asyncio.gather(*coros)
            db_coro = paste_to_db(people_list)  # создаем карутину
            paste_to_db_task = asyncio.create_task(db_coro)  # создаем таску
            tasks.append(paste_to_db_task)  # добавляем таску в список таск
            print()
    tasks = asyncio.all_tasks() - {asyncio.current_task()}
    [await task for task in tasks]


start = datetime.datetime.now()
asyncio.run(main())
print(datetime.datetime.now() - start)
