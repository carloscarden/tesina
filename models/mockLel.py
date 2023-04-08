from Lel import Lel
from termino import Termino


class MockLel:

    def lelMockeado(self):
        lel1 = Lel(Termino.VERBO,  'Administrar', ''' Acción realizada por un médico,
         que consiste en dispensar en una fecha y hora determinada una dosis de una droga para tratar unos
         enfermedad de un paciente con cierta gravedad para obtener algún resultado.''')
        lel2 = Lel(Termino.OBJETO, 'Dosis', ''' Cantidad de un medicamento que se toma una vez, o
regularmente durante un período de tiempo.''')
        lel3 = Lel(Termino.SUJETO, 'Paciente', '''Persona que está enferma o herida, caracterizada por
género y ciudad.''')
        lel4 = Lel(Termino.OBJETO, ' Droga', ''' Medicamento u otra sustancia que tiene un
efecto fisiológico cuando se ingiere o se introduce de otro modo en el cuerpo de acuerdo con
su modo de administración. La droga también
caracterizado por un modo de eliminación.''')
        lel5 = Lel(Termino.SUJETO, 'Doctor', '''Una persona con un título médico cuyo trabajo
es tratar a los pacientes. El médico trabaja para un hospital y pertenece a un Departamento.''')
        lel6 = Lel(Termino.SUJETO, 'Enfermedad', '''
        Alteración leve o grave del funcionamiento normal que afecta a las personas.''')
        lel7 = Lel(Termino.OBJETO, 'Conclusión', ''' El resultado del tratamiento médico''')
        lel8 = Lel(Termino.OBJETO, 'Hora', ''' Una de las 24 partes que un día es dividido.''')
        lel9 = Lel(Termino.OBJETO, 'Día', ''' A particular day of a month, in a particular
year.
''')
        lel10 = Lel(Termino.OBJETO, 'Seriedad', ''' Grado de riesgo de vida de un paciente''')
        lel11 = Lel(Termino.OBJETO, 'Modo de administración', ''''La manera de darle la droga a alguien''')
        lel12 = Lel(Termino.OBJETO, 'Elimination', '''The process of removing or getting rid of the
drug completely''')
        lel13 = Lel(Termino.OBJETO, 'Efecto fisiológico', '''El resultado esperado de administrar la droga
        a drug, it belongs to one family.''')
        lel14 = Lel(Termino.OBJETO, 'Familia', ''' Grupo en el que se dividen los medicamentos que tienen características similares en función de su
efecto fisiológico''')
        lel15 = Lel(Termino.SUJETO, 'Departamento', '''Sección de un hospital''')
        lel16 = Lel(Termino.SUJETO, ' Hospital', ''' An institution in which the sick or injured
are given medical and surgical treatment. A
hospital is located in a city.''')
        lel17 = Lel(Termino.OBJETO, 'Ciudad', ''' A city belongs to a state.''')
        lel18 = Lel(Termino.OBJETO, 'Estado', ''' A state belongs to a country.''')
        lel19 = Lel(Termino.OBJETO, 'País', ''' An area of land that has or used to have its
own government and laws.''')
        lel20 = Lel(Termino.OBJETO, 'Mes', ''' Any of the twelve periods of time into which
a year is divided.''')
        lel21 = Lel(Termino.OBJETO, 'Año', '''The period from January 1 to December 31.''')
        lel22 = Lel(Termino.OBJETO, 'Género', '''A range of identities with reference to social
and cultural differences.''')
        lels = [lel1, lel2, lel3, lel4, lel5, lel6, lel7, lel8, lel9, lel10, lel11, lel12, lel13, lel14, 
         lel15, lel16, lel17, lel18, lel19, lel20, lel21, lel22]

        return lels
