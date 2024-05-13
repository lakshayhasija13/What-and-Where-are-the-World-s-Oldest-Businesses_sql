#!/usr/bin/env python
# coding: utf-8

# ## 1. The oldest business in the world
# <p><img src="https://assets.datacamp.com/production/repositories/5851/datasets/7dded924c6dc418d4a828f2f4daba99953c27a5a/400px-Eingang_zum_St._Peter_Stiftskeller.jpg" alt="The entrance to St. Peter Stiftskeller, a restaurant in Saltzburg, Austria. The sign over the entrance shows &quot;803&quot; - the year the business opened."></p>
# <p><em>Image: St. Peter Stiftskeller, founded 803. Credit: <a href="https://commons.wikimedia.org/wiki/File:Eingang_zum_St._Peter_Stiftskeller.jpg">Pakeha</a>.</em></p>
# <p>An important part of business is planning for the future and ensuring that the company survives changing market conditions. Some businesses do this really well and last for hundreds of years.</p>
# <p>BusinessFinancing.co.uk <a href="https://businessfinancing.co.uk/the-oldest-company-in-almost-every-country">researched</a> the oldest company that is still in business in (almost) every country and compiled the results into a dataset. In this project, you'll explore that dataset to see what they found.</p>
# <p>The database contains three tables.</p>
# <h3 id="categories"><code>categories</code></h3>
# <table>
# <thead>
# <tr>
# <th style="text-align:left;">column</th>
# <th>type</th>
# <th>meaning</th>
# </tr>
# </thead>
# <tbody>
# <tr>
# <td style="text-align:left;"><code>category_code</code></td>
# <td>varchar</td>
# <td>Code for the category of the business.</td>
# </tr>
# <tr>
# <td style="text-align:left;"><code>category</code></td>
# <td>varchar</td>
# <td>Description of the business category.</td>
# </tr>
# </tbody>
# </table>
# <h3 id="countries"><code>countries</code></h3>
# <table>
# <thead>
# <tr>
# <th style="text-align:left;">column</th>
# <th>type</th>
# <th>meaning</th>
# </tr>
# </thead>
# <tbody>
# <tr>
# <td style="text-align:left;"><code>country_code</code></td>
# <td>varchar</td>
# <td>ISO 3166-1 3-letter country code.</td>
# </tr>
# <tr>
# <td style="text-align:left;"><code>country</code></td>
# <td>varchar</td>
# <td>Name of the country.</td>
# </tr>
# <tr>
# <td style="text-align:left;"><code>continent</code></td>
# <td>varchar</td>
# <td>Name of the continent that the country exists in.</td>
# </tr>
# </tbody>
# </table>
# <h3 id="businesses"><code>businesses</code></h3>
# <table>
# <thead>
# <tr>
# <th style="text-align:left;">column</th>
# <th>type</th>
# <th>meaning</th>
# </tr>
# </thead>
# <tbody>
# <tr>
# <td style="text-align:left;"><code>business</code></td>
# <td>varchar</td>
# <td>Name of the business.</td>
# </tr>
# <tr>
# <td style="text-align:left;"><code>year_founded</code></td>
# <td>int</td>
# <td>Year the business was founded.</td>
# </tr>
# <tr>
# <td style="text-align:left;"><code>category_code</code></td>
# <td>varchar</td>
# <td>Code for the category of the business.</td>
# </tr>
# <tr>
# <td style="text-align:left;"><code>country_code</code></td>
# <td>char</td>
# <td>ISO 3166-1 3-letter country code.</td>
# </tr>
# </tbody>
# </table>
# <p>Let's begin by looking at the range of the founding years throughout the world.</p>

# In[226]:


get_ipython().run_cell_magic('sql', '', 'postgresql:///oldestbusinesses\n \n-- Select the oldest and newest founding years from the businesses table\nSELECT MIN(year_founded) AS min, MAX(year_founded) AS max\nFROM businesses;')


# In[227]:


get_ipython().run_cell_magic('nose', '', 'last_output = _\n\ndef test_resultset():\n    try:\n        assert str(type(last_output)) == "<class \'sql.run.ResultSet\'>"\n    except AssertionError:\n        assert False, "Please ensure a SQL ResultSet is the output of the code cell." \nresults = last_output.DataFrame()\ndef test_shape():\n    try:\n        assert results.shape == (1, 2)\n    except AssertionError:\n        assert False, "The results should have two columns and a single row."\ndef test_colnames():\n    try:\n        assert results.columns.tolist() == [\'min\', \'max\']\n    except AssertionError:\n        assert False, "The results should have columns named `\'min` and `\'max\'`."\ndef test_min_year_founded():\n    try:\n        assert results.loc[0, \'min\'] == 578\n    except AssertionError:\n        assert False, "The oldest year founded is incorrect."\ndef test_max_year_founded():\n    try:\n        assert results.loc[0, \'max\'] == 1999 \n    except AssertionError:\n        assert False, "The newest year founded is incorrect."')


