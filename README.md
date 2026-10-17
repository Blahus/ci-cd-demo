# CI/CD Demo

[![Python CI](https://github.com/Blahus/ci-cd-demo/actions/workflows/ci.yml/badge.svg)](https://github.com/Blahus/ci-cd-demo/actions/workflows/ci.yml)

Tämä on pieni GitHub Actions -harjoitus, jossa kokeilin miten Python-projektin tarkistuksia voidaan automatisoida.

Projektissa on yksinkertainen Python-ohjelma, muutama testi ja GitHub Actions -workflow.

## Mitä workflow tekee?

Kun main-haaraan tehdään push tai pull request, GitHub Actions suorittaa automaattisesti:

- riippuvuuksien asennuksen
- Ruff-linttauksen
- pytest-testit
- ZIP-artifactin luonnin

Jos joku vaihe epäonnistuu, workflow pysähtyy siihen.

## Projektin ajo omalla koneella

Asenna ensin riippuvuudet:

python3 -m pip install -r requirements.txt

Linttaus:

ruff check .

Testit:

pytest -q

## Testit

Projektissa on neljä testiä.

Yksi testeistä tarkistaa myös raja-arvoja classify_score-funktiossa.

## GitHub Actions

Workflow löytyy täältä:

.github/workflows/ci.yml

Se käynnistyy automaattisesti, kun:

- main-haaraan tehdään push
- main-haaraan tehdään pull request

## Epäonnistuneen ajon testaus

Testasin workflow'ta myös tekemällä yhden testin tarkoituksella väärin.

Keskiarvon oikea tulos oli 20.0, mutta testissä odotettiin arvoa 99.

GitHub Actions huomasi virheen ja Run unit tests -vaihe epäonnistui.

Tämän jälkeen testi korjattiin takaisin oikeaksi ja seuraava workflow-ajo onnistui.

## Turvallisuus

Workflow käyttää vain repositoryn lukemiseen tarvittavaa contents: read -oikeutta.

Repositoryyn ei tallenneta salasanoja, API-avaimia tai muita salaisia tietoja.

## Kustannukset

Tässä harjoituksessa workflow-ajot ovat hyvin lyhyitä, joten resurssien käyttö on vähäistä.

Isommassa projektissa turhia ajoja voisi vähentää esimerkiksi rajaamalla workflow'n käynnistymistä vain tiettyihin brancheihin tai tiedostomuutoksiin.

Harjoituksessa testattiin myös pull request -triggerin toiminta.
