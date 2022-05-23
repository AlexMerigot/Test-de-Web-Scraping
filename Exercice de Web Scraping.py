# -*- coding: utf-8 -*-
"""
Created on Mon May 23 09:06:49 2022

@author: Alexandre Mérigot
"""

import requests
from bs4 import BeautifulSoup

## Je choisis la page web que je veux Scraper
URL = "https://fr.indeed.com/jobs?q=d%C3%A9veloppeur%20alternance&l=Toulouse%20(31)&vjk=085bf7950287509b"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

## Je retrouve l'ID qui contient la liste d'offre d'alternance
results = soup.find(id="mosaic-provider-jobcards") 

## J'isole les titres de missions
job_title = results.find_all("h2", class_="jobTitle")

for job in job_title:
    print(job.get_text(separator=" "), end="\n"*2)  ## separator et le "end=" pour etre plus lisibles
    
## J'isole les sociétés
companies = results.find_all("span", class_="companyName")

for company in companies :
    print(company.get_text(separator=" "), end="\n"*2)

## J'isole les lieux de travail 
locations = results.find_all("div", class_="companyLocation")

for location in locations :
    print(location.get_text(separator=" "), end="\n"*2)

## problèmatique : J'ai la liste des missions, celle des sociétés, celle des lieux mais ils sont chacun les un après les autres, moi je souhaites les rassembler.

## 1) Je ne peux pas faire de "list" car je me retrouve avec l'intégralité du contenu HTML ...
## 2) Comment extraire les éléments "text" sans me retrouver avec l'ensemble du code HTML.
