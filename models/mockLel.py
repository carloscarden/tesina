from models.Lel import Lel
from models.termino import Termino


class MockLel:

    def lelMockeado(self):
        lel1 = Lel(Termino.VERBO,  'Administer', ''' Action performed by a doctor, that consists
in dispensing at a certain date and hour a dose of a drug to deal with some disease
of a patient in some seriousness in order to obtain some outcome.''')
        lel2 = Lel(Termino.OBJETO, 'Dose', ''' Amount of a drug that is taken once, or
regularly over a period of time''')
        lel3 = Lel(Termino.SUJETO, 'Patient', ''' Person who is ill or hurt, characterized by
gender and city.''')
        lel4 = Lel(Termino.OBJETO, 'Drug', ''' Medicine or other substance which has a
physiological effect when ingested or otherwise introduced into the body according to
its administration mode. The drug is also
characterized by an elimination mode''')
        lel5 = Lel(Termino.SUJETO, 'Doctor', '''A person with a medical degree whose job
is to treat patients. The doctor works for a hospital and belongs to a Department''')
        lel6 = Lel(Termino.SUJETO, 'Disease', ''' Illness affecting humans''')
        lel7 = Lel(Termino.OBJETO, 'Outcome', ''' The result of a medical treatment''')
        lel8 = Lel(Termino.OBJETO, 'Hour', ''' One of the 24 parts that a day is divided into''')
        lel9 = Lel(Termino.OBJETO, 'Date', ''' A particular day of a month, in a particular year.
''')
        lel10 = Lel(Termino.OBJETO, 'Seriousness', '''Degree of risk of the life of a patient.''')
        lel11 = Lel(Termino.OBJETO, 'Administration mode', ''''The way of giving a drug to somebody.''')
        lel12 = Lel(Termino.OBJETO, 'Elimination mode', '''The process of removing or getting rid of the
drug completely''')
        lel13 = Lel(Termino.OBJETO, 'Physiological effect', '''The expected result of administering a drug,
it belongs to one family.''')
        lel14 = Lel(Termino.OBJETO, 'Family', '''  A group into which drugs that have similar characteristics are divided based on their
physiological effect''')
        lel15 = Lel(Termino.SUJETO, 'Department', '''A section of a hospital.''')
        lel16 = Lel(Termino.SUJETO, ' Hospital', ''' An institution in which the sick or injured
are given medical and surgical treatment. A hospital is located in a city.''')
        lel17 = Lel(Termino.OBJETO, 'City', ''' A city belongs to a state.''')
        lel18 = Lel(Termino.OBJETO, 'State', ''' A state belongs to a country.''')
        lel19 = Lel(Termino.OBJETO, 'Country', ''' An area of land that has or used to have its
own government and laws.''')
        lel20 = Lel(Termino.OBJETO, 'Month', ''' Any of the twelve periods of time into which
a year is divided.''')
        lel21 = Lel(Termino.OBJETO, 'Year', '''The period from January 1 to December 31.''')
        lel22 = Lel(Termino.OBJETO, 'Género', '''A range of identities with reference to social
and cultural differences.''')
        lels = [lel1, lel2, lel3, lel4, lel5, lel6, lel7, lel8, lel9, lel10, lel11, lel12, lel13, lel14, 
         lel15, lel16, lel17, lel18, lel19, lel20, lel21, lel22]

        return lels
