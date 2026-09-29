"""HTML Web Table to Structured JSON Parser.
100% Python Standard Library.
"""

import re

class WebTableParser:
    """Parses HTML table elements into structured JSON objects."""
    @staticmethod
    def parse_table(html_table):
        th_matches = re.findall(r'<th\b[^>]*>(.*?)</th>', html_table, flags=re.DOTALL | re.IGNORECASE)
        headers = [re.sub(r'<[^>]+>', '', th).strip() for th in th_matches]
        tr_matches = re.findall(r'<tr\b[^>]*>(.*?)</tr>', html_table, flags=re.DOTALL | re.IGNORECASE)
        rows = []
        for tr in tr_matches:
            td_matches = re.findall(r'<td\b[^>]*>(.*?)</td>', tr, flags=re.DOTALL | re.IGNORECASE)
            if td_matches:
                cells = [re.sub(r'<[^>]+>', '', td).strip() for td in td_matches]
                if headers and len(cells) == len(headers):
                    rows.append(dict(zip(headers, cells)))
                else:
                    rows.append(cells)
        return {"headers": headers, "rows": rows}
