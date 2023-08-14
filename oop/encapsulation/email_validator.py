class Phone:
    def __getattr__(self, attr):
        return None


phone = Phone()
print(phone.color) # None
print(getattr(phone, 'size')) # None
