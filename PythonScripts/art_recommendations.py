#!/usr/bin/env python3

"""
Personalized Art Recommendations Script

This script generates personalized art style recommendations based on user preferences.

Usage: ./art_recommendations.py
"""

import random

# Sample art styles and their descriptions
art_styles = {
    "Impressionism": "Capture the essence of a moment with bold brushstrokes and vibrant colors.",
    "Surrealism": "Explore the world of dreams and the subconscious with imaginative and bizarre imagery.",
    "Cubism": "Portray subjects from multiple perspectives with fragmented and geometric forms.",
    "Abstract Expressionism": "Convey emotions through abstract forms, colors, and textures.",
    "Pop Art": "Celebrate popular culture and consumerism with bold colors and iconic imagery."
}

def get_user_preferences():
    """Get user preferences for art styles."""
    print("Welcome to Personalized Art Recommendations!")
    print("Please rate the following art styles from 1 (not interested) to 5 (very interested):")
    
    user_preferences = {}
    for style, description in art_styles.items():
        rating = input(f"How interested are you in {style}? (1-5): ")
        while not rating.isdigit() or int(rating) < 1 or int(rating) > 5:
            rating = input("Please enter a valid rating between 1 and 5: ")
        user_preferences[style] = int(rating)
    
    return user_preferences

def generate_recommendations(user_preferences):
    """Generate personalized art style recommendations."""
    sorted_preferences = sorted(user_preferences.items(), key=lambda x: x[1], reverse=True)
    
    print("\nBased on your preferences, we recommend the following art styles:")
    for style, _ in sorted_preferences:
        print(f"{style}: {art_styles[style]}")

    top_recommendation = sorted_preferences[0][0]
    print(f"\nYou might especially enjoy the '{top_recommendation}' style!")

if __name__ == '__main__':
    user_preferences = get_user_preferences()
    generate_recommendations(user_preferences)
