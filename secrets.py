try:
    # Try to import credentials from secrets_local.py (not tracked by git)
    from secrets_local import WIFI_SSID, WIFI_PASSWORD
except ImportError:
    # Fallback if secrets_local.py doesn't exist
    WIFI_SSID = "your_ssid_here"
    WIFI_PASSWORD = "your_password_here"

secrets = {
    "ssid": WIFI_SSID,
    "password": WIFI_PASSWORD,
    # area to search for flights: top latitude, bottom latitude, left longitude, right longitude
    # (so this example is greater London)
    # "bounds_box": "51.692,51.287,-0.510,0.334",
    # my house
    "bounds_box" : "51.6,51.4,-0.3,-0.1"
}
