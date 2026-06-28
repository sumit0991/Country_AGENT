import requests

def get_country_info(query):
    """
    Uses REST Countries API
    """
    try:
        words = query.lower().split()

        country_name = words[-1]  # simple extraction

        url = f"https://restcountries.com/v3.1/name/{country_name}"

        response = requests.get(url)
        data = response.json()[0]

        info = {
            "name": data["name"]["common"],
            "capital": data.get("capital", ["N/A"])[0],
            "currency": list(data.get("currencies", {}).keys())[0] if data.get("currencies") else "N/A",
            "population": data.get("population", "N/A"),
            "language": list(data.get("languages", {}).values())[0] if data.get("languages") else "N/A",
            "continent": data.get("continents", ["N/A"])[0]
        }

        return str(info)

    except Exception as e:
        return f"Error fetching country data: {str(e)}"