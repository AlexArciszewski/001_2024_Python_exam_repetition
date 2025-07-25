from typing import Tuple, List
import datetime as dt
import requests
import smtplib
import time


class ISSNotifier:
    def __init__(self, my_lat: float, my_long: float, email: str, password: str, recipient: str):
        self.my_lat = my_lat
        self.my_long = my_long
        self.email = email
        self.password = password
        self.recipient = recipient

    def get_current_time(self) -> Tuple[int, int]:
        """Return current local hour and minute."""
        now = dt.datetime.now()
        print(f"Current time: {now.hour}:{now.minute}")
        return now.hour, now.minute

    def get_sun_times(self) -> List[Tuple[str, str]]:
        """Get sunrise and sunset time based on current coordinates."""
        parameters = {
            "lat": self.my_lat,
            "lng": self.my_long,
            "formatted": 0,
        }

        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()

        sunrise = data['results']['sunrise'].split("T")[1].split("+")[0].split(":")
        sunset = data['results']['sunset'].split("T")[1].split("+")[0].split(":")

        sunrise_tuple = (sunrise[0], sunrise[1])
        sunset_tuple = (sunset[0], sunset[1])

        print(f"Sunrise at: {sunrise_tuple}, Sunset at: {sunset_tuple}")
        return [sunset_tuple, sunrise_tuple]

    def get_iss_location(self) -> Tuple[float, float]:
        """Fetch the current ISS location."""
        response = requests.get("http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()
        latitude = float(data["iss_position"]["latitude"])
        longitude = float(data["iss_position"]["longitude"])
        print(f"ISS location: ({latitude}, {longitude})")
        return latitude, longitude

    def is_night(self, current_time: Tuple[int, int], sun_times: List[Tuple[str, str]]) -> bool:
        """Check if it's currently night based on sunrise/sunset data."""
        hour_now = current_time[0]
        sunset_hour = int(sun_times[0][0])
        sunrise_hour = int(sun_times[1][0])

        if hour_now >= sunset_hour or hour_now <= sunrise_hour:
            print("It's night. You might see the ISS.")
            return True
        else:
            print("It's day. Too bright to see the ISS.")
            return False

    def is_iss_nearby(self, iss_location: Tuple[float, float]) -> bool:
        """Check if ISS is within 5 degrees lat/long."""
        iss_lat, iss_long = iss_location
        lat_diff = abs(self.my_lat - iss_lat)
        long_diff = abs(self.my_long - iss_long)
        if lat_diff <= 5 and long_diff <= 5:
            print("The ISS is close.")
            return True
        else:
            print("The ISS is too far away.")
            return False

    def send_notification(self) -> None:
        """Send an email notification."""
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.sendmail(
                from_addr=self.email,
                to_addrs=self.recipient,
                msg="Subject:ISS location info\n\nGo outside and watch the sky!"
            )
        print("Notification sent.")

    def run(self, interval: int = 180) -> None:
        """Main loop to check conditions and notify."""
        while True:
            try:
                current_time = self.get_current_time()
                sun_times = self.get_sun_times()
                iss_loc = self.get_iss_location()

                if self.is_night(current_time, sun_times) and self.is_iss_nearby(iss_loc):
                    self.send_notification()
                    print(f"Waiting {interval} seconds before next check...")
                    time.sleep(interval)
                else:
                    print(f"Conditions not met. Retrying in {interval} seconds...")
                    time.sleep(interval)
            except Exception as e:
                print(f"An error occurred: {e}")
                time.sleep(interval)


if __name__ == "__main__":
    notifier = ISSNotifier(
        my_lat=52.248421,
        my_long=21.172608,
        email="aaleksandro123@gmail.com",
        password="xxxxxxxxxxxx",  # 👈 UWAGA: Nigdy nie trzymaj haseł w kodzie! Użyj zmiennych środowiskowych!
        recipient="aleksanderarciszewski@yahoo.com"
    )
    notifier.run()