# ## 2. How many businesses were founded before 1000?
# <p>Wow! That's a lot of variation between countries. In one country, the oldest business was only founded in 1999. By contrast, the oldest business in the world was founded back in 578. That's pretty incredible that a business has survived for more than a millennium.</p>
# <p>I wonder how many other businesses there are like that.</p>

# In[228]:


get_ipython().run_cell_magic('sql', '', '\n-- Get the count of rows in businesses where the founding year was before 1000\nSELECT COUNT(*) AS count\nFROM businesses \nWHERE year_founded < 1000;')


# In[229]:


get_ipython().run_cell_magic('nose', '', 'last_output = _\n\ndef test_resultset():\n    try:\n        assert str(type(last_output)) == "<class \'sql.run.ResultSet\'>"\n    except AssertionError:\n        assert False, "Please ensure a SQL ResultSet is the output of the code cell." \nresults = last_output.DataFrame()\ndef test_shape():\n    try:\n        assert results.shape == (1, 1)\n    except AssertionError:\n        assert False, "The results should have a single column and a single row."\ndef test_colnames():\n    try:\n        assert results.columns.tolist() == [\'count\']\n    except AssertionError:\n        assert False, "The results should have a column named `\'count`."\ndef test_count():\n    try:\n        assert last_output.DataFrame().loc[0, \'count\'] == 6\n    except AssertionError:\n        assert False, "The count of businesses founded before 1000 is incorrect."')


# ## 3. Which businesses were founded before 1000?
# <p>Having a count is all very well, but I'd like more detail. Which businesses have been around for more than a millennium?</p>

# In[230]:


get_ipython().run_cell_magic('sql', '', '\n-- Select all columns from businesses where the founding year was before 1000\nSELECT * \nFROM businesses \nWHERE year_founded < 1000\n-- Arrange the results from oldest to newest\nORDER BY year_founded ASC;')


# In[231]:


get_ipython().run_cell_magic('nose', '', 'last_output = _\n\ndef test_resultset():\n    try:\n        assert str(type(last_output)) == "<class \'sql.run.ResultSet\'>"\n    except AssertionError:\n        assert False, "Please ensure a SQL ResultSet is the output of the code cell." \nresults = last_output.DataFrame()\ndef test_shape():\n    try:\n        assert results.shape == (6, 4)\n    except AssertionError:\n        assert False, "The results should have four columns and six rows."\ndef test_colnames():\n    try:\n        assert results.columns.tolist() == [\'business\', \'year_founded\', \'category_code\', \'country_code\']\n    except AssertionError:\n        assert False, "The results should have the four columns from the `businesses` table."\ndef test_where_year_founded_lt_1000():\n    try:\n        assert results.loc[:, \'year_founded\'].max() < 1000 \n    except AssertionError:\n        assert False, "The most recent year founded is not before 1000."\ndef test_ordered_by_year_founded():\n    try:\n        assert results.loc[:, \'year_founded\'].is_monotonic \n    except AssertionError:\n        assert False, "The rows are not ordered by increasing year founded."')


# ## 4. Exploring the categories
# <p>Now we know that the oldest, continuously operating company in the world is called Kongō Gumi. But was does that company do? The category codes in the <code>businesses</code> table aren't very helpful: the descriptions of the categories are stored in the <code>categories</code> table.</p>
# <p>This is a common problem: for data storage, it's better to keep different types of data in different tables, but for analysis, you want all the data in one place. To solve this, you'll have to join the two tables together.</p>

# In[232]:


get_ipython().run_cell_magic('sql', '', '\n-- Select business name, founding year, and country code from businesses; and category from categories\nSELECT b.business, b.year_founded, b.country_code, c.category\nFROM businesses AS b \nINNER JOIN categories AS c\nUSING(category_code)\n-- where the founding year was before 1000, arranged from oldest to newest\nWHERE b.year_founded < 1000\nORDER BY b.year_founded ASC;')


# In[233]:


