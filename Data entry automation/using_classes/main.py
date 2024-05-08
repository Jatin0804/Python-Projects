from scrapper import Scrapper
from compiler import Compiler

scraper = Scrapper()
compiler = Compiler()

for n in range(len(scraper.addresses - 1)):
    compiler.fill_form(scraper.addresses[n], scraper.prices[n], scraper.links[n])
