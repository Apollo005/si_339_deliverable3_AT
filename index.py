import csv
from jinja2 import Environment, FileSystemLoader

# Load Jinja2 environment and templates directory
env = Environment(loader=FileSystemLoader('templates'))

# Paths to the CSV files for Adrienne Stewart, Alex Nemecek, and Amir Abston
alex_csv = "athletes/mens_team/Alex Nemecek18820260.csv"
amir_csv = "athletes/mens_team/Amir Abston25395576.csv"
bruno_csv = "athletes/mens_team/Bruno Cifaldi21147176.csv"
cole_csv = "athletes/mens_team/Cole Harms26322018.csv"
dylan_csv = "athletes/mens_team/Dylan Hanley23349680.csv"
emmett_csv = "athletes/mens_team/Emmett Strait26322025.csv"
enshu_csv = "athletes/mens_team/Enshu Kuan23687884.csv"
ethan_csv = "athletes/mens_team/Ethan Miller23349703.csv"
garrett_csv = "athletes/mens_team/Garrett Comer21615274.csv"
gustaf_csv = "athletes/mens_team/Gustaf Finn21147171.csv"

adrienne_csv = "athletes/womens_team/Adrienne Stewart21142907.csv"
alexandra_csv = "athletes/womens_team/Alexandra Wren21142908.csv"
alison_csv = "athletes/womens_team/Alison Kauffman23564882.csv"
ann_csv = "athletes/womens_team/Ann Kececi24802381.csv"
arabella_csv = "athletes/womens_team/Arabella Kessler23564883.csv"
calla_csv = "athletes/womens_team/Arabella Kessler23564883.csv"
elin_csv = "athletes/womens_team/Elin Tenbrink23349718.csv"
elsa_csv = "athletes/womens_team/Elsa Wenzlaff22520388.csv"
emily_csv = "athletes/womens_team/Emily Mei22520376.csv"
irie_csv = "athletes/womens_team/Irie Scrase23564884.csv"

# Function to load and clean CSV data
def load_csv_data(file_path):
    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = [row for row in reader if row]  # Remove empty rows
    return data

# Extract athlete info from CSV
def extract_athlete_info(data):
    athlete_name = data[0][0] if len(data[0]) > 0 else "Unknown"
    athlete_id = data[1][0] if len(data) > 1 else "Unknown"
    athlete_link = f"https://www.athletic.net/athlete/{athlete_id}/cross-country/high-school"
    athlete_grade = next((row[2] for row in data if len(row) > 2 and row[2].isdigit()), "N/A")
    return athlete_name, athlete_id, athlete_link, athlete_grade

# Load CSV data for athletes
alex_data = load_csv_data(alex_csv)
amir_data = load_csv_data(amir_csv)
bruno_data = load_csv_data(bruno_csv)
garrett_data = load_csv_data(garrett_csv)
cole_data = load_csv_data(cole_csv)
ethan_data = load_csv_data(ethan_csv)
dylan_data = load_csv_data(dylan_csv)
gustaf_data = load_csv_data(gustaf_csv)
emmett_data = load_csv_data(emmett_csv)
enshu_data = load_csv_data(enshu_csv)

adrienne_data = load_csv_data(adrienne_csv)
alexandra_data = load_csv_data(alexandra_csv)
alison_data = load_csv_data(alison_csv)
ann_data = load_csv_data(ann_csv)
arabella_data = load_csv_data(arabella_csv)
calla_data = load_csv_data(calla_csv)
elin_data = load_csv_data(elin_csv)
elsa_data = load_csv_data(elsa_csv)
emily_data = load_csv_data(emily_csv)
irie_data = load_csv_data(irie_csv)

# Extract athlete info
alex_name, alex_id, alex_link, alex_grade = extract_athlete_info(alex_data)
amir_name, amir_id, amir_link, amir_grade = extract_athlete_info(amir_data)
bruno_name, bruni_id, bruno_link, bruno_grade = extract_athlete_info(bruno_data)
garrett_name, garrett_id, garrett_link, garrett_grade = extract_athlete_info(garrett_data)
cole_name, cole_id, cole_link, cole_grade = extract_athlete_info(cole_data)
ethan_name, ethan_id, ethan_link, ethan_grade = extract_athlete_info(ethan_data)
dylan_name, dylan_id, dylan_link, dylan_grade = extract_athlete_info(dylan_data)
gustaf_name, gustaf_id, gustaf_link, gustaf_grade = extract_athlete_info(gustaf_data)
emmett_name, emmett_id, emmett_link, emmett_grade = extract_athlete_info(emmett_data)
enshu_name, enshu_id, enshu_link, enshu_grade = extract_athlete_info(enshu_data)

