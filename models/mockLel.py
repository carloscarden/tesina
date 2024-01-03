from models.Lel import Lel
from models.Categoria import Categoria


class MockLel:

    def lelMockeado(self):
        lel1 = Lel(Categoria.VERBO,  'Administer', ''' Action performed by a doctor, that consists
in dispensing at a certain date and hour a dose of a drug to deal with some disease
of a patient in some seriousness in order to obtain some outcome.''')
        lel2 = Lel(Categoria.OBJETO, 'Dose', ''' Amount of a drug that is taken once, or
regularly over a period of time''')
        lel3 = Lel(Categoria.SUJETO, 'Patient', ''' Person who is ill or hurt, characterized by
gender and city.''')
        lel4 = Lel(Categoria.OBJETO, 'Drug', ''' Medicine or other substance which has a
physiological effect when ingested or otherwise introduced into the body according to
its administration mode. The drug is also
characterized by an elimination mode''')
        lel5 = Lel(Categoria.SUJETO, 'Doctor', '''A person with a medical degree whose job
is to treat patients. The doctor works for a hospital and belongs to a Department''')
        lel6 = Lel(Categoria.SUJETO, 'Disease', ''' Illness affecting humans''')
        lel7 = Lel(Categoria.OBJETO, 'Outcome', ''' The result of a medical treatment''')
        lel8 = Lel(Categoria.OBJETO, 'Hour', ''' One of the 24 parts that a day is divided into''')
        lel9 = Lel(Categoria.OBJETO, 'Date', ''' A particular day of a month, in a particular year.
''')
        lel10 = Lel(Categoria.OBJETO, 'Seriousness', '''Degree of risk of the life of a patient.''')
        lel11 = Lel(Categoria.OBJETO, 'Administration mode', ''''The way of giving a drug to somebody.''')
        lel12 = Lel(Categoria.OBJETO, 'Elimination mode', '''The process of removing or getting rid of the
drug completely''')
        lel13 = Lel(Categoria.OBJETO, 'Physiological effect', '''The expected result of administering a drug,
it belongs to one family.''')
        lel14 = Lel(Categoria.OBJETO, 'Family', '''  A group into which drugs that have similar characteristics are divided based on their
physiological effect''')
        lel15 = Lel(Categoria.SUJETO, 'Department', '''A section of a hospital.''')
        lel16 = Lel(Categoria.SUJETO, ' Hospital', ''' An institution in which the sick or injured
are given medical and surgical treatment. A hospital is located in a city.''')
        lel17 = Lel(Categoria.OBJETO, 'City', ''' A city belongs to a state.''')
        lel18 = Lel(Categoria.OBJETO, 'State', ''' A state belongs to a country.''')
        lel19 = Lel(Categoria.OBJETO, 'Country', ''' An area of land that has or used to have its
own government and laws.''')
        lel20 = Lel(Categoria.OBJETO, 'Month', ''' Any of the twelve periods of time into which
a year is divided.''')
        lel21 = Lel(Categoria.OBJETO, 'Year', '''The period from January 1 to December 31.''')
        lel22 = Lel(Categoria.OBJETO, 'Género', '''A range of identities with reference to social
and cultural differences.''')
        lels = [lel1, lel2, lel3, lel4, lel5, lel6, lel7, lel8, lel9, lel10, lel11, lel12, lel13, lel14, 
         lel15, lel16, lel17, lel18, lel19, lel20, lel21, lel22]

        return lels
