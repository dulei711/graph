import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Title of the webapp
st.title("Excel File Graph Analysis")

# Upload the Excel file
uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

# Check if the file is uploaded
if uploaded_file is not None:
    # Load the Excel file into a Pandas dataframe
    df = pd.read_excel(uploaded_file)

    # Display the dataframe
    st.write("Dataframe:", df)

    # Create the graph from the dataframe
    G = nx.Graph()

    # Add edges to the graph
    for index, row in df.iterrows():
        G.add_edge(row['Node 1'], row['Node 2'])

    # Display the graph
    plt.figure(figsize=(10, 10))
    pos = nx.spring_layout(G, seed=42)
    nx.draw_networkx_nodes(G, pos, node_size=1000)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, font_size=16, font_family="sans-serif")
    st.pyplot(plt)

    # Calculate some basic graph statistics
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    avg_degree = sum(dict(G.degree()).values()) / float(num_nodes)

    # Display the graph statistics
    st.write("Number of nodes:", num_nodes)
    st.write("Number of edges:", num_edges)
    st.write("Average degree:", avg_degree)
