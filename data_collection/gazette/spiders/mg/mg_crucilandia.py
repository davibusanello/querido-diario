from datetime import date

from gazette.spiders.base.instar import BaseInstarSpider


class MgCrucilandiaSpider(BaseInstarSpider):
    TERRITORY_ID = "3120607"
    name = "mg_crucilandia"
    base_url = "http://www.prefeituradecrucilandia.mg.gov.br/portal/diario-oficial"
    start_date = date(2015, 3, 31)
