# SPDX-License-Identifier: CC0-1.0
# SPDX-FileCopyrightText: 2025 Contributors to the CMS Knowledge Management Platform and Open Source Program Office
# This work is dedicated to the public domain under Creative Commons Zero 1.0 Universal

import matplotlib.pyplot as plt

import numpy as np


# Input variables
total_repositories = 10000
automated_percentage = 0.80
manual_time_minutes = 60  # Original manual time per repo
automated_time_minutes = 2  # Average automated processing time
manual_portion_time_minutes = 10  # Time for manual portion after automation
hourly_rate = 80  # Cost per hour
years_to_project = [1, 5, 10]


# Calculate time savings
def calculate_savings(repos, years):

    # Original manual process time (in hours)
    original_time = (repos * manual_time_minutes) / 60

    # New process time (in hours)
    automated_repos = repos * automated_percentage
    manual_repos = repos * (1 - automated_percentage)
    new_time = (automated_repos * automated_time_minutes + 
                manual_repos * manual_portion_time_minutes) / 60

    # Calculate savings for each year
    time_saved = [int((original_time - new_time) * year) for year in years]
    cost_saved = [int(t * hourly_rate) for t in time_saved]

    return time_saved, cost_saved


# Generate data
time_saved, cost_saved = calculate_savings(total_repositories, years_to_project)


# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3))


# Time Savings Plot
ax1.bar(years_to_project, time_saved, color='blue', alpha=0.6)
ax1.set_title('Time Saved by Period', fontsize=9)
ax1.set_xlabel('Years', fontsize=8)
ax1.set_ylabel('Hours Saved', fontsize=8)
ax1.grid(True, alpha=0.3)
ax1.tick_params(axis='both', which='major', labelsize=8)


# Cost Savings Plot
ax2.bar(years_to_project, cost_saved, color='green', alpha=0.6)
ax2.set_title('Cost Savings by Period', fontsize=9)
ax2.set_xlabel('Years', fontsize=8)
ax2.set_ylabel('Dollars Saved ($)', fontsize=8)
ax2.grid(True, alpha=0.3)
ax2.tick_params(axis='both', which='major', labelsize=8)
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1e6:.1f}M'))

plt.tight_layout()

# Save plots
plt.savefig('combined_savings_plots.png', dpi=300, bbox_inches='tight')

# Print calculated values
print("\nCalculated Savings:")

for i, year in enumerate(years_to_project):
    print(f"{year} Year(s): {time_saved[i]:,} hours (${cost_saved[i]:,})")