adrienne_name, adrienne_id, adrienne_link, adrienne_grade = extract_athlete_info(adrienne_data)
alexandra_name, alexandra_id, alexandra_link, alexandra_grade = extract_athlete_info(alexandra_data)
alison_name, alison_id, alison_link, alison_grade = extract_athlete_info(alison_data)
ann_name, ann_id, ann_link, ann_grade = extract_athlete_info(ann_data)
arabella_name, arabella_id, arabella_link, arabella_grade = extract_athlete_info(arabella_data)
calla_name, calla_id, calla_link, calla_grade = extract_athlete_info(calla_data)
elin_name, elin_id, elin_link, elin_grade = extract_athlete_info(elin_data)
elsa_name, elsa_id, elsa_link, elsa_grade = extract_athlete_info(elsa_data)
emily_name, emily_id, emily_link, emily_grade = extract_athlete_info(emily_data)
irie_name, irie_id, irie_link, irie_grade = extract_athlete_info(irie_data)


# Extract season records for each athlete
def extract_season_records(data):
    return [
        {"Year": int(row[1]), "Grade": int(row[2]), "Time": row[3]}
        for row in data if len(row) > 3 and row[1].isdigit() and int(row[1]) > 1999
    ]

# Extract season records
alex_records = extract_season_records(alex_data)
amir_records = extract_season_records(amir_data)
bruno_records = extract_season_records(bruno_data)
garrett_records = extract_season_records(garrett_data)
cole_records = extract_season_records(cole_data)
ethan_records = extract_season_records(ethan_data)
dylan_records = extract_season_records(dylan_data)
gustaf_records = extract_season_records(gustaf_data)
emmett_records = extract_season_records(emmett_data)
enshu_records = extract_season_records(enshu_data)

adrienne_records = extract_season_records(adrienne_data)
alexandra_records = extract_season_records(alexandra_data)
alison_records = extract_season_records(alison_data)
ann_records = extract_season_records(ann_data)
arabella_records = extract_season_records(arabella_data)
calla_records = extract_season_records(calla_data)
elin_records = extract_season_records(elin_data)
elsa_records = extract_season_records(elsa_data)
emily_records = extract_season_records(emily_data)
irie_records = extract_season_records(irie_data)

# Extract races from CSV data
def extract_races(data):
    races = []
    for row in data:
        # Skip rows that don't have enough data or are headers
        if len(row) < 6 or row[0] == "Name":
            continue
        if int(row[1]) < 1999:  # Assuming this is the year column
            race_dict = {
                "Place": row[1],
                "Time": row[3],
                "Date": row[4],
                "Meet": row[5]
            }
            races.append(race_dict)
    return races

# Filter 2024 races
def filter_2024_races(races):
    races_2024 = []
    for race in races:
        if "Aug" in race["Date"][0:3]:  # Example logic to filter races in 2024
            break
        races_2024.append(race)
    return races_2024

# Extract and filter races for each athlete
alex_races = extract_races(alex_data)
amir_races = extract_races(amir_data)
bruno_races = extract_races(bruno_data)
garrett_races = extract_races(garrett_data)
cole_races = extract_races(cole_data)
ethan_races = extract_races(ethan_data)
dylan_races = extract_races(dylan_data)
gustaf_races = extract_races(gustaf_data)
emmett_races = extract_races(emmett_data)
enshu_races = extract_races(enshu_data)

adrienne_races = extract_races(adrienne_data)
alexandra_races = extract_races(alexandra_data)
alison_races = extract_races(alison_data)
ann_races = extract_races(ann_data)
arabella_races = extract_races(arabella_data)
calla_races = extract_races(calla_data)
elin_races = extract_races(elin_data)
elsa_races = extract_races(elsa_data)
emily_races = extract_races(emily_data)
irie_races = extract_races(irie_data)


