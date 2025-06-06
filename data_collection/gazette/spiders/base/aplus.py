import datetime as dt
import re
from urllib.parse import urlparse

from scrapy import FormRequest
from scrapy.exceptions import NotConfigured

from gazette.items import Gazette
from gazette.spiders.base import BaseGazetteSpider


class BaseAplusSpider(BaseGazetteSpider):
    def __init__(self, *args, **kwargs):
        if not hasattr(self, "BASE_URL"):
            raise NotConfigured("Please set a value for `BASE_URL`")

        self.allowed_domains = [urlparse(self.BASE_URL).netloc]

        super(BaseAplusSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        start_date = self.start_date.strftime("%Y/%m/%d")
        end_date = self.end_date.strftime("%Y/%m/%d")
        yield FormRequest(
            url=self.BASE_URL,
            formdata={"data": start_date, "data2": end_date, "termo": "", "submit": ""},
        )

    def parse(self, response):
        gazettes = response.xpath(
            "//tbody/tr[not(contains(./td/text(), 'Nenhum registro encontrado'))]"
        )
        for gazette in gazettes:
            gazette_date = dt.datetime.strptime(
                gazette.xpath("./td[2]/text()").get(), "%d/%m/%Y"
            ).date()
            gazette_url = gazette.css("td a::attr(href)").get()
            edition_number = self._get_edition_number(gazette)

            is_extra_edition = re.search(r"-\d+$", edition_number) is not None

            yield Gazette(
                date=gazette_date,
                edition_number=edition_number,
                file_urls=[gazette_url],
                is_extra_edition=is_extra_edition,
                power="executive",
            )

    def _get_edition_number(self, gazette):
        raw = gazette.xpath("./td[1]/text()").get()
        edition_number_match = re.search(r"(\d+)/", raw)

        if edition_number_match is None:
            return ""
        else:
            return edition_number_match.group(1)
