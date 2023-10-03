from bs4 import BeautifulSoup
import requests
import pandas

response = requests.get("https://300baicode.com/")

page_300_codes = response.text

soup = BeautifulSoup(page_300_codes, "html.parser")
codes = soup.find_all(name="a", class_="text-indigo-600 text-base hover:underline")
code_names = []
code_links = []
for code in codes:
    name = code.getText()
    code_names.append(name)
    link = code.get("href")
    code_links.append(link)

codes_2 = soup.find_all(class_="flex space-x-2")
code_levels_times = []
for code_2 in codes_2:
    level_time = code_2.getText()
    code_levels_times.append(level_time)

df_code_names = pandas.DataFrame(code_names)
df_code_names.to_csv("code_names.csv")
df_code_links = pandas.DataFrame(code_links)
df_code_links.to_csv("code_links.csv")
df_code_levels_times = pandas.DataFrame(code_levels_times)
df_code_levels_times.to_csv("code_levels_times.csv")
df_new_table = df_code_names + df_code_links + df_code_levels_times
df_new_table.to_csv("300baicode.csv")


# print(code_names)
# print(code_links)
# print(code_levels_times)


# PRINT FIRST RESULT
# code_tag_1_s = soup.find(name="a", class_="text-indigo-600 text-base hover:underline")
# name = code_tag_1_s.getText()
# link = code_tag_1_s.get("href")
#
# codes_tag_2_s = soup.find(class_="flex space-x-2")
# code_level_time = codes_tag_2_s.getText()
#
# print(name)
# print(link)
# print(code_level_time)

