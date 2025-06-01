#!/usr/bin/python3
"""
Weather Recommendation Program
Provides clothing advice based on weather conditions.
"""

def get_recommendation():
    weather = input("What's the weather? (sunny/rainy/cold): ").strip().lower()
    
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("Bring an umbrella and raincoat.")
    elif weather == "cold":
        print("Wear a warm coat and scarf.")
    else:
        print("No recommendations for this weather.")

if __name__ == "__main__":
    get_recommendation()
