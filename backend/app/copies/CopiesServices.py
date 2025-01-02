from psycopg import Copy

import Copies
class CopiesService:
    def __init__(self, db_session):
        self.db_session = db_session

    def create_copy(self, data):
        new_copy = Copies(**data)
        self.db_session.add(new_copy)
        self.db_session.commit()
        return new_copy

    def get_copy(self, copy_id):
        return self.db_session.query(Copies).filter(Copies.id == copy_id).first()

    def get_all_copies(self):
        return self.db_session.query(Copies).all()

    def update_copy(self, copy_id, data):
        copy_entry = self.db_session.query(Copy).filter(Copy.id == copy_id).first()
        if copy_entry:
            for key, value in data.items():
                setattr(copy_entry, key, value)
            self.db_session.commit()
            return copy_entry
        return None

    def delete_copy(self, copy_id):
        copy_entry = self.db_session.query(Copy).filter(Copy.id == copy_id).first()
        if copy_entry:
            self.db_session.delete(copy_entry)
            self.db_session.commit()
            return True
        return False
