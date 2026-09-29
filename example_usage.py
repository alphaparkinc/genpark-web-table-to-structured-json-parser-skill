from client import WebTableParser

table_html = """
<table>
    <tr><th>Symbol</th><th>Price</th><th>Volume</th></tr>
    <tr><td>BTC</td><td>95000</td><td>1200</td></tr>
    <tr><td>ETH</td><td>3400</td><td>8500</td></tr>
</table>
"""

data = WebTableParser.parse_table(table_html)
import json
print("Structured Table JSON:\n" + json.dumps(data, indent=2))
