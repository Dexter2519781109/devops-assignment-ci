\# DevOps CI Assignment



\## Miről szól ez a repom?

Ez a repository a DevOps / CI beadandóhoz készült Ku7iez.



Tartalom:

\- `src/calculator.py`: egy egyszerű Calculator osztály

\- `tests/test\_unit\_calculator.py`: unit tesztek

\- `tests/test\_integration\_calculator.py`: integration tesztek

\- `.github/workflows/pr-tests.yml`: Pull Request esetén futó GitHub Actions workflow (csak unit tesztek)

\- `.github/workflows/main-branch-tests.yml`: master/main branch push esetén futó workflow (unit + integration tesztek)



\## Beadandó követelmények

1\. Saját public GitHub repository.

2\. Egy program/osztály + kétféle teszt (unit és integration).

3\. GitHub Actions:

&nbsp;  - Pull Request esetén csak a unit tesztek fussanak.

&nbsp;  - master/main branchre történő push esetén fusson le a unit + integration.

4\. Legyen legalább:

&nbsp;  - egy Pull Request, ahol látszik a PR-es workflow futása,

&nbsp;  - és egy push a master/main branchre, ahol látszik a teljes tesztfuttatás.



A tesztek eredménye (zöld/piros) nem számít, csak az, hogy a pipeline elinduljon.

# kis módosítás
Ez egy teszt PR módosítás a workflow kipróbálásához.
