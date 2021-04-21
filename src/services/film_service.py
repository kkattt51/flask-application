from src.database.models import Film


class FilmService:
    @staticmethod
    def fetch_all_films(session):
        return session.query(Film)

    @classmethod
    def fetch_film_by_uuid(cls, session, uuid):
        return cls.fetch_all_films(session).filter_by(
            uuid=uuid
        ).first()

    @staticmethod
    def bulk_create_films(session, films):
        films_to_create = [
            Film(**film)
            for film in films
        ]
        session.bulk_save_objects(films_to_create)
        session.commit()
        return len(films_to_create)
