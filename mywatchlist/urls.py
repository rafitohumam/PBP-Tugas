from django.urls import path
from mywatchlist.views import show_watchlist
from mywatchlist.views import show_html, show_xml, show_json, show_xml_id, show_json_id

app_name =  "mywatchlist"

urlpatterns = [
    path("", show_watchlist, name="show_watchlist"),
    path("html/", show_html, name="show_html"),
    path("xml/", show_xml, name="show_xml"),
    path("json/", show_json, name="show_json"),
    path("xml/<int:id>", show_xml_id, name="show_xml_id"),
    path("json/<int:id>", show_json_id, name="show_json_id"),
]