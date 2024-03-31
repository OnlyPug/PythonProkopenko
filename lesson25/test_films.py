

def test_creator_films(films_pack, films):
    list_of_films = films.filter_only_films(films_pack)
    assert list_of_films.status_code == 200
    print(list_of_films.json())

