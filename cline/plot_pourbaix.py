import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Data from CSV (approximate boundaries)
data = """pH,Potential,Species
0,-1.5,Zn
0,0,Zn
0,2,ZnO2
6,2,ZnO2
6,0,Zn2+
6,-1,Zn2+
6,-1.5,Zn
8,-1.5,Zn
8,-1,Zn2+
8,0,Zn2+
8,0.2,ZnOH+
8,0.7,ZnOH+
8,0.7,ZnO2
8,2,ZnO2
10,2,ZnO2
10,0.7,ZnO2
10,0.2,ZnO
10,-0.8,ZnO
10,-1,HZnO2-
10,-1.5,HZnO2-
12,-1.5,HZnO2-
12,-1,HZnO2-
12,-0.8,ZnO2--
12,0.2,ZnO2--
12,0.7,ZnO2--
12,2,ZnO2
14,2,ZnO2
14,0.7,ZnO2--
14,0.2,ZnO2--
14,-1,ZnO2--
14,-1.5,ZnO2--
16,-1.5,ZnO2--
16,-1,ZnO2--
16,0.2,ZnO2--
16,0.7,ZnO2--
16,2,ZnO2
2,-2,Zn
2,2,ZnO2
4,-2,Zn
4,2,ZnO2
"""

from io import StringIO
df = pd.read_csv(StringIO(data))

# Create the plot
plt.figure(figsize=(8, 6))
plt.xlabel('pH at 25 °C')
plt.ylabel('Potential (V vs SHE)')
plt.title('Pourbaix Diagram for Zinc')
plt.xlim(0, 16)
plt.ylim(-3, 3)

# Define regions and colors (approximate - needs refinement for exact match)
regions = {
    'Zn': {'color': 'lightgrey', 'points': [(0, -3), (0, 0), (6, -1.5), (8, -1.5), (16, -1.5), (16, -3)]},
    'Zn2+': {'color': 'lightblue', 'points': [(6, 0), (6, 2), (8, 2), (8, 0), (6, 0)]},
    'ZnO': {'color': 'lightgreen', 'points': [(10, 0.2), (10, 0.7), (12, 0.7), (12, 0.2), (10, 0.2)]},
    'ZnO2': {'color': 'yellow', 'points': [(0, 2), (6, 2), (8, 2), (10, 2), (12, 2), (14, 2), (16, 2), (16, 3), (0, 3)]},
    'ZnOH+': {'color': 'lightsalmon', 'points': [(8, 0.2), (8, 0.7), (10, 0.7), (10, 0.2), (8, 0.2)]},
    'HZnO2-': {'color': 'plum', 'points': [(10, -1), (10, -0.8), (12, -0.8), (12, -1), (10, -1)]},
    'ZnO2--': {'color': 'lavender', 'points': [(12, -0.8), (12, 0.2), (14, 0.2), (14, -1), (16, -1), (16, -0.8), (12, -0.8)]}
}

# Plot regions
for region_name, region_data in regions.items():
    polygon = patches.Polygon(region_data['points'], closed=True, facecolor=region_data['color'], edgecolor='black', linewidth=0.5, alpha=0.7)
    plt.gca().add_patch(polygon)

# Plot boundary lines (approximate - needs refinement for exact match)
plt.plot([0, 16], [2, 2], 'k--', linewidth=0.8) # H2O/O2
plt.plot([0, 16], [-1, -1], 'k--', linewidth=0.8) # H2O/H2
plt.plot([8, 8], [-1, 0.7], 'k--', linewidth=0.8) # Zn2+/ZnOH+ and ZnOH+/ZnO2
plt.plot([10, 10], [-1, 0.7], 'k--', linewidth=0.8) # ZnO/HZnO2- and ZnO/ZnO2

# Add region labels (approximate positions)
plt.text(3, -2.2, 'Zn', ha='center', va='center')
plt.text(3, 1, 'ZnO2', ha='center', va='center')
plt.text(7, -0.5, 'Zn2+', ha='center', va='center')
plt.text(9, 0.5, 'ZnOH+', ha='center', va='center')
plt.text(11, -0.3, 'ZnO', ha='center', va='center')
plt.text(11, -1.2, 'HZnO2-', ha='center', va='center')
plt.text(14, -0.5, 'ZnO2--', ha='center', va='center')


plt.axvline(x=0, color='k', linewidth=0.5)
plt.axhline(y=0, color='k', linewidth=0.5)

plt.savefig('vscode learn/cline/pourbaix_diagram.png', dpi=300, bbox_inches='tight')
plt.show()
