class App:
    def __init__(self, user: int, storage: int, username: str) -> None:
        self.user: int = user
        self.storage: int = storage
        self.username: str = username
        
    def login(self) -> None:
        if self.username == 'owner':
            print(f'Hello to : {self.username}')
            print(f'the storage is : {self.storage}')
        else:
            print('access denied')
    
    def increase_capacity(self, add_storage: int) -> None:
        print(f'added storage is: {self.storage + add_storage}')
        
if __name__ == '__main__':
    user = App(35, 256, 'owner')
    user.login()
    user.increase_capacity(502)
    
    user_two = App(22, 128, "joo")
    user_two.login()