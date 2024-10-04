import random
import string

# Function to generate a random password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Function to check for flagged keywords in posts
def check_flagged_keywords(posts):
    flagged_keywords = ["danger", "attack", "threat", "bomb", "weapon"]
    count = 0
    for post in posts:
        for keyword in flagged_keywords:
            if keyword in post.lower():
                count += 1
    return count

# Function to calculate the distance between two coordinates
def calculate_distance(coord1, coord2):
    from geopy.distance import geodesic
    return geodesic(coord1, coord2).kilometers

# Function to check proximity to sensitive location
def is_near_sensitive_location(current_location, sensitive_location, threshold_distance):
    distance = calculate_distance(current_location, sensitive_location)
    return distance <= threshold_distance

# Example usage
posts = [
    "There is a threat in the area",
    "Just a normal day",
    "Heard about a bomb threat nearby"
]

current_location = (35.6895, 139.6917)  # Example coordinates (Tokyo)
sensitive_location = (35.6586, 139.7454)  # Example coordinates (Tokyo Tower)
threshold_distance = 5.0  # Example threshold distance in kilometers

# Check for flagged keywords
flagged_count = check_flagged_keywords(posts)

# Check proximity to sensitive location
near_sensitive_location = is_near_sensitive_location(current_location, sensitive_location, threshold_distance)

# Determine if activities are high risk
high_risk = flagged_count > 1 and near_sensitive_location

print("High Risk Activities:", high_risk)

