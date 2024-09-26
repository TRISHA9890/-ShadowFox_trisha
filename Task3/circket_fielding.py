

import pandas as pd
import csv

# Sample fielding data for multiple players
data = {
    'Match No.': [1, 1, 1, 1],
    'Innings': [1, 1, 1, 1],
    'Team': ['Team A', 'Team A', 'Team A', 'Team A'],
    'Player Name': ['Player 1', 'Player 1', 'Player 2', 'Player 3'],
    'Ball Count': [1, 2, 3, 4],
    'Position': ['Point', 'Cover', 'Mid-off', 'Square Leg'],
    'Short Description': ['Clean pickup', 'Good throw', 'Dropped catch', 'Direct hit'],
    'Pick': ['Clean Pick', 'Good Throw', 'Drop Catch', 'Clean Pick'],
    'Throw': ['Run Out', 'Missed Run Out', 'N/A', 'Stumping'],
    'Runs': [2, -1, -4, 1],
    'Over Count': [1, 1, 1, 1],
    'Venue': ['Stadium A', 'Stadium A', 'Stadium A', 'Stadium A']
}

# Convert the dictionary into a pandas DataFrame
df = pd.DataFrame(data)

# Define the weights for the performance metrics
weights = {
    'CP': 2,     # Clean Picks
    'GT': 1.5,   # Good Throws
    'C': 3,      # Catches
    'DC': -2,    # Dropped Catches
    'ST': 3,     # Stumpings
    'RO': 4,     # Run Outs
    'MRO': -3,   # Missed Run Outs
    'DH': 3,     # Direct Hits
    'RS': 1      # Runs Saved (positive for saved, negative for conceded)
}

# Function to calculate the performance score for each row/player
def calculate_performance_score(row):
    score = 0  # Initialize the performance score

    # Calculate the score based on fielding actions
    if row['Pick'] == 'Clean Pick':
        score += weights['CP']
    if row['Pick'] == 'Good Throw':
        score += weights['GT']
    if row['Pick'] == 'Drop Catch':
        score += weights['DC']
    if row['Throw'] == 'Run Out':
        score += weights['RO']
    if row['Throw'] == 'Missed Run Out':
        score += weights['MRO']
    if row['Throw'] == 'Stumping':
        score += weights['ST']
    if row['Short Description'] == 'Direct hit':  # Direct hit in Short Description
        score += weights['DH']
    
    # Add runs saved or conceded
    score += row['Runs'] * weights['RS']
    
    return score

# Apply the function to each row in the DataFrame
df['Performance Score'] = df.apply(calculate_performance_score, axis=1)

# Display the DataFrame with the performance score added
print(df)

# Export the updated DataFrame with performance scores to a CSV file
df.to_csv('fielding_performance.csv', index=False)

print("Fielding performance data has been exported to 'fielding_performance.csv'.")
