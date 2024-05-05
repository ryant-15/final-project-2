"""
Final Project
CS 230
London Pubs Data set
Ryan Trottier

Description: This stream lit page shows the amount of pubs by town in a bar chart, a heat map of the pubs, an interactive map that shows the name and address of the pubs, and two rating pie charts
"""
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import pydeck as pdk
import numpy as np

df_pubs = pd.read_csv("open_pubs.csv")
np.random.seed(42)
df_pubs["rating"] = np.random.randint(1, 101, df_pubs.shape[0])
df_pubs["safety_rating"] = np.random.randint(1, 51, df_pubs.shape[0])

df_p1 = df_pubs.set_index("local_authority")

df_p2 = df_p1.loc[:,"name"]


st.title("London Pubs Final Project")
st.image("C:/Users/ryant/PycharmProjects/pythonProject/london_p1.jpg", width=500)

bar_count = df_pubs["local_authority"].value_counts()

pub_select = st.multiselect("Pick the towns you want to be shown on the graph:", {"Bedford", "Braintree", "Central Bedfordshire", "Breckland", "Babergh", "Brentwood", "Cambridge", "Broadland", "Basildon", "Broxbourne", "Castle Point" })
if pub_select == []:
    bar_count.plot(kind="bar")
else:
    bar_count[pub_select].plot(kind= "bar")
plt.xlabel("Town")
plt.ylabel("Amount of Pubs")
plt.title("Amount of Pubs in each Town")
st.pyplot()
st.set_option("deprecation.showPyplotGlobalUse", False)

st.title("London Pubs Map Heat Map")

df_p3 = df_pubs.rename(columns={"latitude":"lat", "longitude": "lon"})
df_p3["lat"] = pd.to_numeric(df_p3["lat"], errors="coerce")
df_p3["lon"] = pd.to_numeric(df_p3["lon"], errors="coerce")
df_p4 = df_p3.dropna()
df_p5 = df_p4.set_index("local_authority")
selected_map = st.sidebar.radio("Please select a heat map:", [ "All Towns", "Bedford", "Braintree", "Central Bedfordshire", "Breckland", "Babergh", "Brentwood", "Cambridge", "Broadland", "Basildon", "Broxbourne", "Castle Point"])

if selected_map == "All Towns":
    layer = pdk.Layer(
        "ScatterplotLayer", #I used AI to help me with changing the background and removing N/A from the dataseries
        df_p5,
        get_position=["lon", "lat"],
        get_radius=200,
        get_color=[255, 0, 0, 160],

    )

    # Define the view state
    view_state = pdk.ViewState(
        latitude=df_p5["lat"].mean(),
        longitude=df_p5["lon"].mean(),
        zoom= 8,
        pitch= 0
    )

    # Create the pydeck chart
    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/dark-v10",
        initial_view_state=view_state,
        layers=[layer]
    ))
elif selected_map == "Bedford":
    layer = pdk.Layer(
        "ScatterplotLayer",
        df_p5.loc["Bedford"],
        get_position=["lon", "lat"],
        get_radius=200,
        get_color=[255, 0, 0, 160],

    )

    # Define the view state
    view_state = pdk.ViewState(
        latitude=df_p5["lat"].mean(),
        longitude=df_p5["lon"].mean(),
        zoom=8,
        pitch=0
    )

    # Create the pydeck chart
    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/dark-v10",
        initial_view_state=view_state,
        layers=[layer]
    ))
elif selected_map == "Braintree":
    layer = pdk.Layer(
        "ScatterplotLayer",
        df_p5.loc["Braintree"],
        get_position=["lon", "lat"],
        get_radius=200,
        get_color=[255, 0, 0, 160],

    )


    view_state = pdk.ViewState(
        latitude=df_p5["lat"].mean(),
        longitude=df_p5["lon"].mean(),
        zoom=8,
        pitch=0
    )


    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/dark-v10",
        initial_view_state=view_state,
        layers=[layer]
    ))
elif selected_map == "Central Bedfordshire":
    layer = pdk.Layer(
        "ScatterplotLayer",
        df_p5.loc["Central Bedfordshire"],
        get_position=["lon", "lat"],
        get_radius=200,
        get_color=[255, 0, 0, 160],

    )

    view_state = pdk.ViewState(
        latitude=df_p5["lat"].mean(),
        longitude=df_p5["lon"].mean(),
        zoom=8,
        pitch=0
    )

    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/dark-v10",
        initial_view_state=view_state,
        layers=[layer],

    ))

elif selected_map == "Breckland":
    layer = pdk.Layer(
        "ScatterplotLayer",
        df_p5.loc["Breckland"],
        get_position=["lon", "lat"],
        get_radius=200,
        get_color=[255, 0, 0, 160],

    )

    view_state = pdk.ViewState(
        latitude=df_p5["lat"].mean(),
        longitude=df_p5["lon"].mean(),
        zoom=8,
        pitch=0
    )

    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/dark-v10",
        initial_view_state=view_state,
        layers=[layer]
    ))

elif selected_map == "Babergh":
    layer = pdk.Layer(
        "ScatterplotLayer",
        df_p5.loc["Babergh"],
        get_position=["lon", "lat"],
        get_radius=200,
        get_color=[255, 0, 0, 160],

    )

    view_state = pdk.ViewState(
        latitude=df_p5["lat"].mean(),
        longitude=df_p5["lon"].mean(),
        zoom=8,
        pitch=0
    )

    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/dark-v10",
        initial_view_state=view_state,
        layers=[layer]
    ))

