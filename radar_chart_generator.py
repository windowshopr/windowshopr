from turtle import fillcolor
import plotly.express as px
from pandas import DataFrame

# # Programming Languages
# data = {"r": [3, 3, 3, 2, 3, 2],
#         "theta": ['Python', 'Java', 'VBA', 'C#', 'C++', 'C']}

# df = DataFrame(data)
# fig = px.line_polar(df, r='r', theta='theta', line_close=True, markers=True, range_r=(0,3))
# fig.update_traces(fill='toself')

# fig.update_layout(
#     font=dict(
#         family="Calibri",
#         size=24,  # Set the font size here
#         color="Black",
#     ),
#     title={
#         'text': "Programming Languages",
#         'y':0.6,
#         'x':0.5,
#         'xanchor': 'center',
#         'yanchor': 'top'}
# )

# fig.layout.polar.radialaxis.tickvals = [0,1,2,3]

# fig.write_html("graphs/programming_languages.html")
# fig.show()



















# # Web Development
# data = {"r": [3, 3, 3, 3, 2, 1],
#         "theta": ['HTML/CSS/JS', 'Node.js', 'Flask', 'Django', 'Vue', 'React']}

# df = DataFrame(data)
# fig = px.line_polar(df, r='r', theta='theta', line_close=True, markers=True, range_r=(0,3))
# fig.update_traces(fill='toself', fillcolor='green', opacity=0.5)

# fig.update_layout(
#     font=dict(
#         family="Calibri",
#         size=24,  # Set the font size here
#         color="Black",
#     ),
#     title={
#         'text': "Web Development",
#         'y':0.6,
#         'x':0.5,
#         'xanchor': 'center',
#         'yanchor': 'top'}
# )

# fig.layout.polar.radialaxis.tickvals = [0,1,2,3]

# fig.write_html("graphs/web_development.html")
# fig.show()
























# # Databases
# data = {"r": [3, 3, 3, 3, 1],
#         "theta": ['MySQL', 'SQL', 'SQLite', 'Oracle', 'MongoDB']}

# df = DataFrame(data)
# fig = px.line_polar(df, r='r', theta='theta', line_close=True, markers=True, range_r=(0,3))
# fig.update_traces(fill='toself', fillcolor='yellow', opacity=0.5)

# fig.update_layout(
#     font=dict(
#         family="Calibri",
#         size=24,  # Set the font size here
#         color="Black",
#     ),
#     title={
#         'text': "DBMS's",
#         'y':0.6,
#         'x':0.5,
#         'xanchor': 'center',
#         'yanchor': 'top'}
# )

# fig.layout.polar.radialaxis.tickvals = [0,1,2,3]

# fig.write_html("graphs/databases.html")
# fig.show()






















# # Mobile Development
# data = {"r": [2, 3, 3, 2, 3, 3],
#         "theta": ['Flutter', 'Xamarin', 'Android Studio', 'C#', 'Java', 'Swift']}

# df = DataFrame(data)
# fig = px.line_polar(df, r='r', theta='theta', line_close=True, markers=True, range_r=(0,3))
# fig.update_traces(fill='toself', fillcolor='red', opacity=0.5)

# fig.update_layout(
#     font=dict(
#         family="Calibri",
#         size=24,  # Set the font size here
#         color="Black",
#     ),
#     title={
#         'text': "Mobile App Development",
#         'y':0.6,
#         'x':0.5,
#         'xanchor': 'center',
#         'yanchor': 'top'}
# )

# fig.layout.polar.radialaxis.tickvals = [0,1,2,3]

# fig.write_html("graphs/mobile_dev.html")
# fig.show()



























# # Machine Learning
# data = {"r": [3, 3, 3, 3, 3, 2],
#         "theta": ['Tensorflow', 'Scikit Learn', 'Keras', 'Reinforcement Learning', 'Classification/Regression', 'Computer Vision']}

# df = DataFrame(data)
# fig = px.line_polar(df, r='r', theta='theta', line_close=True, markers=True, range_r=(0,3))
# fig.update_traces(fill='toself', fillcolor='purple', opacity=0.5)