alex_races_2024 = filter_2024_races(alex_races)
amir_races_2024 = filter_2024_races(amir_races)
bruno_races_2024 = filter_2024_races(bruno_races)
garrett_races_2024 = filter_2024_races(garrett_races)
cole_races_2024 = filter_2024_races(cole_races)
ethan_races_2024 = filter_2024_races(ethan_races)
dylan_races_2024 = filter_2024_races(dylan_races)
gustaf_races_2024 = filter_2024_races(gustaf_races)
emmett_races_2024 = filter_2024_races(emmett_races)
enshu_races_2024 = filter_2024_races(enshu_races)

adrienne_races_2024 = filter_2024_races(adrienne_races)
alexandra_races_2024 = filter_2024_races(alexandra_races)
alison_races_2024 = filter_2024_races(alison_races)
ann_races_2024 = filter_2024_races(ann_races)
arabella_races_2024 = filter_2024_races(arabella_races)
calla_races_2024 = filter_2024_races(calla_races)
elin_races_2024 = filter_2024_races(elin_races)
elsa_races_2024 = filter_2024_races(elsa_races)
emily_races_2024 = filter_2024_races(emily_races)
irie_races_2024 = filter_2024_races(irie_races)

# Generate dynamic HTML table for races
def races_table_maker(races_list):
    if not races_list:
        return
    
    html_table = "<table>\n<tr>\n<th>Place</th>\n<th>Time</th>\n<th>Date</th>\n<th>Meet</th>\n</tr>\n"
    for race in races_list:
        html_table += f"<tr><td>{race['Place']}</td><td>{race['Time']}</td><td>{race['Date']}</td><td>{race['Meet']}</td></tr>\n"
    html_table += "</table>\n"
    return html_table

# Generate dynamic HTML table for season records
def table_maker(list_dicts):
    if not list_dicts:
        return
    
    html_table = "<table>\n<tr>\n"
    for key in list_dicts[0].keys():
        html_table += f"<th>{key}</th>\n"
    html_table += "</tr>\n"
    
    for entry in list_dicts:
        html_table += "<tr>\n"
        for value in entry.values():
            html_table += f"<td>{value}</td>\n"
        html_table += "</tr>\n"
    
    html_table += "</table>\n"
    return html_table

# Generate tables for season records
alex_table = table_maker(alex_records)
amir_table = table_maker(amir_records)
bruno_table = table_maker(bruno_records)
garrett_table = table_maker(garrett_records)
cole_table = table_maker(cole_records)
ethan_table = table_maker(ethan_records)
dylan_table = table_maker(dylan_records)
gustaf_table = table_maker(gustaf_records)
emmett_table = table_maker(emmett_records)
enshu_table = table_maker(enshu_records)

adrienne_table = table_maker(adrienne_records)
alexandra_table = table_maker(alexandra_records)
alison_table = table_maker(alison_records)
ann_table = table_maker(ann_records)
arabella_table = table_maker(arabella_records)
calla_table = table_maker(calla_records)
elin_table = table_maker(elin_records)
elsa_table = table_maker(elsa_records)
emily_table = table_maker(emily_records)
irie_table = table_maker(irie_records)

# Generate tables for 2024 races
alex_races_table_2024 = races_table_maker(alex_races_2024)
amir_races_table_2024 = races_table_maker(amir_races_2024)
bruno_races_table_2024 = races_table_maker(bruno_races_2024)
garrett_races_table_2024 = races_table_maker(garrett_races_2024)
cole_races_table_2024 = races_table_maker(cole_races_2024)
ethan_races_table_2024 = races_table_maker(ethan_races_2024)
dylan_races_table_2024 = races_table_maker(dylan_races_2024)
gustaf_races_table_2024 = races_table_maker(gustaf_races_2024)
emmett_races_table_2024 = races_table_maker(emmett_races_2024)
enshu_races_table_2024 = races_table_maker(enshu_races_2024)

adrienne_races_table_2024 = races_table_maker(adrienne_races_2024)
alexandra_races_table_2024 = races_table_maker(alexandra_races_2024)
alison_races_table_2024 = races_table_maker(alison_races_2024)
ann_races_table_2024 = races_table_maker(ann_races_2024)
arabella_races_table_2024 = races_table_maker(arabella_races_2024)
calla_races_table_2024 = races_table_maker(calla_races_2024)
elin_races_table_2024 = races_table_maker(elin_races_2024)
emily_races_table_2024 = races_table_maker(emily_races_2024)
elsa_races_table_2024 = races_table_maker(elsa_races_2024)
irie_races_table_2024 = races_table_maker(irie_races_2024)

