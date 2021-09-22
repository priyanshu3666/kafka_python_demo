from faker import Faker
fake  = Faker()

def get_registered_user():
    return {
        'name' :fake.name(),
        'adddress' : fake.address(),
        'year':fake.year()
    }
    
def get_movielist():
    return {
        "movie_name" : fake.name(),
        "movie" : fake.url()
    }
    
if __name__ == '__main__':
    print(get_movielist())