elif selected_map == "Brentwood":
    layer = pdk.Layer(
        "ScatterplotLayer",
        df_p5.loc["Brentwood"],
        get_position=["lon", "lat"],
        get_radius=200,
        get_color=[255, 0, 0, 160],

    )

    view_state = pdk.ViewState(
        latitude=df_p5["lat"].mean(),
        longitude=df_p5["lon"].mean(),
        zoom=8,
        pitch=0
    )

    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/dark-v10",
        initial_view_state=view_state,
        layers=[layer]
    ))

elif selected_map == "Cambridge":
    layer = pdk.Layer(
        "ScatterplotLayer",
        df_p5.loc["Cambridge"],
        get_position=["lon", "lat"],
        get_radius=200,
        get_color=[255, 0, 0, 160],

    )

    view_state = pdk.ViewState(
        latitude=df_p5["lat"].mean(),
        longitude=df_p5["lon"].mean(),
        zoom=8,
        pitch=0
    )

    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/dark-v10",
        initial_view_state=view_state,
        layers=[layer]
    ))

elif selected_map == "Broadland":
    layer = pdk.Layer(
        "ScatterplotLayer",
        df_p5.loc["Broadland"],
        get_position=["lon", "lat"],
        get_radius=200,
        get_color=[255, 0, 0, 160],

    )

    view_state = pdk.ViewState(
        latitude=df_p5["lat"].mean(),
        longitude=df_p5["lon"].mean(),
        zoom=8,
        pitch=0
    )

    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/dark-v10",
        initial_view_state=view_state,
        layers=[layer]
    ))

elif selected_map == "Basildon":
    layer = pdk.Layer(
        "ScatterplotLayer",
        df_p5.loc["Basildon"],
        get_position=["lon", "lat"],
        get_radius=200,
        get_color=[255, 0, 0, 160],

    )

    view_state = pdk.ViewState(
        latitude=df_p5["lat"].mean(),
        longitude=df_p5["lon"].mean(),
        zoom=8,
        pitch=0
    )

    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/dark-v10",
        initial_view_state=view_state,
        layers=[layer]
    ))

elif selected_map == "Broxbourne":
    layer = pdk.Layer(
        "ScatterplotLayer",
        df_p5.loc["Broxbourne"],
        get_position=["lon", "lat"],
        get_radius=200,
        get_color=[255, 0, 0, 160],

    )

    view_state = pdk.ViewState(
        latitude=df_p5["lat"].mean(),
        longitude=df_p5["lon"].mean(),
        zoom=8,
        pitch=0
    )

    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/dark-v10",
        initial_view_state=view_state,
        layers=[layer]
    ))

elif selected_map == "Castle Point":
    layer = pdk.Layer(
        "ScatterplotLayer",
        df_p5.loc["Castle Point"],
        get_position=["lon", "lat"],
        get_radius=200,
        get_color=[255, 0, 0, 160],

    )

    view_state = pdk.ViewState(
        latitude=df_p5["lat"].mean(),
        longitude=df_p5["lon"].mean(),
        zoom=8,
        pitch=0
    )

    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/dark-v10",
        initial_view_state=view_state,
        layers=[layer],
    ))

st.title("London Pubs Interactive Map")

layer = pdk.Layer(
    "ScatterplotLayer",
    df_p5,
    get_position=["lon", "lat"],
    get_radius=100,
    get_color=[128, 0, 128],
    pickable=True

)

view_state = pdk.ViewState(
    latitude=df_p5["lat"].mean(),
    longitude=df_p5["lon"].mean(),
    zoom=8,
    pitch=0
)

st.pydeck_chart(pdk.Deck(
    map_style="light",
    initial_view_state=view_state,
    layers=[layer],
    tooltip = {
        "html": "<b>Pub Name:</b> {name}<br><b>Address:</b> {address}",
            "style": { "backgroundColor": "purple",
                        "color": "white"
                       }
    }

))
st.title("Towns with the highest rated Pubs")
top_5_pubs = df_pubs.sort_values(by='rating', ascending=False).head(20)
highly_rated_pubs = top_5_pubs["local_authority"].value_counts()
highly_rated_pubs.plot(kind= "pie", autopct= "%.1f%%")
plt.ylabel("")
plt.title("Top 20 Rated pubs distribution")
st.pyplot()

highest_rated_pubs = df_pubs[df_pubs["rating"] == 100]
pub_100 = highest_rated_pubs["name"].tolist()
town_100 = highest_rated_pubs["local_authority"].tolist()
print(town_100)
st.write("The Pubs with the 100 ratings are:")
for i, x in zip(pub_100, town_100):
    st.write(f"{i}, {x}")

st.title("Towns with the best safety rated Pubs")
top_5_safety_pubs = df_pubs.sort_values(by="rating", ascending=False).head(50)
highly_rated_safety_pubs = top_5_pubs["local_authority"].value_counts()
highly_rated_safety_pubs.plot(kind= "pie", autopct= "%.1f%%")
plt.ylabel("")
plt.title("Top 50 safety rated pubs distribution")
st.pyplot()

st.write("Below, use the search box to find the safest pub by town:")
user_pub = st.text_input("Enter a town: ")

if user_pub:

    filtered_pubs = df_pubs[df_pubs['local_authority'].str.contains(user_pub, case=False, na=False)]


    sorted_pubs = filtered_pubs.sort_values(by='rating', ascending=False)


    st.write(f"The highest-safety-rated pubs in {user_pub} are:")
    for index, row in sorted_pubs.iterrows():
        st.write(f"{row['name']} - {row['rating']}")
