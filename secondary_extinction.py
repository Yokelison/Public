def secondary_extinction(sequence, G):
    """
    Simulates secondary extinction in a food web after the sequential removal of species.

    Parameters:
    ----------
    sequence : list
        The specified sequence of species to be removed from the food web.
    G : networkx.Graph
        The constructed food web represented as a graph.

    Returns:
    -------
    primary_extinct_rates : list
        A list of primary extinction rates at each step, where primary extinction refers 
        to the species removed directly based on the sequence.
    secondary_extinct_rates : list
        A list of secondary extinction rates at each step, where secondary extinction refers 
        to species that became isolated (no connections in the network) after primary removals.
    final_primary_rate : float
        The final primary extinction rate when all nodes in the graph have been removed.

    """
    secondary_extinct_rates = [0.0]
    primary_extinct_rates = [0.0]
    primary_removed_species = set()
    secondary_removed_species = set()
    total_nodes = G.number_of_nodes()

    for i, node in enumerate(sequence):
        if node not in secondary_removed_species:
            primary_removed_species.add(node)  # Add node to the set of removed species
            primary_extinct_rates.append(len(primary_removed_species) / total_nodes)  # Calculate primary extinction rate
            G.remove_nodes_from(primary_removed_species)  # Remove primary species from the graph
            isolated_nodes = {node for node in G.nodes() if G.degree(node) == 0}  # Find isolated nodes (secondary extinctions)
            G.remove_nodes_from(isolated_nodes)  # Remove isolated nodes from the graph
            secondary_removed_species.update(isolated_nodes)  # Add isolated nodes to secondary removed set
            secondary_extinct_rates.append(len(secondary_removed_species) / total_nodes)  # Calculate secondary extinction rate

            # If all nodes have been removed, return the results
            if len(primary_removed_species | secondary_removed_species) == total_nodes:
                return primary_extinct_rates, secondary_extinct_rates, primary_extinct_rates[-1]
