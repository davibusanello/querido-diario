import datetime as dt

from gazette.spiders.base.aplus import BaseAplusSpider


class MaSantoAntoniodosLopesSpider(BaseAplusSpider):
    TERRITORY_ID = "2110302"
    name = "ma_santo_antonio_dos_lopes"
    start_date = dt.date(2017, 11, 10)
    BASE_URL = "https://www.stoantoniodoslopes.ma.gov.br/diario/"
