class Counter:
    count = 0
    @classmethod
    def increment(cls):
        cls.count += 1
        print(cls.count)

Counter.increment()
Counter.increment()
Counter.increment()
Counter.increment()