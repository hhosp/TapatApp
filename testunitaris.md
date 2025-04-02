# Què són els tests unitaris?

Els tests unitaris són una tècnica de verificació de programari que permet provar de manera independent les unitats més petites del codi, com ara funcions o mètodes. L'objectiu és assegurar que cada unitat funcioni correctament de manera aïllada abans d'integrar-la amb altres components del sistema.

# Llibreries de test amb Python

Python ofereix diverses llibreries per a realitzar tests unitaris, com ara:
- `unittest`: Llibreria estàndard integrada a Python.
- `pytest`: Llibreria avançada amb sintaxi simplificada.
- `nose2`: Successor de `nose`, amb suport per a plugins.
- `doctest`: Permet escriure tests dins de la documentació.

## Com funciona `unittest`?

`unittest` és una llibreria integrada que segueix el model xUnit. Per utilitzar-la:
1. Importa `unittest`.
2. Crea una classe que hereti de `unittest.TestCase`.
3. Defineix mètodes que comencin amb `test_` per escriure els tests.
4. Utilitza assertions com `assertEqual`, `assertTrue`, etc.
5. Executa els tests amb `unittest.main()`.

## Assertions més importants en `unittest` i la seva utilitat

1. **`assertEqual(a, b)`**  
   Comprova que `a` i `b` són iguals.  
   *Exemple*: Verificar que el resultat d'una funció és el valor esperat.

2. **`assertNotEqual(a, b)`**  
   Comprova que `a` i `b` no són iguals.  
   *Exemple*: Assegurar-se que una funció no retorna un valor incorrecte.

3. **`assertTrue(x)`**  
   Comprova que `x` és cert (`True`).  
   *Exemple*: Verificar que una condició o resultat és cert.

4. **`assertFalse(x)`**  
   Comprova que `x` és fals (`False`).  
   *Exemple*: Assegurar-se que una condició no es compleix.

5. **`assertIs(a, b)`**  
   Comprova que `a` i `b` són el mateix objecte (comparació per identitat).  
   *Exemple*: Verificar que dues variables apunten al mateix objecte.

6. **`assertIsNot(a, b)`**  
   Comprova que `a` i `b` no són el mateix objecte.  
   *Exemple*: Assegurar-se que dues variables no comparteixen la mateixa referència.

7. **`assertIsNone(x)`**  
   Comprova que `x` és `None`.  
   *Exemple*: Verificar que una funció retorna `None` en un cas específic.

8. **`assertIsNotNone(x)`**  
   Comprova que `x` no és `None`.  
   *Exemple*: Assegurar-se que una funció retorna un valor vàlid.

9. **`assertIn(a, b)`**  
   Comprova que l'element `a` està dins de la col·lecció `b`.  
   *Exemple*: Verificar que un element es troba en una llista o diccionari.

10. **`assertNotIn(a, b)`**  
    Comprova que l'element `a` no està dins de la col·lecció `b`.  
    *Exemple*: Assegurar-se que un element no forma part d'una col·lecció.

11. **`assertRaises(exception, callable, *args, **kwargs)`**  
    Comprova que es llança una excepció específica quan es crida una funció amb els arguments donats.  
    *Exemple*: Verificar que una divisió per zero llança una excepció.

12. **`assertAlmostEqual(a, b, places=7)`**  
    Comprova que `a` i `b` són gairebé iguals fins a un nombre determinat de decimals.  
    *Exemple*: Verificar resultats de càlculs amb números en coma flotant.

13. **`assertNotAlmostEqual(a, b, places=7)`**  
    Comprova que `a` i `b` no són gairebé iguals fins a un nombre determinat de decimals.  
    *Exemple*: Assegurar-se que dos valors flotants no són gairebé iguals.

14. **`assertGreater(a, b)`**  
    Comprova que `a` és més gran que `b`.  
    *Exemple*: Verificar que un valor supera un llindar.

15. **`assertLess(a, b)`**  
    Comprova que `a` és més petit que `b`.  
    *Exemple*: Assegurar-se que un valor està per sota d'un límit.

16. **`assertGreaterEqual(a, b)`**  
    Comprova que `a` és més gran o igual que `b`.  
    *Exemple*: Verificar que un valor compleix un mínim.

17. **`assertLessEqual(a, b)`**  
    Comprova que `a` és més petit o igual que `b`.  
    *Exemple*: Assegurar-se que un valor no supera un màxim.