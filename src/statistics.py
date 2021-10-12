class Statistics:
    def __init__(self):
        self.count = 0
        self.stats_sum = 0

    def add_number(self, number):
        self.stats_sum += number
        self.count +=1

    def get_count(self):
        return self.count

    def sum(self):
        return self.stats_sum

    def average(self):
        return (self.stats_sum / self.count)