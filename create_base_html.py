import get_stops

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>all stops...</title>
</head>
<body>
<select id="bus-stops" onchange="selectStop()">
    <option value="">select a stop...</option>
"""

for stop in get_stops.all_stops:
    url, name = stop
    html_content += f'    <option value="{url}">{name}</option>\n'

html_content += """
</select>
<script>
function selectStop() {
    var dropdown = document.getElementById("bus-stops");
    var selectedUrl = dropdown.value;
    if (selectedUrl) {
        console.log("Selected URL:", selectedUrl);
        // Further actions with selectedUrl can be added here
    }
}
</script>
</body>
</html>
"""

with open("index.html", "w") as file:
    file.write(html_content)

print("file has been created...")