# Top 10 for index page
mens_top10 = [{"Rank": 1, "Name": "Bruno Cifaldi", "Time": "16:57.4 PR"}, {"Rank": 2, "Name": "Enshu Kuan", "Time": "17:20.8 PR"}, 
              {"Rank": 3, "Name": "Dylan Hanley", "Time": "18:13.9 PR"}, {"Rank": 4, "Name": "Gustaf Finn", "Time": "18:22.8 PR"}, 
              {"Rank": 5, "Name": "Alex Nemecek", "Time": "18:24.0 PR"}, {"Rank": 6, "Name": "Garrett Comer", "Time": "18:24.6 PR"},
              {"Rank": 7, "Name": "Emmett Strait", "Time": "19:41.3 PR"}, {"Rank": 8, "Name": "Ethan Miller", "Time": "21:25.1 PR"}, 
              {"Rank": 9, "Name": "Cole Harms", "Time": "24:34.5 PR"}, {"Rank": 10, "Name": "Amir Abston", "Time": "25:25.0 PR"}]

womens_top10 = [{"Rank": 1, "Name": "Irie Scrase", "Time": "19:08.3 PR"}, {"Rank": 2, "Name": "Alison Kauffman", "Time": "21:59.0 PR"},
                {"Rank": 3, "Name": "Adrienne Stewart", "Time": "22:21.2 PR"},{"Rank": 4, "Name": "Elin Tenbrink", "Time": "22:30.0 PR"},
                {"Rank": 5, "Name": "Emily Mei", "Time": "24:19.3 PR"}, {"Rank": 6, "Name": "Alexandra Wren", "Time": "24:22.1 PR"},
                {"Rank": 7, "Name": "Calla Sopoci", "Time": "24:30.4 PR"}, {"Rank": 8, "Name": "Ann Kececi", "Time": "24:46.0 PR"},
                {"Rank": 9, "Name": "Elsa Wenzlaff", "Time": "24:54.7 PR"}, {"Rank": 10, "Name": "Arabella Kessler", "Time": "28:52.0 PR"}]

mens_top10_table = table_maker(mens_top10)
womens_top10_table = table_maker(womens_top10)

# Render the index.html template (pass both top 10 lists)
index_template = env.get_template('index.html')
index_html = index_template.render(
    site_title="Men's and Women's Top 10 XC Times",
    page_heading="Top 10 Overall Rankings for Men and Women",
    mens_top10=mens_top10,  # Pass the raw data list
    womens_top10=womens_top10,  # Pass the raw data list
    mens_top10_table=mens_top10_table,
    womens_top10_table=womens_top10_table
)

# Save the generated index.html
with open("index.html", "w") as f:
    f.write(index_html)

# Render and save athlete pages
athlete_template = env.get_template('athlete.html')

# Alex Nemecek's page
athlete_html_alex = athlete_template.render(
    athlete_name=alex_name,
    athlete_grade=alex_grade,
    athlete_school="Ann Arbor Skyline",
    season_year="2024",
    races_2024_table=alex_races_table_2024,  # Now passing the races table
    all_records_table=alex_table,
    season_notes="<li>2024: PR</li>"
)
with open("athlete-alex.html", "w") as f:
    f.write(athlete_html_alex)

# Amir Abston's page
athlete_html_amir = athlete_template.render(
    athlete_name=amir_name,
    athlete_grade=amir_grade,
    athlete_school="Ann Arbor Skyline",
    season_year="2024",
    races_2024_table=amir_races_table_2024,  # Now passing the races table
    all_records_table=amir_table,
    season_notes="<li>2024: PR</li>"
)
with open("athlete-amir.html", "w") as f:
    f.write(athlete_html_amir)

# Bruno Cifaldi's page
athlete_html_bruno = athlete_template.render(
    athlete_name=bruno_name,
    athlete_grade=bruno_grade,
    athlete_school="Ann Arbor Skyline",
    season_year="2024",
    races_2024_table=bruno_races_table_2024,  # Now passing the races table
    all_records_table=bruno_table,
    season_notes="<li>2023: PR</li> <li>2024: PR</li>"
)
with open("athlete-bruno.html", "w") as f:
    f.write(athlete_html_bruno)

