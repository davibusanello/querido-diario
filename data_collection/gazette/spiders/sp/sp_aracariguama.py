from datetime import date

from gazette.spiders.base.instar import BaseInstarSpider


class SpAracariguamaSpider(BaseInstarSpider):
    TERRITORY_ID = "3502754"
    name = "sp_aracariguama"
    base_url = "https://www.aracariguama.sp.gov.br/portal/diario-oficial"
    start_date = date(2019, 9, 6)
