# Simple Python Weather App

from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}


def weather(city):
    city = city.replace(" ", "+")
    x = requests.get(
        "https://www.google.com/search?q={}&oq={}+&aqs=chrome..69i59j69i57j69i59j35i39j46i131i433j69i61j69i60l2.5676j1j7&sourceid=chrome&ie=UTF-8".format(
            city, city
        ),
        headers=headers,
    )
    # x = request.get("https://www.google.com/search?q=montreal+weather&sxsrf=ALeKk03iMHO0_aE-qAreTfGkvESD7HOA7g%3A1621713013272&ei=dWCpYJ6KEMmvggeg6Y74AQ&oq=montreal+weather&gs_lcp=Cgdnd3Mtd2l6EAMyDAgjECcQnQIQRhCAAjIICAAQsQMQgwEyCAgAELEDEIMBMgsIABCxAxCDARDJAzIFCAAQkgMyAggAMgIIADICCAAyAggAMgIIADoHCCMQsAMQJzoHCAAQRxCwAzoKCC4QsAMQyAMQQzoHCCMQJxCdAjoLCC4QsQMQxwEQrwE6AgguSgUIOBIBMVD9zSlYpdUpYPnWKWgBcAJ4AYABnASIAZIJkgEHNy4xLjUtMZgBAKABAaoBB2d3cy13aXrIAQ_AAQE&sclient=gws-wiz&ved=0ahUKEwjemNXgh97wAhXJl-AKHaC0Ax8Q4dUDCA4&uact=5")
    print("searching....")
    soup = BeautifulSoup(x.text, "html.parser")
    location = soup.select("#wob_loc")[0].getText().strip()
    time = soup.select("#wob_dts")[0].getText().strip()
    info = soup.select("#wob_dc")[0].getText().strip()
    weather = soup.select("#wob_tm")[0].getText().strip()
    print(location)
    print(time)
    print(info)
    print(weather + "°C")


city = input("Enter the city Name\n")
city = city + " weather"
weather(city)