# fig.update_layout(
#     font=dict(
#         family="Calibri",
#         size=24,  # Set the font size here
#         color="Black",
#     ),
#     title={
#         'text': "Machine Learning",
#         'y':0.6,
#         'x':0.5,
#         'xanchor': 'center',
#         'yanchor': 'top'}
# )

# fig.layout.polar.radialaxis.tickvals = [0,1,2,3]

# fig.write_html("graphs/machine_learning.html")
# fig.show()
































# Data Science
data = {"r": [3, 3, 3, 3, 3, 3, 3],
        "theta": ['Pandas', 'Numpy', 'SciPy', 'Genetic Algorithms', 'EDA', 'Visualization', 'Feature Eng./Sel.']}

df = DataFrame(data)
fig = px.line_polar(df, r='r', theta='theta', line_close=True, markers=True, range_r=(0,3))
fig.update_traces(fill='toself', fillcolor='pink', opacity=0.5)

fig.update_layout(
    font=dict(
        family="Calibri",
        size=24,  # Set the font size here
        color="Black",
    ),
    title={
        'text': "Data Science",
        'y':0.6,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
)

fig.layout.polar.radialaxis.tickvals = [0,1,2,3]

fig.write_html("graphs/data_science.html")
fig.show()


























# # Finance
# data = {"r": [3, 3, 2, 3, 3, 2, 3, 3, 3],
#         "theta": ['Day Trading', 'Technical Analysis', 'Fundamental Analysis', 'Screeners', 'Backtesting', 'Portfolio Optimization', 'MetaTrader', 'TradingView/Pine Script', 'ToS/ThinkScript']}

# df = DataFrame(data)
# fig = px.line_polar(df, r='r', theta='theta', line_close=True, markers=True, range_r=(0,3))
# fig.update_traces(fill='toself', fillcolor='grey', opacity=0.5)

# fig.update_layout(
#     font=dict(
#         family="Calibri",
#         size=24,  # Set the font size here
#         color="Black",
#     ),
#     title={
#         'text': "Finance",
#         'y':0.6,
#         'x':0.5,
#         'xanchor': 'center',
#         'yanchor': 'top'}
# )

# fig.layout.polar.radialaxis.tickvals = [0,1,2,3]

# fig.write_html("graphs/finance.html")
# fig.show()




























# # Multimedia
# data = {"r": [3, 2, 2, 3, 3],
#         "theta": ['Adobe Photoshop', 'Adobe After Effects', 'Filmora Wondershare', 'DrawIO', 'Visio']}

# df = DataFrame(data)
# fig = px.line_polar(df, r='r', theta='theta', line_close=True, markers=True, range_r=(0,3))
# fig.update_traces(fill='toself', fillcolor='black', opacity=0.5)

# fig.update_layout(
#     font=dict(
#         family="Calibri",
#         size=24,  # Set the font size here
#         color="Black",
#     ),
#     title={
#         'text': "Multimedia and Design",
#         'y':0.6,
#         'x':0.5,
#         'xanchor': 'center',
#         'yanchor': 'top'}
# )

# fig.layout.polar.radialaxis.tickvals = [0,1,2,3]

# fig.write_html("graphs/multimedia.html")
# fig.show()

























# # Misc
# data = {"r": [3, 2, 1, 2, 3, 2],
#         "theta": ['GitHub', 'GitLab', 'BitBucket', 'Dynamics365', 'Bash/Shell/Batch Scripting', 'Azure Cloud']}

# df = DataFrame(data)
# fig = px.line_polar(df, r='r', theta='theta', line_close=True, markers=True, range_r=(0,3))
# fig.update_traces(fill='toself', fillcolor='orange', opacity=0.5)

# fig.update_layout(
#     font=dict(
#         family="Calibri",
#         size=24,  # Set the font size here
#         color="Black",
#     ),
#     title={
#         'text': "Miscellaneous",
#         'y':0.6,
#         'x':0.5,
#         'xanchor': 'center',
#         'yanchor': 'top'}
# )

# fig.layout.polar.radialaxis.tickvals = [0,1,2,3]

# fig.write_html("graphs/misc.html")
# fig.show()