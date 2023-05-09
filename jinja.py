import jinja2
import folium 
# Other imports and your code

def create_map(column, html_file):
    cp_map = folium.Map(location=[55.678086, 12.568827], zoom_start=12)
    # Your existing code
    cp_map.save(html_file)

options = ['belaegning_kl_12_pct', 'belaegning_kl_17_pct', 'belaegning_kl_22_pct']
html_file_prefix = 'map'

# Save separate maps for each time option
for option in options:
    html_file = f"{html_file_prefix}_{option}.html"
    create_map(option, html_file)

# Render the final HTML file with Jinja2
template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template("map_template.html")

output_path = "map_with_dropdown.html"
with open(output_path, "w") as output_file:
    output_file.write(
        template.render(
            dropdown_options=options,
            selected_option=options[0],
            html_file=f"{html_file_prefix}_{options[0]}.html"
        )
    )
