class student:
    marks_bonus=2
    some_thing=" "
    def __init__(self,first,last,marks):
        self.first=first
        self.last=last
        self.marks=marks

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    @property
    def apply_bonus(self):
        self.marks=int(self.marks*self.marks_bonus)
    def something(self):
        self.some_thing=self.first+self.last