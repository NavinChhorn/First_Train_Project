from db import session
from sqlalchemy import desc,asc

class BaseModel:
    def __init__(self):
        self._session = session
        self.__query = self.get_query()
    
    def _commit(self):
        self._session.commit()

    def get_query(self):
        return self._session.query(self.__class__)
    
    def get_none(self):
        return self.__query.filter(self.__class__.id == id).one__or__none()
    
    def get_all(self):
     return self.__query.order_by(desc("id")).all()
    
    def get_by_id(self, id):
        return self.__query.filter_by(self.__class__.id == id).all()
    
    def update_status(self):
        self.__query.filter(self.__class__.id == self.id).update(
            {
                self.__class__.status: self.status
            }
        )
        self._commit()
    
    def update(self):
        self.__query.filter(self.__class__.id == self.id).update(
            {
                k: v
                for k, v in self.__dict__.items()
                if not k.startswith("_")
                and k not in ["_sa_instance_state", "_session", "_query"]
            }
        )
        self._commit()
    
    def delete(self):
        self._session.query(self.__class__).filter(
            self.__class__.id == self.id
        ).delete()
        self._commit()
    
    def jsonify(self, schema, model, **kwargs):
        # return schema.dump(model, **kwargs)
        return schema(**kwargs).dump(model)