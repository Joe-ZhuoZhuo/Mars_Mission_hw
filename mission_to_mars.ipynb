{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import dependencies\n",
    "from bs4 import BeautifulSoup as bs\n",
    "from splinter import Browser\n",
    "import os\n",
    "import pandas as pd\n",
    "import time"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## NASA Mars News"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [],
   "source": [
    "#pointing to the directory where chromedriver exists\n",
    "executable_path = {'executable_path': '/usr/local/bin/chromedriver'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [],
   "source": [
    "#visiting the news page\n",
    "url = \"https://mars.nasa.gov/news/\"\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Write it into html\n",
    "html = browser.html\n",
    "soup = bs(html,\"html.parser\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Title: Mars 2020 Rover: T-Minus One Year and Counting \n",
      "Para: The launch period for NASA's next rover, Mars 2020, opens exactly one year from today, July 17, 2020, and extends through Aug. 5, 2020.\n"
     ]
    }
   ],
   "source": [
    "news_title = soup.find(\"div\",class_=\"content_title\").text\n",
    "news_p = soup.find(\"div\", class_=\"article_teaser_body\").text\n",
    "print(f\"Title: {news_title}\")\n",
    "print(f\"Para: {news_p}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## JPL Mars Space Images - Featured Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [],
   "source": [
    "url_Mars_Space_Images = \"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
    "\n",
    "browser.visit(url_Mars_Space_Images)\n",
    "time.sleep(1)\n",
    "\n",
    "html = browser.html\n",
    "\n",
    "soup = bs(html,'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [],
   "source": [
    "featured_image_list = []\n",
    "\n",
    "for image in soup.find_all('div',class_=\"img\"):\n",
    "    featured_image_list.append(image.find('img').get('src'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Feature Image URL: https://www.jpl.nasa.gov//spaceimages/images/wallpaper/PIA23341-640x350.jpg\n"
     ]
    }
   ],
   "source": [
    "\n",
    "#feature image\n",
    "feature_Image = featured_image_list[0]\n",
    "\n",
    "#feature image url \n",
    "feature_Image_url = \"https://www.jpl.nasa.gov/\" + feature_Image\n",
    "\n",
    "feature_Image_dict = {\"image\": feature_Image_url}\n",
    "\n",
    "# print feature image url \n",
    "\n",
    "print(\"Feature Image URL:\", feature_Image_url)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Mars Weather"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [],
   "source": [
    "#get mars weather's latest tweet from the website\n",
    "url_weather = \"https://twitter.com/marswxreport?lang=en\"\n",
    "browser.visit(url_weather)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Putting a 1 ton robot on another planet takes a few peoplehttps://twitter.com/earthtoleo/status/1152463780338532352 …\n"
     ]
    }
   ],
   "source": [
    "\n",
    "html_weather = browser.html\n",
    "soup = bs(html_weather, \"html.parser\")\n",
    "#temp = soup.find('div', attrs={\"class\": \"tweet\", \"data-name\": \"Mars Weather\"})\n",
    "mars_weather = soup.find(\"p\", class_=\"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text\").text\n",
    "print(mars_weather)\n",
    "#temp"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Mars Facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [],
   "source": [
    "url_facts = \"https://space-facts.com/mars/\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mars - Earth Comparison</th>\n",
       "      <th>Mars</th>\n",
       "      <th>Earth</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Diameter:</td>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg</td>\n",
       "      <td>5.97 × 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Distance from Sun:</td>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Length of Year:</td>\n",
       "      <td>687 Earth days</td>\n",
       "      <td>365.24 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Temperature:</td>\n",
       "      <td>-153 to 20 °C</td>\n",
       "      <td>-88 to 58°C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Mars - Earth Comparison             Mars            Earth\n",
       "0               Diameter:         6,779 km        12,742 km\n",
       "1                   Mass:  6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       "2                  Moons:                2                1\n",
       "3      Distance from Sun:   227,943,824 km   149,598,262 km\n",
       "4         Length of Year:   687 Earth days      365.24 days\n",
       "5            Temperature:    -153 to 20 °C      -88 to 58°C"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "table = pd.read_html(url_facts)\n",
    "table[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mars_Values</th>\n",
       "      <th>Earth_Values</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Parameter</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Diameter:</th>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.39 × 10^23 kg</td>\n",
       "      <td>5.97 × 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Distance from Sun:</th>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Length of Year:</th>\n",
       "      <td>687 Earth days</td>\n",
       "      <td>365.24 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Temperature:</th>\n",
       "      <td>-153 to 20 °C</td>\n",
       "      <td>-88 to 58°C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                        Mars_Values     Earth_Values\n",
       "Parameter                                           \n",
       "Diameter:                  6,779 km        12,742 km\n",
       "Mass:               6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       "Moons:                            2                1\n",
       "Distance from Sun:   227,943,824 km   149,598,262 km\n",
       "Length of Year:      687 Earth days      365.24 days\n",
       "Temperature:          -153 to 20 °C      -88 to 58°C"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_mars_facts = table[0]\n",
    "df_mars_facts.columns = [\"Parameter\", \"Mars_Values\",\"Earth_Values\"]\n",
    "df_mars_facts.set_index([\"Parameter\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">  <thead>    <tr style=\"text-align: right;\">      <th></th>      <th>Parameter</th>      <th>Mars_Values</th>      <th>Earth_Values</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>Diameter:</td>      <td>6,779 km</td>      <td>12,742 km</td>    </tr>    <tr>      <th>1</th>      <td>Mass:</td>      <td>6.39 × 10^23 kg</td>      <td>5.97 × 10^24 kg</td>    </tr>    <tr>      <th>2</th>      <td>Moons:</td>      <td>2</td>      <td>1</td>    </tr>    <tr>      <th>3</th>      <td>Distance from Sun:</td>      <td>227,943,824 km</td>      <td>149,598,262 km</td>    </tr>    <tr>      <th>4</th>      <td>Length of Year:</td>      <td>687 Earth days</td>      <td>365.24 days</td>    </tr>    <tr>      <th>5</th>      <td>Temperature:</td>      <td>-153 to 20 °C</td>      <td>-88 to 58°C</td>    </tr>  </tbody></table>'"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mars_html_table = df_mars_facts.to_html()\n",
    "mars_html_table = mars_html_table.replace(\"\\n\", \"\")\n",
    "mars_html_table"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Mars Hemisperes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "url_Mars_Hemisperes = \"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "\n",
    "browser.visit(url_Mars_Hemisperes)\n",
    "\n",
    "html = browser.html\n",
    "\n",
    "soup = bs(html,'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [],
   "source": [
    "mars_hemisperes_title_list = []\n",
    "\n",
    "for img_title in soup.find_all('div',class_=\"description\"):\n",
    "    mars_hemisperes_title_list.append(img_title.find('h3').text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "mars_hemisphere_image_url = []\n",
    "\n",
    "for image in soup.find_all('div',class_=\"item\"):\n",
    "    \n",
    "    url = \"https://astrogeology.usgs.gov/\"\n",
    "    \n",
    "    mars_hemisphere_image_url.append(url + image.find('img').get('src'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['https://astrogeology.usgs.gov//cache/images/dfaf3849e74bf973b59eb50dab52b583_cerberus_enhanced.tif_thumb.png',\n",
       " 'https://astrogeology.usgs.gov//cache/images/7677c0a006b83871b5a2f66985ab5857_schiaparelli_enhanced.tif_thumb.png',\n",
       " 'https://astrogeology.usgs.gov//cache/images/aae41197e40d6d4f3ea557f8cfe51d15_syrtis_major_enhanced.tif_thumb.png',\n",
       " 'https://astrogeology.usgs.gov//cache/images/04085d99ec3713883a9a57f42be9c725_valles_marineris_enhanced.tif_thumb.png']"
      ]
     },
     "execution_count": 102,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mars_hemisphere_image_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {},
   "outputs": [],
   "source": [
    "full_image_url = []\n",
    "\n",
    "for each_url in mars_hemisphere_image_url:\n",
    "    \n",
    "    split_url = each_url.split(\".tif_thumb.png\")[0]\n",
    "    \n",
    "    image_url = split_url + \".tif/full.jpg\"\n",
    "    \n",
    "    full_image_url.append(image_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['https://astrogeology.usgs.gov//cache/images/dfaf3849e74bf973b59eb50dab52b583_cerberus_enhanced.tif/full.jpg',\n",
       " 'https://astrogeology.usgs.gov//cache/images/7677c0a006b83871b5a2f66985ab5857_schiaparelli_enhanced.tif/full.jpg',\n",
       " 'https://astrogeology.usgs.gov//cache/images/aae41197e40d6d4f3ea557f8cfe51d15_syrtis_major_enhanced.tif/full.jpg',\n",
       " 'https://astrogeology.usgs.gov//cache/images/04085d99ec3713883a9a57f42be9c725_valles_marineris_enhanced.tif/full.jpg']"
      ]
     },
     "execution_count": 113,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "full_image_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Cerberus Hemisphere Enhanced',\n",
       " 'Schiaparelli Hemisphere Enhanced',\n",
       " 'Syrtis Major Hemisphere Enhanced',\n",
       " 'Valles Marineris Hemisphere Enhanced']"
      ]
     },
     "execution_count": 114,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mars_hemisperes_title_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [],
   "source": [
    "hemisphere_image_urls = [\n",
    "    {\"title\": \"Valles Marineris Hemisphere\", \"img_url\": full_image_url[3]},\n",
    "    {\"title\": \"Cerberus Hemisphere\", \"img_url\": full_image_url[0]},\n",
    "    {\"title\": \"Schiaparelli Hemisphere\", \"img_url\": full_image_url[1]},\n",
    "    {\"title\": \"Syrtis Major Hemisphere\", \"img_url\": full_image_url[2]},\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [],
   "source": [
    "image_one = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'\n",
    "image_two = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'\n",
    "image_three = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'\n",
    "image_four = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'\n",
    "\n",
    "full_image = {\"image_one\": image_one, \"image_two\":image_two, \"image_three\":image_three, \"image_four\":image_four}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'"
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "full_image['image_one']\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:PythonData=3.6] *",
   "language": "python",
   "name": "conda-env-PythonData_3.6-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
