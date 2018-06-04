import requests


def get_prices_history():
    labels = ["January", "February", "March",
              "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return {
        'labels': labels,
        'values': values
    }
