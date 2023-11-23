# Learning Python with CS50
# Cookie Jar
# https://cs50.harvard.edu/python/2022/psets/8/jar/


class Jar:
    def __init__(self, capacity=12):
        # Call the setter for capacity
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        cookies = "🍪" * self.size
        return cookies

    def deposit(self, n):
        if n > (self.capacity - self.size):
            raise ValueError("Deposit amount exceeds jar capacity")
        else:
            self.size = self.size + n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError("Withdraw amount exceeds amount of cookies in the jar")
        else:
            self.size -= n

    # Getter for capacity
    @property
    def capacity(self):
        return self._capacity

    # Setter for capacity
    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Capacity must be a non-negative value")
        self._capacity = value

    # Getter for size
    @property
    def size(self):
        return self._size

    # Setter for size
    @size.setter
    def size(self, value):
        if value < 0:
            raise ValueError("Size must be a non-negative value")
        self._size = value


def main():
    user_input = int(input("What is the capacity of the jar? "))
    cookie_jar = Jar(user_input)
    print(cookie_jar)
    cookie_jar.deposit(int(input("How many cookies do you want to deposit? ")))
    print(cookie_jar)
    cookie_jar.withdraw(int(input("How many cookies do you want to withdraw? ")))
    print(cookie_jar)


if __name__ == "__main__":
    main()
