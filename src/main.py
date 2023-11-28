import unittest
from tests.test_login import TestHomePage

if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestHomePage)
    unittest.TextTestRunner(verbosity=2).run(test_suite)
    #verbosity controlla l'output durante l'esecuzione del test sulla console.
    #ci sono 3 stati: 0 - 1 e 2. 
    #0: Stampa solo i risultati finali dei test (passati o falliti).
    #1: Stampa una breve descrizione di ciascun test mentre viene eseguito, oltre ai risultati finali.
    #2: Stampa una descrizione più dettagliata di ciascun test mentre viene eseguito, oltre ai risultati finali.
