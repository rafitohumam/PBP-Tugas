from django.test import TestCase
from katalog.models import CatalogItem

class Test(TestCase):

    def test(self):
        test_1 = CatalogItem.objects.get(item_name = "Macbook Pro M2")
        test_2 = CatalogItem.objects.get(item_name = "Sony A7 ii")
        test_3 = CatalogItem.objects.get(item_name = "Dior Sauvage")
        test_4 = CatalogItem.objects.get(item_name = "Apple Watch 3")
        self.assertIn("Macbook Pro M2", test_1.item_name)
        self.assertIn("Sony A7 ii", test_2.item_name)
        self.assertIn("Dior Sauvage", test_3.item_name)
        self.assertIn("Apple Watch 3", test_4.item_name)

    def setUp(self):
        CatalogItem.objects.create(
            item_name = "Macbook Pro M2",
            item_price = 21649000,
            item_stock = 12,
            description = "Macbook Pro terbaru dengan processor M2",
            rating = 5,
            item_url = "https://www.tokopedia.com/newrizkyapple/apple-macbook-pro-m2-2022-13-512gb-grey-silver-256gb-ibox-not-m1-512gb-inter-space-grey?extParam=ivf%3Dfalse&src=topads")
        
        CatalogItem.objects.create(
            item_name = "Sony A7 ii",
            item_price = 19999000,
            item_stock = 4,
            description = "Kamera full-frame dengan value terbaik",
            rating = 4,
            item_url = "https://www.tokopedia.com/focus-nusantara/sony-alpha-a7-ii-fe-85mm-f18")

        CatalogItem.objects.create(
            item_name = "Dior Sauvage",
            item_price = 2000000,
            item_stock = 20,
            description = "Parfum mas-mas ganteng",
            rating = 5,
            item_url = "https://www.tokopedia.com/newgloriaparfum/original-parfum-christian-dior-sauvage-edp-100ml-men")
        
        CatalogItem.objects.create(
            item_name = "Apple Watch 3",
            item_price = 2770000,
            item_stock = 50,
            description = "Jam tengan pintar terkeren",
            rating = 4,
            item_url = "https://www.tokopedia.com/techstudioid/garansi-ibox-apple-watch-series-3-42mm-38mm-space-grey-silver-sport-grs-apple-inter-38mm-space-grey?extParam=ivf%3Dfalse&src=topads")