get_ipython().run_cell_magic('nose', '', 'last_output = _\n\ndef test_resultset():\n    try:\n        assert str(type(last_output)) == "<class \'sql.run.ResultSet\'>"\n    except AssertionError:\n        assert False, "Please ensure a SQL ResultSet is the output of the code cell." \nresults = last_output.DataFrame()\ndef test_shape():\n    try:\n        assert results.shape == (6, 4)\n    except AssertionError:\n        assert False, "The results should have four columns and six rows."\ndef test_colnames():\n    try:\n        assert results.columns.tolist() == [\'business\', \'year_founded\', \'country_code\', \'category\']\n    except AssertionError:\n        assert False, "The results should have business, year founded, and country code columns from the `businesses` table and category from the `categories` table."\ndef test_where_year_founded_lt_1000():\n    try:\n        assert results.loc[:, \'year_founded\'].max() < 1000 \n    except AssertionError:\n        assert False, "The most recent year founded is not before 1000."\ndef test_ordered_by_year_founded():\n    try:\n        assert results.loc[:, \'year_founded\'].is_monotonic \n    except AssertionError:\n        assert False, "The rows are not ordered by increasing year founded."')


# ## 5. Counting the categories
# <p>With that extra detail about the oldest businesses, we can see that Kongō Gumi is a construction company. In that list of six businesses, we also see a café, a winery, and a bar. The two companies recorded as "Manufacturing and Production" are both mints. That is, they produce currency.</p>
# <p>I'm curious as to what other industries constitute the oldest companies around the world, and which industries are most common.</p>

# In[234]:


get_ipython().run_cell_magic('sql', '', '\n-- Select the category and count of category (as "n")\nSELECT c.category, COUNT(*) AS n \nFROM categories AS c\nINNER JOIN businesses \nUSING(category_code)\n-- arranged by descending count, limited to 10 most common categories\nGROUP BY c.category\nORDER BY COUNT(*) DESC\nLIMIT 10;')


# In[235]:


get_ipython().run_cell_magic('nose', '', 'last_output = _\n\ndef test_resultset():\n    try:\n        assert str(type(last_output)) == "<class \'sql.run.ResultSet\'>"\n    except AssertionError:\n        assert False, "Please ensure a SQL ResultSet is the output of the code cell." \nresults = last_output.DataFrame()\ndef test_shape():\n    try:\n        assert results.shape == (10, 2)\n    except AssertionError:\n        assert False, "The results should have two columns and ten rows."\ndef test_colnames():\n    try:\n        assert results.columns.tolist() == [\'category\', \'n\']\n    except AssertionError:\n        assert False, "The results should have a category column and a count column named `\'n\'`."\ndef test_ordered_by_desc_n():\n    try:\n        assert results.loc[:, \'n\'].is_monotonic_decreasing\n    except AssertionError:\n        assert False, "The rows are not ordered by descending count."\ndef test_count():\n    try:\n        assert results.loc[:, \'n\'].values.tolist() == [37, 22, 19, 16, 15, 7, 6, 6, 6, 4]\n    except AssertionError:\n        assert False, "The category counts are not correct."')


# ## 6. Oldest business by continent
# <p>It looks like "Banking &amp; Finance" is the most popular category. Maybe that's where you should aim if you want to start a thousand-year business.</p>
# <p>One thing we haven't looked at yet is where in the world these really old businesses are. To answer these questions, we'll need to join the <code>businesses</code> table to the <code>countries</code> table. Let's start by asking how old the oldest business is on each continent.</p>

# In[236]:


get_ipython().run_cell_magic('sql', '', '\n-- Select the oldest founding year (as "oldest") from businesses,\nSELECT MIN(b.year_founded) AS oldest, co.continent \nFROM businesses AS b\n-- and continent from countries\nINNER JOIN countries AS co \nUSING(country_code)\n-- for each continent, ordered from oldest to newest \nGROUP BY co.continent\nORDER BY oldest;')


# In[237]:


get_ipython().run_cell_magic('nose', '', 'last_output = _\n\ndef test_resultset():\n    try:\n        assert str(type(last_output)) == "<class \'sql.run.ResultSet\'>"\n    except AssertionError:\n        assert False, "Please ensure a SQL ResultSet is the output of the code cell." \nresults = last_output.DataFrame()\ndef test_shape():\n    try:\n        assert results.shape == (6, 2)\n    except AssertionError:\n        assert False, "The results should have two columns and six rows."\ndef test_colnames():\n    try:\n        assert results.columns.tolist() == [\'oldest\', \'continent\']\n    except AssertionError:\n        assert False, "The results should have columns named oldest, and continent."\ndef test_ordered_by_min_year_founded():\n    try:\n        assert results.loc[:, \'oldest\'].is_monotonic \n    except AssertionError:\n        assert False, "The rows are not ordered by year founded."\ndef test_count():\n    try:\n        assert results.loc[:, \'oldest\'].values.tolist() == [578, 803, 1534, 1565, 1772, 1809]\n    except AssertionError:\n        assert False, "The year founded values are not correct."')


