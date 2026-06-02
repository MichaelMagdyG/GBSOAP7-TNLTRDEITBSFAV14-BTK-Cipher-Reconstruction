import matplotlib.pyplot as plt


matrix = [
['P','I','A','N','O'],
['G','B','S','O','A'],
['P','T','N','L','T'],
['R','D','E','I','T'],
['B','S','F','A','V']
]

coords = [
(1,3),(2,5),(5,3),(2,2),(5,2),
(4,1),(4,2),(5,4),(2,1),(1,2),
(4,3),(3,4),(1,4),(3,3),(1,5),
(2,4),(1,1),(3,1),(2,3),(4,5),
(3,2),(3,5),(4,4),(5,5),(5,1)
]

colors = [
"#ef5350",
"#42a5f5",
"#66bb6a",
"#ffa726",
"#ab47bc"
]

fig, ax = plt.subplots(figsize=(9,9))

for idx,(r,c) in enumerate(coords):

    r-=1
    c-=1

    group = idx//5
    color = colors[group]

    rect = plt.Rectangle(
        (c-0.5,r-0.5),
        1,1,
        color=color,
        alpha=0.75
    )

    ax.add_patch(rect)

    ax.text(
        c,
        r,
        f"{matrix[r][c]}\n{idx+1}",
        ha='center',
        va='center',
        fontsize=12,
        color='white',
        fontweight='bold'
    )

    if idx < len(coords)-1:

        nr,nc = coords[idx+1]
        nr-=1
        nc-=1

        ax.arrow(
            c,
            r,
            nc-c,
            nr-r,
            length_includes_head=True,
            head_width=0.12,
            alpha=0.6
        )

ax.set_xlim(-0.5,4.5)
ax.set_ylim(4.5,-0.5)

ax.set_xticks(range(5))
ax.set_yticks(range(5))

ax.set_title("BTK Coordinate Traversal — Colored Groups")

plt.show()