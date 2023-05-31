async def paste_to_db_hero(people_list):
    async with Session() as session:
        people_orm = []
        for people in people_list:
            name = people.get('name')
            birth_year = people.get('birth_year')
            eye_color = people.get('eye_color')
            # film = await get_films(people.get('films'))
            # films = people.get('films')
            # gender = people.get('gender')
            # hair_color = people.get('hair_color')
            # height = people.get('height')
            # homeworld = people.get('homeworld')
            # mass = people.get('mass')
            # skin_color = people.get('skin_color')
            # species = people.get('species')
            # starships = people.get('starships')
            # vehicles = people.get('vehicles')
            People(name=name, birth_year=birth_year, eye_color=eye_color)
            await people_orm.append(People)

        session.add_all(people_orm)
        await session.commit()
        print(people_orm)