# ## 7. Joining everything for further analysis
# <p>Interesting. There's a jump in time from the older businesses in Asia and Europe to the 16th Century oldest businesses in North and South America, then to the 18th and 19th Century oldest businesses in Africa and Oceania. </p>
# <p>As mentioned earlier, when analyzing data it's often really helpful to have all the tables you want access to joined together into a single set of results that can be analyzed further. Here, that means we need to join all three tables.</p>

# In[238]:


get_ipython().run_cell_magic('sql', '', '\n-- Select the business, founding year, category, country, and continent\nSELECT b.business, b.year_founded, c.category, co.country, co.continent\nFROM businesses AS b \nINNER JOIN countries AS co \nON b.country_code = co.country_code\nINNER JOIN categories AS c \nON b.category_code = c.category_code;')


# In[239]:


get_ipython().run_cell_magic('nose', '', 'last_output = _\n\ndef test_resultset():\n    try:\n        assert str(type(last_output)) == "<class \'sql.run.ResultSet\'>"\n    except AssertionError:\n        assert False, "Please ensure a SQL ResultSet is the output of the code cell." \nresults = last_output.DataFrame()\ndef test_shape():\n    try:\n        assert results.shape == (163, 5)\n    except AssertionError:\n        assert False, "The results should have five columns and one hundred and sixty three rows."\ndef test_colnames():\n    try:\n        assert results.columns.tolist() == [\'business\', \'year_founded\', \'category\', \'country\', \'continent\']\n    except AssertionError:\n        assert False, "The results should have columns named business, year_founded, category, country, and continent."  ')


# ## 8. Counting categories by continent
# <p>Having <code>businesses</code> joined to <code>categories</code> and <code>countries</code> together means we can ask questions about both these things together. For example, which are the most common categories for the oldest businesses on each continent?</p>

# In[240]:


get_ipython().run_cell_magic('sql', '', '\n-- Count the number of businesses in each continent and category\nSELECT co.continent, c.category, COUNT(*) AS n\nFROM businesses AS b\nINNER JOIN categories AS c\nON b.category_code = c.category_code\nINNER JOIN countries AS co \nON co.country_code = b.country_code\nGROUP BY co.continent, c.category;')


# In[241]:


get_ipython().run_cell_magic('nose', '', 'last_output = _\n\ndef test_resultset():\n    try:\n        assert str(type(last_output)) == "<class \'sql.run.ResultSet\'>"\n    except AssertionError:\n        assert False, "Please ensure a SQL ResultSet is the output of the code cell." \nresults = last_output.DataFrame()\ndef test_shape():\n    try:\n        assert results.shape == (56, 3)\n    except AssertionError:\n        assert False, "The results should have three columns and fifty six rows."\ndef test_colnames():\n    try:\n        assert results.columns.tolist() == [\'continent\', \'category\', \'n\']\n    except AssertionError:\n        assert False, "The results should have continent, category, and count (as \'n\')."\ndef test_count():\n    try:\n        assert results.loc[:, \'n\'].sort_values(ascending=False).values.tolist() == [17, 12, 10, 9, 8, 7, 6, 5, 5, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]\n    except AssertionError:\n        assert False, "The counts are not correct."')


# ## 9. Filtering counts by continent and category
# <p>Combining continent and business category led to a lot of results. It's difficult to see what is important. To trim this down to a manageable size, let's restrict the results to only continent/category pairs with a high count.</p>

# In[242]:


get_ipython().run_cell_magic('sql', '', '\n-- Repeat that previous query, filtering for results having a count greater than 5\nSELECT co.continent, c.category, COUNT(*) AS n\nFROM businesses AS b\nINNER JOIN categories AS c\nON b.category_code = c.category_code\nINNER JOIN countries AS co \nON co.country_code = b.country_code\nGROUP BY co.continent, c.category\nHAVING COUNT(*) > 5\nORDER BY n DESC;')


# In[243]:


get_ipython().run_cell_magic('nose', '', 'last_output = _\n\ndef test_resultset():\n    try:\n        assert str(type(last_output)) == "<class \'sql.run.ResultSet\'>"\n    except AssertionError:\n        assert False, "Please ensure a SQL ResultSet is the output of the code cell." \nresults = last_output.DataFrame()\ndef test_shape():\n    try:\n        assert results.shape == (7, 3)\n    except AssertionError:\n        assert False, "The results should have three columns and seven rows."\ndef test_colnames():\n    try:\n        assert results.columns.tolist() == [\'continent\', \'category\', \'n\']\n    except AssertionError:\n        assert False, "The results should have continent, category, and count (as \'n\')."\ndef test_count():\n    try:\n        assert results.loc[:, \'n\'].values.tolist() == [17, 12, 10, 9, 8, 7, 6]\n    except AssertionError:\n        assert False, "The counts are not correct."')

