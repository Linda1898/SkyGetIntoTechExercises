from Ex16Person import Person

class Employee(Person):

    def __init__(self,first_name, surname, national_insurance_number, tax_code, speaks_english):
        Person.__init__(self, first_name, surname)
        self.national_insurance_number = national_insurance_number
        self.tax_code = tax_code
        self.speaks_english = speaks_english

    def _eligibility(self):
        print(f"Name: {self.first_name} {self.surname}")
        print(f'National Insurance number: {self.national_insurance_number}')
        print(f'Tax code: {self.tax_code}')
        print(f'English speaker: {self.speaks_english}')

    def at_work(self):
        super().eat()
        print("I eat from the canteen at lunch")
        super().drink()
        print("I drink the free coffee in the office")
        super().sleep()
        print("I don't nap at work")
        super().social()
        print('I like my colleagues at work and go for after')