# Garrett Comer's page
athlete_html_garrett = athlete_template.render(
    athlete_name=garrett_name,
    athlete_grade=garrett_grade,
    athlete_school="Ann Arbor Skyline",
    season_year="2024",
    races_2024_table=garrett_races_table_2024,  # Now passing the races table
    all_records_table=garrett_table,
    season_notes="<li>2024: Best perf.</li>"
)
with open("athlete-garrett.html", "w") as f:
    f.write(athlete_html_garrett)

# Cole Harm's page
athlete_html_cole = athlete_template.render(
    athlete_name=cole_name,
    athlete_grade=cole_grade,
    athlete_school="Ann Arbor Skyline",
    season_year="2024",
    races_2024_table=cole_races_table_2024,  # Now passing the races table
    all_records_table=cole_table,
    season_notes="<li>2024: Best season</li>"
)
with open("athlete-cole.html", "w") as f:
    f.write(athlete_html_cole)

# Ethan Miller's page
athlete_html_ethan = athlete_template.render(
    athlete_name=ethan_name,
    athlete_grade=ethan_grade,
    athlete_school="Ann Arbor Skyline",
    season_year="2024",
    races_2024_table=ethan_races_table_2024,  # Now passing the races table
    all_records_table=ethan_table,
    season_notes="<li>2024: Coming Perf.</li>"
)
with open("athlete-ethan.html", "w") as f:
    f.write(athlete_html_ethan)

# Dylan Hanley's page
athlete_html_dylan = athlete_template.render(
    athlete_name=dylan_name,
    athlete_grade=dylan_grade,
    athlete_school="Ann Arbor Skyline",
    season_year="2024",
    races_2024_table=dylan_races_table_2024,  # Now passing the races table
    all_records_table=dylan_table,
    season_notes="<li>2024: Coming Perf.</li>"
)
with open("athlete-dylan.html", "w") as f:
    f.write(athlete_html_dylan)

# Gustaf Finn's page
athlete_html_gustaf = athlete_template.render(
    athlete_name=gustaf_name,
    athlete_grade=gustaf_grade,
    athlete_school="Ann Arbor Skyline",
    season_year="2024",
    races_2024_table=gustaf_races_table_2024,  # Now passing the races table
    all_records_table=gustaf_table,
    season_notes="<li>2024: Coming Perf.</li>"
)
with open("athlete-gustaf.html", "w") as f:
    f.write(athlete_html_gustaf)

# Emmett Strait's page
athlete_html_emmett = athlete_template.render(
    athlete_name=emmett_name,
    athlete_grade=emmett_grade,
    athlete_school="Ann Arbor Skyline",
    season_year="2024",
    races_2024_table=emmett_races_table_2024,  # Now passing the races table
    all_records_table=emmett_table,
    season_notes="<li>2024: Coming Perf.</li>"
)
with open("athlete-emmett.html", "w") as f:
    f.write(athlete_html_emmett)

# Enshu Kuan's page
athlete_html_enshu = athlete_template.render(
    athlete_name=enshu_name,
    athlete_grade=enshu_grade,
    athlete_school="Ann Arbor Skyline",
    season_year="2024",
    races_2024_table=enshu_races_table_2024,  # Now passing the races table
    all_records_table=enshu_table,
    season_notes="<li>2024: Coming Perf.</li>"
)
with open("athlete-enshu.html", "w") as f:
    f.write(athlete_html_enshu)



# Adrienne Stewart's page
athlete_html_adrienne = athlete_template.render(
    athlete_name=adrienne_name,
    athlete_grade=adrienne_grade,
    athlete_school="Ann Arbor Skyline",
    season_year="2024",
    races_2024_table=adrienne_races_table_2024,  # Now passing the races table
    all_records_table=adrienne_table,
    season_notes="<li>2024: Coming Perf.</li>"
)
with open("athlete-adrienne.html", "w") as f:
    f.write(athlete_html_adrienne)

