from pickledb import PickleDB


class TestDB(object):
    def __init__(self, db=PickleDB):
        self.db = PickleDB("test.db", False, False)

    def add(self, item, ttl="module"):
        try:
            self.db.dadd(item.__class__.__name__, (item.name, item))
        except KeyError:
            self.db.dcreate(item.__class__.__name__)
            self.db.dadd(item.__class__.__name__, (item.name, item))

    def get(self, item_type, name):
        return self.db.dget(item_type.__name__, name)

    def find(self, name):
        for item_type in self.db.getall():
            if self.db.dexists(item_type, name):
                return self.db.dget(item_type, name)
