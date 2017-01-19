import gda_finder
import product_key_search

# URLS
all_fresh_fruit = "http://www.tesco.com/groceries/product/browse/default.aspx?N=4294793658&Ne=4294793660"
all_fresh_veget = "http://www.tesco.com/groceries/product/browse/default.aspx?N=4294793612&Ne=4294793660"
fresh_salad_veg = "http://www.tesco.com/groceries/product/browse/default.aspx?N=4294721050&Ne=4294793660"

# Get ids for page
product_ids = product_key_search.get_ids(all_fresh_fruit)

# For every id get product name and nutritional information
for id in product_ids:
  name, nutrition = gda_finder.get(str(id))
  print name
  print nutrition


  # to populate db you might
  # - use product id (ID) as primary key
  # - store name
  # - store nutrition
  # -- all same tuple


  # so standardise db columns on 100g nutrition values and then have potential to add custom values e.g. per yorkshire pud
  