# Alexandra Wren's page
athlete_html_alexandra = athlete_template.render(
    athlete_name=alexandra_name,
    athlete_grade=alexandra_grade,
    athlete_school="Ann Arbor Skyline",
    season_year="2024",
    races_2024_table=alexandra_races_table_2024,  # Now passing the races table
    all_records_table=alexandra_table,
    season_notes="<li>2024: Coming Perf.</li>"
)
with open("athlete-alexandra.html", "w") as f:
    f.write(athlete_html_alexandra)

# Alison Kauffman's page
athlete_html_alison = athlete_template.render(
    athlete_name=alison_name,
    athlete_grade=alison_grade,
    athlete_school="Ann Arbor Skyline",
    season_year="2024",
    races_2024_table=alison_races_table_2024,  # Now passing the races table
    all_records_table=alison_table,
    season_notes="<li>2024: Coming Perf.</li>"
)
with open("athlete-alison.html", "w") as f:
    f.write(athlete_html_alison)

# Ann Kececi's page
athlete_html_ann = athlete_template.render(
    athlete_name=ann_name,
    athlete_grade=ann_grade,
    athlete_school="Ann Arbor Skyline",
    season_year="2024",
    races_2024_table=ann_races_table_2024,  # Now passing the races table
    all_records_table=ann_table,
    season_notes="<li>2024: Coming Perf.</li>"
)
with open("athlete-ann.html", "w") as f:
    f.write(athlete_html_ann)

# Arabella Kessler's page
athlete_html_arabella = athlete_template.render(
    athlete_name=arabella_name,
    athlete_grade=arabella_grade,
    athlete_school="Ann Arbor Skyline",
    season_year="2024",
    races_2024_table=arabella_races_table_2024,  # Now passing the races table
    all_records_table=arabella_table,
    season_notes="<li>2024: Coming Perf.</li>"
)
with open("athlete-arabella.html", "w") as f:
    f.write(athlete_html_arabella)

# Calla Sopoci's page
athlete_html_calla = athlete_template.render(
    athlete_name=calla_name,
    athlete_grade=calla_grade,
    athlete_school="Ann Arbor Skyline",
    season_year="2024",
    races_2024_table=calla_races_table_2024,  # Now passing the races table
    all_records_table=calla_table,
    season_notes="<li>2024: Coming Perf.</li>"
)
with open("athlete-calla.html", "w") as f:
    f.write(athlete_html_calla)

# Elin Tenbrink's page
athlete_html_elin = athlete_template.render(
    athlete_name=elin_name,
    athlete_grade=elin_grade,
    athlete_school="Ann Arbor Skyline",
    season_year="2024",
    races_2024_table=elin_races_table_2024,  # Now passing the races table
    all_records_table=elin_table,
    season_notes="<li>2024: Coming Perf.</li>"
)
with open("athlete-elin.html", "w") as f:
    f.write(athlete_html_elin)

# Elsa Wenzlaff's page
athlete_html_elsa = athlete_template.render(
    athlete_name=elsa_name,
    athlete_grade=elsa_grade,
    athlete_school="Ann Arbor Skyline",
    season_year="2024",
    races_2024_table=elsa_races_table_2024,  # Now passing the races table
    all_records_table=elsa_table,
    season_notes="<li>2024: Coming Perf.</li>"
)
with open("athlete-elsa.html", "w") as f:
    f.write(athlete_html_elsa)

# Emily Mei's page
athlete_html_emily= athlete_template.render(
    athlete_name=emily_name,
    athlete_grade=emily_grade,
    athlete_school="Ann Arbor Skyline",
    season_year="2024",
    races_2024_table=emily_races_table_2024,  # Now passing the races table
    all_records_table=emily_table,
    season_notes="<li>2024: Coming Perf.</li>"
)
with open("athlete-emily.html", "w") as f:
    f.write(athlete_html_emily)

# Irie Scrase's page
athlete_html_irie = athlete_template.render(
    athlete_name=irie_name,
    athlete_grade=irie_grade,
    athlete_school="Ann Arbor Skyline",
    season_year="2024",
    races_2024_table=irie_races_table_2024,  # Now passing the races table
    all_records_table=irie_table,
    season_notes="<li>2024: Coming Perf.</li> <li>2025: Coming Perf.</li>"
)
with open("athlete-irie.html", "w") as f:
    f.write(athlete_html_irie)


