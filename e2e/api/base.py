class Base(object):
    BASE_URL = None  # Set in conftest#test_data

    @classmethod
    def make_request(cls):
        return "success"
